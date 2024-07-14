def genes_extractor(path):
    all_genes = {}
    with open(path, mode = "r") as data:
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
  
with open("../results/MF_GENES_50_HUM.tsv", mode = "w") as out:
    gene_list_MF = genes_extractor("../data/MF_RIBO_50_HUM.tsv")
    for i in gene_list_MF:
        print(i, file = out)
      
with open("../results/CC_GENES_50_HUM.tsv", mode = "w") as out:
    gene_list_CC = genes_extractor("../data/CC_RIBO_50_HUM.tsv")
    for i in gene_list_CC:
        print(i, file = out)
      
with open("../results/BP_GENES_50_HUM.tsv", mode = "w") as out:
    gene_list_BP = genes_extractor("../data/BP_RIBO_50_HUM.tsv")
    for i in gene_list_BP:
        print(i, file = out)
