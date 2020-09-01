import sys

file_name = sys.argv[1]

name_list = []

with open(file_name, 'r') as handle:
    for line in handle:
        name_list.append(line.strip())
    
unique_name_list = set(name_list)

print(len(unique_name_list))
                                           
                 
