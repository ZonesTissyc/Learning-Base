from gc_count import gc_count
fo = open('python\exercises\gc_dna2.txt',"r")

ls = [] # 创建列表，用于存储每个dna序列
name = [] # 创建列表，存储每个序列的编号，索引与dna序列对应
i = -1 # 用于列表索引
for line in fo:
    if(line[0]=='>'):
        i += 1
        name.append(line[1:14])
        ls.append("")
    else:
        ls[i]+=line
lsn = []
for a in ls:
    lsn.append(gc_count(a))
ind = lsn.index(max(lsn))

print(name[ind])
print(gc_count(ls[ind])*100)
fo.close