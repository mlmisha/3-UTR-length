import sys
import requests
import time

utr_dict = {}

xid = sys.argv[1]

def extractor (transctipt_id,k):
  server = "https://rest.ensembl.org"
  cds = f"/sequence/id/{transctipt_id}?type=cds"

  orf = requests.get(server+cds, headers={ "Content-Type" : "text/x-fasta",'User-Agent': f'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15_12{k}'})

  if not orf.ok:
    orf.raise_for_status()
    sys.exit()
  return orf.text.strip()


with open(f"PATH_TO_FILE_WITH_3'UTRs", mode = "r") as data:
    name = data.readline().strip()
    utr_seq = data.readline().strip()
    while name != "" and utr_seq != "":
        utr_dict[name] = utr_seq
        name = data.readline().strip()
        utr_seq = data.readline().strip()


transcripts = []
with open (f"PATH_TO_FILE_WITH_TRANSCRIPTS_OF_ORTHOLOGOUS_GENES.tsv", mode = "r") as data:
   tran = data.readline().strip()
   while tran != "":
      transcripts.append(tran)
      tran = data.readline().strip()

count = 0
result = []
stops = {"TAA":"", "TAG":"", "TGA":""}
lost = []
lost_seqs = []
for i in transcripts:
    if i in utr_dict:
      print(".",end = "",flush=True)
      if count%1000==0:
          print()
          print(count,xid,flush=True)
      failed = False
      try:
          cds = extractor(i,count)
      except requests.exceptions.HTTPError:
          failed = True
      except requests.exceptions.ConnectionError:
          attempts = 0
          while attempts<5:
              try:
                attempts+=1
                cds = extractor(i,count)
                break
              except:
                print("-",end="",flush=True)
                time.sleep(5)
          if attempts>=5:
            failed = True
      count+=1
      if not failed:
        stop_codon = cds[-3::]
        if stop_codon in stops:
          result.append([i, stop_codon,len(utr_dict[i])])
      else:
         lost.append(i)
         lost_seqs.append(utr_dict[i])
with open(f"../data/ORTHS/ORTHRES_{xid}.tsv", mode = "w") as out:
   print ("")
   for i in result:
      print(*i, sep="\t", file = out)

with open(f"PATH_to_lost_dir/lost_{xid}.tsv", mode = "w") as out: #to manage 3'UTRs lost due to some request errors
   print ("")
   for i in result:
      print(*i, sep="\t", file = out)
