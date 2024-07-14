import requests
import sys
import requests, sys
import time

def extractor (transctipt_id,k):
  server = "https://rest.ensembl.org"
  cds = f"/sequence/id/{transctipt_id}?type=cds"

  orf = requests.get(server+cds, headers={ "Content-Type" : "text/x-fasta",'User-Agent': f'.dksdlksjflsdkjflssdfs{k}'})

  if not orf.ok:
    orf.raise_for_status()
    sys.exit()
  return orf.text.strip()

xid = sys.argv[1] #e.g file ../data/Chlamydomonas_reinhardtii.utrs

stop_codons = {"TAA":[], "TAG": [], "TGA":[]}
lost = []
count = 0
with open(f"{xid}",mode ="r") as data:
    name = data.readline().strip()
    utr_seq = name
    while name!="" and utr_seq!="":
      print(".",end = "",flush=True)
      if count%1000==0:
        print()
        print(count,xid,flush=True)
      failed = False
      try:
        cds = extractor(name,count)
      except requests.exceptions.HTTPError:
        failed = True
      except requests.exceptions.ConnectionError:
        attempts = 0
        while attempts<5:
            try:
              attempts+=1
              cds = extractor(name,count)
              break
            except:
              print("-",end="",flush=True)
              time.sleep(5)
        if attempts>=5:
          failed = True
      count+=1
      if not failed:  
        stop_codon = cds[-3::]
        utr_seq = data.readline().strip()
        utr_length = len(utr_seq)
        if stop_codon in stop_codons:
          stop_codons[stop_codon].append(utr_length)
        name = data.readline().strip()
      else:
        lost.append(name) #to be able to run the script again on transcripts that occasionaly were lost during the run
        name = data.readline().strip()
        name = data.readline().strip()

import pandas as pd

df = pd.DataFrame({key: pd.Series(value) for key, value in stop_codons.items()})
df.to_csv(f"{xid}.tsv", encoding="utf-8",index=False,sep="\t")
with open(f"{xid}.txt",mode = "w") as out:
    for i in lost:
        print(i, file = out)
datas = 0
for key,value in stop_codons.items():
   datas+=len(value)
print(f"TOTAL: {datas}")
