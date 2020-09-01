import sys
import gzip



refGene_file = sys.argv[1]

transcriptID_list = []
exonStarts_list = []
exonEnds_list = []
exonLength_list = []

with gzip.open(refGene_file,'rb') as handle:
    for line in handle:
        splitted = line.decode("utf-8").strip().split("\t")
        transcriptID = splitted[1]
        exonStarts = splitted[9]
        exonEnds = splitted[10]
        transcriptID_list.append(transcriptID.strip())
        exonStarts_list = exonStarts.strip().split(",")                    
        exonEnds_list = exonEnds.strip().split(",")
        exonLength = 0
        for i in range(0,len(exonStarts_list)-1):
            exonLength += int(exonEnds_list[i]) - int(exonStarts_list[i]) +1
        exonLength_list.append(exonLength)



max_exonIndex= exonLength_list.index(max(exonLength_list))
print(transcriptID_list[max_exonIndex],"\t", max(exonLength_list))
                                                                                         
                                                                                  
