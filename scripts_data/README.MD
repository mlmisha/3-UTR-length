Hello! This is the folder for scripts I used to obtain the data to be analysed (scripts I used for analysis are in `scripts_analysis` folder)


### Contents

- `Paramecium.py` script is used to build the table of 3'UTR lengths for *Paramecium tetraurelia*. It is apart from other scripts, because *P.tetraurelia* is not presented in the UTRdb 2.0 we worked with. 
- `UTR.py` script is the main script used to obtain almost all the data used for analysis. It uses preliminarily prepared files with the structure like in the file `../data/Chlamydomonas_reinhardtii.txt`. It has `.txt` format to be readable on GitHub. Normally script works with files `.utrs` format
- `preparator.py` script is used to prepare raw gunzipped files from the database to be consumed by `UTR.py`. 
- `UTR_zeros.py` script is used to build the tables for each organism with transcripts without 3'UTR. Output tables from this script and `UTR.py` script has the same structure and then they were "organimwise" merged. Final output merged from both scripts is in ../data/Org_tables folder


