## Given: A DNA string s of length at most 1000 nt.
## Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

# 导入编码，调用count函数

DNA_string = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

A = "A"
C = "C"
G = "G"
T = "T"

count_A = DNA_string.count(A)
count_C = DNA_string.count(C)
count_G = DNA_string.count(G)
count_T = DNA_string.count(T)

print(count_A,count_C,count_G,count_T)
