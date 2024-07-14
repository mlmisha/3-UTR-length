import sys

xig = sys.argv[1]

with open(f"./{xig}",mode = "r") as data:
    line = data.readline().strip()
    names = []
    seqs = []
    while line != "":
        if line.startswith(">|three"):
            names.append(line.split("|")[2])
            line = data.readline().strip()
            seq = []
            while not line.startswith(">") and line !="":
                seq.append(line)
                line = data.readline().strip()
            seqs.append("".join(seq))
        else:
            while line != "" and not line.startswith(">|three"):
                line = data.readline().strip()
with open(f"PATH_TO_THE_RESULT",mode = "w") as out:
    for i in range(len(names)):
        print(names[i],file=out)
        print(seqs[i],file=out)
