import pandas as pd
import numpy as np
import sys


print(f"READING {sys.argv[1]}", flush = True)
gtex_data = pd.read_csv(sys.argv[1], sep = "\t")
print("CALCULATING", flush = True)
gtex_data = gtex_data.replace(0, np.NaN)

gtex_data["avg_exp"] = gtex_data.drop(["transcript_id","gene_id"],axis=1).mean(axis = 1).round(2)
gtex_data["max_exp"] = gtex_data.drop(["transcript_id","gene_id"],axis=1).max(axis = 1)
gtex_data["med_exp"] = gtex_data.drop(["transcript_id","gene_id"],axis=1).median(axis = 1).round(2)
gtex_data["sum_exp"] = gtex_data.drop(["transcript_id", "gene_id"], axis=1).sum(axis=1)

res = gtex_data[["transcript_id","avg_exp","max_exp","med_exp", "sum_exp"]]
print("SAVING", flush = True)
res.to_csv(sys.argv[2], sep = "\t", index = False, header = ["Transcript_id","avg_exp","max_exp","med_exp", "sum_exp"])
