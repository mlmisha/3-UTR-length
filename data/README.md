This folder contains tables files used for analysis. 

### Contents

- `EXP.tsv` is a TSV table with isoform expression data. Columns: Ensembl Transcript ID, average, maximum, median and total expression.
- `GENCODE.tsv` is a TSV table with Ensembl Transcript ID, Stop codon type and 3'UTR length for all human protein coding genes annotated in the GENCODE v47 (Rel. Oct 2024, GRCh38.p14)
- `GO_ORA_cytoplasmic_translation.tsv` is a result of GO ORA filtered by the "cytoplasmic translation" category
- `MANE.tsv` is a TSV table with Ensembl Transcript ID, Stop codon type and 3'UTR length for  human protein coding genes annotated in the GENCODE v47 (Rel. Oct 2024, GRCh38.p14) having MANE Select status (subset of `GENCODE.tsv`)
- `transcript_expression.tsv` final table of human protein-coding transcirpts with their 3'UTR length and mean/max/median/total expression (estimated from TPM)
- `transl_genes.txt` is a list of genes (entrez IDs) obtained from the file `GO_ORA_cytoplasmic_translation.tsv`

