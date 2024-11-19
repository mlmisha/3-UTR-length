result = []
stops = {"TAA":"", "TAG":"", "TGA":""}
with open (GENCODE_PROTEIN_CODING_TRANSCRIPTS_FASTA_FILE, mode = "r") as data:
    line = data.readline().strip()
    while line!="":
        line = line.split("|")
        print(line)
        trans_id = line[0][1::].split(".")[0]
        utr_coords = [1,-1]
        print(line[len(line)-2])
        if line[len(line)-2].startswith("UTR3"):
            utr_coords = line[len(line)-2].split(":")[1].split("-")
        utr_length = int(utr_coords[1])-int(utr_coords[0])+1
        if utr_length >0:
            stop_coord = int(line[len(line)-3].split(":")[1].split("-")[1])
        line = data.readline().strip()
        trans_seq = []
        while not line.startswith(">") and line != "":
            trans_seq.append(line)
            line = data.readline().strip()
        transcript = "".join(trans_seq)
        if utr_length >0:
            stop_codon = transcript[stop_coord-3:stop_coord]
        else:
            stop_codon = transcript[-3::]
        if stop_codon in stops and utr_length>0:
            result.append([trans_id, stop_codon, utr_length])
with open("../data/GENCODE.tsv", mode = "w") as out:
    for i in result:
        print(*i, sep = "\t", file =out)
