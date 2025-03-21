fo = open("dna.txt","r")
i = -1
ls = []
name = []
for line in fo:
    if(line[0]==">"):
        i+=1
        name.append(line[10:13])
        ls.append("")
    ls[i] = ls[i]+line
    ls[i].replace("\n",'')

for o in range(i+1):
    print(name[i],":",ls[i])
