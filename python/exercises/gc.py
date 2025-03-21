from gc_count import gc_count
fo = open('gc_dna2.txt',"r")

ls = []
name = []
i = -1
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