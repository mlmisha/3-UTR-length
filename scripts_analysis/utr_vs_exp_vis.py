import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("../data/transcript_expression.tsv", sep = "\t")
#data = data[data["Length"]<150]


def len_group (length):
    if length <=10:
        res = "1-10"
    elif length<=30 and length>10:
        res = "11-30"
    elif length<=50 and length>30:
        res = "31-50"
    elif length<=150 and length>51:
        res = "51-150"
    elif length<=1000 and length>150:
        res = "151-1000"
    elif length<=7424 and length>1000:
        res = "1001-7424"
    else:
        res = ">7424"
    return res

data["Length_group"] = data["Length"].apply(len_group)

# MANE check
mane = pd.read_csv("../data/MANE.tsv", sep= "\t", names = ["Transcript_id"])
mane["Transcript_id"] = mane["Transcript_id"].str.split(".", expand=True)[0]
data_mane = data.merge(mane, on = "Transcript_id")


hue_order = ["1-10","11-30","31-50","51-150","151-1000", "1001-7424",">7424"]

fig, ax = plt.subplots(1,2)
plt.tight_layout()
sns.scatterplot(data = data, x = "Length", y = "sum_exp",hue = "Length_group", hue_order=hue_order,ax = ax[0])
ax[0].set_xlabel("3'UTR length, nt", fontsize = 14)
ax[0].set_ylabel("Expression, sum(TPM)", fontsize = 14)
ax[0].set_xscale("log")
ax[0].set_yscale("log")
ax[0].set_title("GENCODE", fontsize = 16)
ax[0].get_legend().remove()

sns.scatterplot(data = data_mane, x = "Length", y = "sum_exp",hue = "Length_group", hue_order=hue_order,ax = ax[1])
ax[1].set_xlabel("3'UTR length, nt", fontsize = 14)
ax[1].set_ylabel("Expression, sum(TPM)", fontsize = 14)
ax[1].set_xscale("log")
ax[1].set_yscale("log")
ax[1].set_title("MANE Select", fontsize = 16)

plt.legend(bbox_to_anchor=(0.5, 0), loc="lower center",
                bbox_transform=fig.transFigure, ncol=7, title = "3'UTR length, nt")
plt.show()
