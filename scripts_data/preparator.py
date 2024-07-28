import sys

xig = sys.argv[1]


final = {}
with open(f"PATH_TO_THE_RAW_UTRs_FILE/{xig}",mode = "r") as data:
    line = data.readline().strip()
    seqs = []
    while line != "":
        if line.startswith(">|three"):
            name = line.split("|")[2]
            line = data.readline().strip()
            seq = []
            while not line.startswith(">") and line !="":
                seq.append(line)
                line = data.readline().strip()
            utr_temp_seq = "".join(seq)
            if name in final:
                final[name].append(utr_temp_seq)
            else:
                final[name] = [utr_temp_seq]
        else:
            while line != "" and not line.startswith(">|three"):
                line = data.readline().strip()

with open(f"PATH_TO_THE_RESULT/{xig}", mode = "w") as out:
 for key, value in final.items():
    final[key] = "".join(value)
    print(key, file = out)
    print(final[key], file = out)

