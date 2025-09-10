import pandas as pd
import sys


print(f"READING", flush = True)
gtex_data = pd.read_csv(sys.argv[1], sep = "\t") #takes the same dataset as GTEx_expr.py script (check in README)
print("CALCULATING", flush = True)
gtex_data["transcript_id"] = gtex_data["transcript_id"].str.split(".",expand=True)[0]

tissue_data = pd.read_csv("../data/samples_tissues.tsv", sep = "\t")

samples = tissue_data["SAMPID"]
samp_tiss = tissue_data[["SAMPID","SMTS"]].set_index("SAMPID").to_dict()["SMTS"]
res_dict = {}

def tiss_expr (x):
    tiss_dict = {tissue:0 for tissue in tissue_data["SMTS"].unique()}
    res_dict[x["transcript_id"]] = tiss_dict
    for samp in samples:
        res_dict[x["transcript_id"]][samp_tiss[samp]]+=x[samp]
    return

gtex_data.apply(tiss_expr, axis =1)
res = pd.DataFrame(res_dict).T

res.reset_index().to_csv(sys.argv[2], sep = "\t", index = False)
