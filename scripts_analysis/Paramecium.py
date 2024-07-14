result_cdna = {}
with open ("CDNA", mode = "r") as data: #cDNA file was donwloaded from https://ftp.ensemblgenomes.ebi.ac.uk/pub/protists/release-59/fasta/paramecium_tetraurelia/cdna/Paramecium_tetraurelia.ASM16542v1.cdna.all.fa.gz
    line = data.readline().strip()
    while line !="":
      name = line.split(" ")[0][1::]
      line = data.readline().strip()
      seq = []
      while not line.startswith(">") and line != "":
          seq.append(line)
          line = data.readline().strip()
      result_cdna[name]= "".join(seq)

result_cds = {}
with open ("CDS", mode = "r") as data: #CDS file was donwloaded from https://ftp.ensemblgenomes.ebi.ac.uk/pub/protists/release-59/fasta/paramecium_tetraurelia/cds/Paramecium_tetraurelia.ASM16542v1.cds.all.fa.gz
    line = data.readline().strip()
    while line !="":
      name = line.split(" ")[0][1::]
      line = data.readline().strip()
      seq = []
      while not line.startswith(">") and line != "":
          seq.append(line)
          line = data.readline().strip()
      result_cds[name] = "".join(seq)

stop_codons = {"TAA": [], "TAG": [], "TGA": []}
final = []
cds_names = result_cds.keys()
cdna_names = result_cdna.keys()

for gene, cds in result_cds.items():
    cdna = result_cdna[gene]
    cds_start = cdna.find(cds)
    utr_length = len(cdna) - cds_start - len(cds)
    stop_codon = cds[-3::]
    if stop_codon in stop_codons:
        final.append([gene, stop_codon, utr_length])

with open("../data/Paramecium_tetraurelia.RES.tsv", mode = "w") as out:
   for i in final:
      print(*i, sep="\t", file = out)
