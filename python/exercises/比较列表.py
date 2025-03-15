import random

ls1 = list()
ls2 = list()
for m in range(0,random.randint(8,20)):
    ls1.append(random.randint(0,500))
    ls2.append(random.randint(0,500))

print(ls1,"\n",ls2)
n = len(ls1)

for i in range(0,n):
    if(ls1[i]==ls2[i]):
        pass
    else:
        print("在第",i+1,"项不相等")
        break
else:
    print("列表相等")