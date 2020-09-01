import sys


file_vcf = sys.argv[1] 


with open(file_vcf, 'r') as handle:
     for line in handle:
         if line.startswith("#"):
             continue
         splitted = line.strip().split("\t")
         chrom = splitted[0]
         pos = splitted[1]
         Ref_Alt = splitted[3]+","+splitted[4]
         Ref_Alt_split = Ref_Alt.split(",")
         FORMAT = splitted[9]
         GT = FORMAT.split(":")[0]
         Ref = int(GT.split("/")[0])
         Alt = int(GT.split("/")[1])
         print("{0}    {1}   {2}    {3}/{4}".format(chrom,pos,GT,Ref_Alt_split[Ref],Ref_Alt_split[Alt]))  


