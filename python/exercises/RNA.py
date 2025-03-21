## Given: A DNA string t having length at most 1000 nt.
## Return: The transcribed RNA string of t.

# 定义DNA片段

DNA_string = """GGTGCTTGGAGCATTGAGGGCGAACAACAGAATGCGGTACAGCGAAGTTTGCCATAAGCAGGGCGTGGGTCAGCCTCCTATAGTTGGCTCCTTGTGACACGACGGGGCTATGCGCTATGGTCTGGGCCAACATGGTAACGTCCCCCGTTTGACAGGTCGATGACAAAGCGTCATCATATGCTGTCCTCGGGTGACCATGTACGCAGAGAATTTCTACGCGCCTTGATTTTTTCTAAGGCACGGCGATGCCCGGACGGCGTTCCCATGCCGGTCGACTTGCGCATATCGTGGGTAACTGCCCCCGCGGAGCTAAGGCACCGAGAGCGACTTCATCGAGTAGCATTACACCGGAACGTGTATAGTTATGCTCGATTACACACCTGTCCTTAAGGTCGAGATCCTATCTGCGACTATTACGATACCTCCCTATTGAATGCGCCCCTGGACCCCATACGATGATCAGCGTTCCCCTTTCCTGTACGATCTGCTGACCTTTTACCTAGACCTTCCGCGTGCGCCACATACCCGCACGACATATCTCTCCGAACTCTAGCGGCGCATGCAGTTCCGAATGAAGCATGTCAGGGGGTCGCCCAATCAAGCATGATAGATTCGTGTAAGGCCGTAGACTGGGTGAAAAAAAACACCCTTTGTTTGCGCCGCCCAGTAGATTTAGTAAAATAGTAAACCGGAAACATATAGCTATAATGGACTATAAGGATTGCCTACTGTTCTTACACGGTCACAGATTGCGTGTGCCCTTTCCATCGCTCACGAGGGGAGATCCTCTTAGCGTCCCGCCCTATGCCCCCAGACGGTGTACGGTATTAATGTGTCGCTGGGTCCCGAGTGCCGCAAAGGCGCGGGAAATGGTTTATAAAACCGGCTTTATGTATTGTCACTGTATTTCGCTC
"""

# 使用.replace函数替换

RNA_string = DNA_string.replace("T","U")

print(RNA_string)