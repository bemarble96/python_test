import sys

Sequence = ""
Seq_dic = {}
fasta_file = sys.argv[1]

with open(fasta_file, 'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        Sequence +=line.strip()

for seq in Sequence:
     if seq in Seq_dic:
         Seq_dic[seq] +=1
     else:
         Seq_dic[seq] =1

Seq_val =list(Seq_dic.values())
Seq_item =list(Seq_dic.items())

cnt =5
while cnt !=0:
    cnt -=1
    max_index = Seq_val.index(max(Seq_val))
    Seq_val.remove(max(Seq_val))
    print(list(Seq_item[max_index])[0]+":"+str(list(Seq_item[max_index])[1]))
    Seq_item.remove(Seq_item[max_index])
