import sys

gene_tsv = sys.argv[1]

Sample2_list = []
Sample2_max = []
Result = []

with open(gene_tsv,'r') as gene:
    for line in gene:
        if line.startswith("gene"):
            continue
        splitted = line.strip().split("\t")
        geneID = splitted[0]
        sample2 = splitted[2]
        result = geneID + "\t" + sample2
        Sample2_list.append(float(sample2))   
        Result.append(result)
while len(Sample2_max) !=5 :    
      Sample2_max.append(max(Sample2_list))
      Sample2_list.remove(max(Sample2_list))

for geneID in Result[::-1]:
    for sample_name in Sample2_max:
        if str(sample_name) in geneID:
            print(geneID)                              
