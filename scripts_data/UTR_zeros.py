import sys
import requests
import time

utr_dict = {}

xid = sys.argv[1]

def extractor (transctipt_id,k):
  server = "https://rest.ensembl.org"
  cds = f"/sequence/id/{transctipt_id}?type=cds"

  orf = requests.get(server+cds, headers={ "Content-Type" : "text/x-fasta",'User-Agent': f'fwefwefwefwef'})

  if not orf.ok:
    orf.raise_for_status()
    sys.exit()
  return orf.text.strip()


transcripts = []
with open (f"PATH_TO_ENSEMBL_TRANSCRIPT_IDs_OF_THOSE_HAVING_ONLY_5'UTR_ENTRIES", mode = "r") as data:
   tran = data.readline().strip()
   while tran != "":
      transcripts.append(tran)
      tran = data.readline().strip()

count = 0
result = []
stops = {"TAA":"", "TAG":"", "TGA":""}
lost = []
lost_seqs = []
other_stops = []
for i in transcripts:
    if True:
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
          result.append([i, stop_codon,0])
        else:
          other_stops.append(i)
with open(f"PATH_TO_RESULT_FILE", mode = "w") as out:
   print ("")
   for i in result:
      print(*i, sep="\t", file = out)
