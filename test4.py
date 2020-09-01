

def mer(base1,base2,n):
    if n ==1:
        return base2
    k_mer = []
    for seq1 in base1:
        for seq2 in base2:
            k_mer.append(seq1+seq2)
    return mer(base1,k_mer,n-1) 

base1 = ["A","C","G","T"]
base2 = ["A","C","G","T"]

n = 7
mer_7=mer(base1,base2,n)
Result = []


for sequence in mer_7:
    if sequence == sequence[::-1]:
        Result.append(sequence)
print(len(Result))                   
