import requests
import sys
import requests, sys
import time

xid = sys.argv[1]

def extractor (transctipt_id,k):
  server = "https://rest.ensembl.org"
  cds = f"/sequence/id/{transctipt_id}?type=cds"

  orf = requests.get(server+cds, headers={ "Content-Type" : "text/x-fasta",'User-Agent': f'erglernglekrnglekrgnlerkgn{k}'})

  if not orf.ok:
    orf.raise_for_status()
    sys.exit()
  return orf.text.strip()

stop_codons =[]
stops = ["TAA","TAG","TGA"]
lost = []
lost_seq = []
with open(f"PATH_TO_THE_PREPARED_3'UTRs_FILE/{xid}",mode ="r") as data:
    name = data.readline().strip()
    utr_seq = name
    while name!="" and utr_seq!="":
      print(".",end = "",flush=True)
      if count%1000==0:
        print()
        print(count,flush=True)
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
        print(name)
        stop_codon = cds[-3::]
        utr_seq = data.readline().strip()
        utr_length = len(utr_seq)
        if stop_codon in stops:
          stop_codons.append([name, stop_codon, utr_length])
        name = data.readline().strip()
      else:
        lost.append(name)
        lost_s = data.readline().strip()
        lost_seq.append(lost_s)
        name = data.readline().strip()

with open(f"PATH_TO_THE_RESULT_DIR/RES_{xid}.tsv", mode = "w") as out:
    for i in stop_codons:
        print(*i, sep="\t", file = out)
with open(f"PATH_TO_THE_LOST_DIR/LOST_{xid}.tsv", mode = "w") as out: #to manage 3'UTRs lost due to some request errors 
    for i in range(len(lost)):
        print(lost[i], file = out)
        print(lost_seq[i], file = out)
