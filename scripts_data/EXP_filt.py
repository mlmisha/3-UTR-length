import pandas as pd
import numpy as np

exp_data = pd.read_csv("../data/EXP.tsv", sep = "\t")
gc_trans = pd.read_csv("../data/GENCODE.tsv", sep = "\t", names=["Transcript_id","Stop","Length"])


exp_data = exp_data[exp_data["max_exp"]>0]
exp_data["Transcript_id"] = exp_data["Transcript_id"].str.split(".", expand=True)[0]

res = gc_trans.merge(exp_data, on="Transcript_id")

res.to_csv("../data/transcript_expression.tsv", sep = "\t",index = False)
