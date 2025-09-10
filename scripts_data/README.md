- `EXP_filt.py` filters only protein-coding transcripts with annotated 3'UTRs we were working with and merges expression data with data on 3'UTR length and stop codon. Output is in `transcript_expression.tsv`
- `GTEx_expr.py` script that takes gunzipped GTEx dataset (https://storage.googleapis.com/adult-gtex/bulk-gex/v10/rna-seq/GTEx_Analysis_v10_RSEMv1.3.3_transcripts_tpm.txt.gz) and count mean, max, median and total TPM for each transcript in all the samples. It's written as it is because we splitted the original file into several pieces and analysed them separately. Output combined from all separate outputs is in `../data/EXP.tsv`
- `obtain_lengths.py` used to parse the file with annotated protein-coding human transcripts from GENCODE. The output is `../data/GENCODE.tsv`
- `tiss_exp.py` script to calculate tissue-specific isoform expression, taking sample annotation from `../data/samples_tissues.tsv`





