import sys
import requests
import time

utr_dict = {}

xid = sys.argv[1]

def extractor (transctipt_id,k):
  server = "https://rest.ensembl.org"
  cds = f"/sequence/id/{transctipt_id}?type=cds"

  orf = requests.get(server+cds, headers={ "Content-Type" : "text/x-fasta",'User-Agent': f'fwefweffwwfapwjefnllw{k}'})

  if not orf.ok:
    orf.raise_for_status()
    sys.exit()
  return orf.text.strip()


with open(f"utrs_file_here", mode = "r") as data:
    name = data.readline().strip()
    utr_seq = data.readline().strip()
    while name != "" and utr_seq != "":
        if name in utr_dict:
            utr_dict[name].append(utr_seq)
        else:
            utr_dict[name] = [utr_seq]
        name = data.readline().strip()
        utr_seq = data.readline().strip()


transcripts = []
with open (f"file_with_unique_transcript_ids_here", mode = "r") as data:
   tran = data.readline().strip()
   while tran != "":
      transcripts.append(tran)
      tran = data.readline().strip()

count = 0
result = []
stops = ["TAA", "TAG", "TGA"]
for i in transcripts:
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
        if i in utr_dict:
            for utr in utr_dict[i]:
                result.append([i,stop_codon, len(utr)])

with open(f"../data/RES_Human_or_Rabbit.tsv", mode = "w") as out:
   print ("")
   for i in result:
      print(*i, sep="\t", file = out)
