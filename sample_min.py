from __future__ import division
import os



SampleID =["N06A","N06B","N07A","N07B","N08A","N08B","N09A","N09B","N10A",
"N10B","T01A","T01B","T02A","T02B","T03A","T03B","T04A","T04B","T05A","T05B"]
Reads_count = []
Reads_assem = []
As_per = []
Reads_450 = []
Reads_N = []

sample_list = []
os.system("ls *.fastq > samples.txt")

with open("samples.txt",'r') as handle:
    for name in handle:
        sample_list.append(name.strip())
        

Read =[]
line_num = 0

for sample in sample_list:
    reads_cnt = 0
    with open(sample,'r') as handle:
        for line in handle:
            line_num += 1
            if line_num % 4 == 2:
                reads_cnt +=1
        Read.append(reads_cnt/2)    

oddlist = Read[0::2]
evenlist = Read[1::2]

Reads_count= [int(x+y) for x,y in zip(oddlist,evenlist)]


os.system("ls -d */ > as_samples.txt")

as_sample_list=[]
with open("as_samples.txt",'r') as handle:
    for name in handle:
        as_sample_list.append(name.strip())

as_line_num =0

for as_sample in as_sample_list:
    as_reads_cnt = 0
    read450_cnt = 0
    N_cnt = 0
    with open(as_sample+"/fastqjoin.join.fastq",'r') as handle:
        for line in handle:
            as_line_num += 1
            if as_line_num % 4 == 2:
                as_reads_cnt +=1
                if len(line) < 450 :
                    read450_cnt +=1
                if "N" in line:
                    N_cnt +=1
        Reads_assem.append(as_reads_cnt)
        Reads_450.append(read450_cnt)
        Reads_N.append(N_cnt)    
#print(Reads_N)

As_per = [x/y*100 for x,y in zip(Reads_assem,Reads_count)]
N_per = [x/y*100 for x,y in zip(Reads_N,Reads_assem)]

for i in range(0,20):
    print SampleID[i],Reads_count[i],Reads_assem[i],As_per[i],Reads_450[i],N_per[i]



os.system("rm samples.txt")
os.system("rm as_samples.txt")                                                          
