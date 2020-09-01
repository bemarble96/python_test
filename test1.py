Sequence = ""
with open("sequences.fasta",'r') as handle:
    for line in handle:
        if line.startswith(">"):
            Sequence += ">"
        else:
            Sequence += line.strip()
Record_seq = Sequence.split(">")

Total_record = []
Record_G = []
Record_C = []
for seq in Record_seq:
    Total_record.append(len(seq))
    Record_G.append(seq.count("G"))
    Record_C.append(seq.count("C"))

Record1_GC = (Record_G[1] + Record_C[1])*100 / Total_record[1]      
Record2_GC = (Record_G[2] + Record_C[2])*100 / Total_record[2]      
Record3_GC = (Record_G[3] + Record_C[3])*100 / Total_record[3]      

print(round(Record1_GC,1))
print(round(Record2_GC,1))
print(round(Record3_GC,1))
