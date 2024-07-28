Hello! This folder contains data for analysis

- `Org_tables` folder contains final tables of 3'UTR length for each organism separately
- `Chlamydomonas_reinhardtii.txt` is an example of file used by the `../scripts_data/UTR.py` script to build the final table. The data in in this file is a modified file, downloaded from the UTRdb 2.0 database. Modification is made with `../scripts_data/preparator.py` script. It has `.txt` format to be readable on GitHub, script also work with file in `.utrs` format that remains after `../scripts_data/preparator.py` launch. 
- `HK_genes.txt` is a list of human housekeeping genes, obtained from https://www.tau.ac.il/~elieis/HKG/
- `Human_total_list.tsv` is a table of genes and corresponding transcripted obtained from the UTRdb 2.0
- `ORTHRES_HT.tsv` is a final table for human genes orthologous to the rabbit ones
- `ORTHRES_RT.tsv` is a final table for rabbit genes orthologous to the human ones
- `Oryctolagus.tsv` is a table of genes and corresponding transcripted obtained from the UTRdb 2.0
- `Paramecium_tetraurelia.RES.tsv` is a final table for *Paramecium tetraurelia*
- `RES_Arabidopsis_lyrata.v.1.0.54.utrs.tsv` is a final table for *Arabidopsis lyrata*
- `RES_Drosophila_willistoni.dwil_caf1.54.utrs.tsv` is a final table for *Drosophila willistoni*
- `RES_Homo_sapiens.GRCh38.107.utrs.tsv` is a final table for human.
- `RES_Myotis_lucifugus.Myoluc2.0.107.utrs.tsv` is a final table for *Myotis lucifugus*
- `RES_Oryctolagus_cuniculus.OryCun2.0.107.utrs.tsv` is a final table for rabbit
- `RES_Ostreococcus_lucimarinus.ASM9206v1.54.utrs.tsv` is a final table for *Ostreococcus lucimarinus*
- `TOTAL_PY.tsv.zip` is a final merged table, contating all infromation from all the organisms analysed

