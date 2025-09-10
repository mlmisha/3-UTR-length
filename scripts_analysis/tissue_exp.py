import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


tiss_exp = pd.read_csv("OUTPUT OF ../scripts_data/tiss_exp.py", sep ="\t")
tiss_exp = tiss_exp.rename(columns={"index":"Transcript_ID"})

len_data = pd.read_csv("../data/GENCODE.tsv", sep ="\t", names = ["Transcript_ID", "Stop", "Length"])

plot_data = len_data.merge(tiss_exp, on = "Transcript_ID")

plot_data_10 = plot_data[plot_data["Length"] <=10].drop(["Transcript_ID","Length", "Stop"], axis = 1).sum(axis = 0)
plot_data_30 = plot_data[(plot_data["Length"] <=30)&(plot_data["Length"] >10)].drop(["Transcript_ID","Length", "Stop"], axis = 1).sum(axis = 0)
plot_data_50 = plot_data[(plot_data["Length"] <=50)&(plot_data["Length"] >30)].drop(["Transcript_ID","Length", "Stop"], axis = 1).sum(axis = 0)
plot_data_150 = plot_data[(plot_data["Length"] <=150) & (plot_data["Length"] > 30)].drop(["Transcript_ID","Length", "Stop"], axis = 1).sum(axis = 0)
plot_data_1000 = plot_data[(plot_data["Length"] <=1000) & (plot_data["Length"] > 150)].drop(["Transcript_ID","Length", "Stop"], axis = 1).sum(axis = 0)
plot_data_7500 = plot_data[(plot_data["Length"] <=7424) & (plot_data["Length"] > 1000)].drop(["Transcript_ID","Length", "Stop"], axis = 1).sum(axis = 0)
plot_data_10000 = plot_data[plot_data["Length"] >7424].drop(["Transcript_ID","Length", "Stop"], axis = 1).sum(axis = 0)

frame = {"1-10":plot_data_10,"11-30":plot_data_30, "31-50":plot_data_50,"51-150":plot_data_150, "151-1000":plot_data_1000, "1000-7424":plot_data_7500, ">7424":plot_data_10000}

plot_data = pd.DataFrame(frame)
plot_data = plot_data.div(plot_data.sum(axis=1), axis = 0)*100

plot_data.plot.bar(stacked = True)

handles, labels = plt.gca().get_legend_handles_labels() 
  
order = [6, 5, 4,3, 2,1,0]

plt.xlabel("Sample", fontsize = 16)
plt.ylabel("Expression ratio, %", fontsize = 16)
plt.yticks(np.arange(0, 101, 10))
plt.legend([handles[i] for i in order], [labels[i] for i in order], loc='center left',bbox_to_anchor=(1.0, 0.5), title = "3'UTR length, nt")
plt.show()
