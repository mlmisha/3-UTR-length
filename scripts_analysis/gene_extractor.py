def genes_extractor(path):
    all_genes = {}
    with open(path, mode = "r") as data:
        line = data.readline().strip()
        line = data.readline().strip()
        while line !="":
            print(line)
            line = line.split("\t")
            print(line)
            genes = line[7].split("/")
            print(genes)
            for i in genes:
                if not i in all_genes:
                    all_genes[i] = ""
            line = data.readline().strip()
    result = list(all_genes.keys())
    print(result)
    return result

with open("../results/GENES_50_HUM.tsv", mode = "w") as out:
    gene_list_MF = genes_extractor("../results/hum_11_50_go_ribo.tsv")
    for i in gene_list_MF:
        print(i, file = out)
