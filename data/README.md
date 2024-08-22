Hello! This folder contains data for analysis

- `Org_tables` folder contains final tables of 3'UTR length for each organism separately
- `Chlamydomonas_reinhardtii_for_UTR.py.txt` is an example of file used by the `../scripts_data/UTR.py` script to build the final table. The data in in this file is a modified file, downloaded from the UTRdb 2.0 database. Modification is made with `../scripts_data/preparator.py` script. It has `.txt` format to be readable on GitHub, script also work with file in `.utrs` format that remains after `../scripts_data/preparator.py` launch.
- `Chlamydomonas_reinhardtii_for_UTR_zeros.py.txt` is an example of file used by the `../scripts_data/UTR_zeros.py` script to build the  table of transcipts without 3'UTR. The data in in this file is a list of Ensembl transcript IDs that has only 5'UTR entries in the UTRdb 2.0.
- `HK_genes.txt` is a list of human housekeeping genes, obtained from https://www.tau.ac.il/~elieis/HKG/
- `Human_trans_gene_total.tsv` is a table of genes and corresponding transcripted obtained from the UTRdb 2.0
- `Paramecium_tetraurelia.RES.tsv` is a final table for *Paramecium tetraurelia*
- `RABORTH.tsv` is a table with 3'UTR lengths for rabbit genes having human orthologs
- `RES_Arabidopsis_lyrata.v.1.0.54.utrs.tsv` is a final table for *Arabidopsis lyrata*
- `RES_Drosophila_willistoni.dwil_caf1.54.utrs.tsv` is a final table for *Drosophila willistoni*
- `RES_Homo_sapiens.GRCh38.107.utrs.tsv` is a final table for human.
- `RES_Oryctolagus_cuniculus.OryCun2.0.107.utrs.tsv` is a final table for rabbit
- `RES_Ostreococcus_lucimarinus.ASM9206v1.54.utrs.tsv` is a final table for *Ostreococcus lucimarinus*
- `RES_Phlebotomus_perniciosus_gca918844115.pperniciosus_illum_n82538_165Mb.54.utrs.tsv` is a final table for *Phlebotomus preniciosus*
- `Rabbit_trans_gene_total.tsv` is a table of genes and corresponding transcripted obtained from the UTRdb 2.0
- `human_house.tsv` is a table of 3'UTR lengths corresponding to human housekeeping genes
- `TOTAL_PY.tsv.zip` is a final merged table, contating all infromation from all the organisms analysed
  

