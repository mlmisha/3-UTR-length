Hello! This is the folder for scripts I used to obtain the data to be analysed (scripts I used for analysis are in `scripts_analysis` folder)


### Contents

- `Paramecium.py` script is used to build the table of 3'UTR lengths for *Paramecium tetraurelia*. It is apart from other scripts, because *P.tetraurelia* is not presented in the UTRdb 2.0 we worked with. 
- `UTR.py` script is the main script used to obtain almost all the data used for analysis. It uses preliminarily prepared files with the structure like in the file `../data/Chlamydomonas_reinhardtii.utrs`
- `preparator.py` script is used to prepare raw, just downloaded `.gz` files from the database to be consumed by `UTR.py`. 
- `UTR_trans.py` script is used to collect the same data about 3'UTR length, but also keep the transcript ID. 
- `UTR_orth.py` script is used to build the tables for orthologous human and rabbit genes. So the result is the same as from `UTR_trans.py`script, but the procedure is a little different
