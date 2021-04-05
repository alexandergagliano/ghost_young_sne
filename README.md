# Host Matching for Young SNe
A quick wrapper to find the host galaxies of young SN candidates using the astro_ghost package.

## Steps for installing ghost and associating SNe:
1. Create a clean conda environment (optional, but makes sure packages don't conflict)

2. Run the following code:
```bash
pip install astro_ghost
```
3. Run the command 
```bash
python youngSNe_ghost.py <csv>
```

at the command line, passing in the path to the csv file (that you got from the SQL Explorer Script). 
