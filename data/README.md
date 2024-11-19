This folder contains tables files used for analysis. 

### Contents

- `GENCODE.tsv` is a TSV table with Ensembl Transcript ID, Stop codon type and 3'UTR length for all human protein coding genes annotated in the GENCODE v47 (Rel. Oct 2024, GRCh38.p14)
- `MANE.tsv` is a TSV table with Ensembl Transcript ID, Stop codon type and 3'UTR length for  human protein coding genes annotated in the GENCODE v47 (Rel. Oct 2024, GRCh38.p14) having MANE Select status (subset of `GENCODE.tsv`)
- `GO_ORA_cytoplasmic_translation.tsv` is a result of GO ORA filtered by the "cytoplasmic translation" category
- `transl_genes.txt` is a list of genes (entrez IDs) obtained from the file `GO_ORA_cytoplasmic_translation.tsv`

