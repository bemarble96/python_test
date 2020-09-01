import sys

file_vcf = sys.argv[1]

PASS_cnt = 0
with open(file_vcf,'r') as handle:
    for line in handle:
        if line.startswith("#"):
            continue
        header = line.strip().split("\t")
        if header[6] == "PASS":
           PASS_cnt += 1

print(PASS_cnt)
