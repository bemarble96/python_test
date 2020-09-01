import sys

gene_file = sys.argv[1]
data_file = sys.argv[2]

Gene = {}
Data = {}
Result = {}
with open(gene_file,'r') as gene:
    for line1 in gene:
        Gene[line1.strip()] = "NA"   
        with open(data_file, 'r') as data:
            for line2 in data:
                splitted = line2.strip().split("\t")
                Data[splitted[0]] = splitted[1]
                if line1.strip() in Data:
                    Result[line1.strip()] = Data[line1.strip()]
                else:
                    Result[line1.strip()] = Gene[line1.strip()]

for key,value in Result.items():
    print(key+"\t"+value)                                                  

