from os import listdir
from os.path import isfile, join
import numpy as np
import pandas as pd

dir_path = "../data/Org_tables/"
filenames = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]

result = []
for i in filenames:
    if i.endswith("tsv"):
        print(i)
        data =  pd.read_csv(dir_path+i, delimiter="\t")
        med = data.median()
        count = np.sum(data.count())
        try:
            med_sum = med[0]+med[1]+med[2]
            result.append((i, med[0], med[1], med[2],med_sum, count))
        except IndexError:
            pass
result.sort(key=lambda x:x[4])
for i in result:
    print(*i, sep = "\t")
