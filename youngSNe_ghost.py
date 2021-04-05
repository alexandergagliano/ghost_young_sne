#Candidate SN Host Info

# You need to run the SQL Explorer Script "" and download the csv file this produces.
#
from __future__ import print_function
import sys
import argparse
import numpy as np
import scipy as sp
import pandas as pd
from ps1 import PS1_query
import astropy
import time
import os
import sys
from astro_ghost.PS1QueryFunctions import getAllPostageStamps
from astro_ghost.TNSQueryFunctions import getTNSSpectra
from astro_ghost.NEDQueryFunctions import getNEDSpectra
from astro_ghost.ghostHelperFunctions import *
from astropy.coordinates import SkyCoord
from astro_ghost.classifier import classify
from sklearn import preprocessing
from astropy import units as u
import pandas as pd
from datetime import datetime

verbose = 1
parser = argparse.ArgumentParser(description='Young Candidates:')
parser.add_argument('file', type=str, help='input csv file',default=None)
condits=parser.parse_args()
file = condits.file
#file = '/Users/alexgagliano/Documents/Research/YSE/young_sne/trigger_checklist/New_young_objects.csv'
candidates=pd.read_csv(file,sep=',',header=0)

#we want to include print statements so we know what the algorithm is doing
verbose = 1

#download the database from ghost.ncsa.illinois.edu
#note: real=False creates an empty database, which
#allows you to use the association methods without
#needing to download the full database first
getGHOST(real=False, verbose=verbose)

candidates
#create a list of the supernova names and their skycoords (these three are from TNS)
snName = candidates['name'].values

snCoord = []
for i in np.arange(len(snName)):
    snCoord.append(SkyCoord(candidates['ra'].values[i]*u.deg, candidates['dec'].values[i]*u.deg, frame='icrs'))

# run the association algorithm!
print("Ingesting %i recent candidates from YSE-PZ"%(len(candidates.name)))
no_host_flag=[]
host_flag=[]
print('Checking host environments')
hosts = getTransientHosts(snName, snCoord, verbose=verbose, starcut='normal', gradientAscent=False)

host_flag = hosts['TransientName'].values
no_host_flag = candidates.loc[~candidates['name'].isin(hosts['TransientName'].values), 'name'].values
print("Found hosts for:")
for obj in host_flag:
    print(obj)
print("No hosts found for:")
for obj in no_host_flag:
    print(obj)
print('Total objects meeting all selection criteria: (%i/%i)'%(len(host_flag),(len(candidates.name))))
