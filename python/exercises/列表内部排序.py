# 排序一个数字列表
import random
ls = list()

for m in range(0,random.randint(10,20)):
    ls.append(random.randint(0,500))

n = len(ls)

# 从小到大排序
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if ls[j+i+1] < ls[i]:
            ls[j+i+1],ls[i] = ls[i],ls[j+i+1]


print("从小到大排序：\n",ls)

print()

# 从大到小排序
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if ls[j+i+1] > ls[i]:
            ls[j+i+1],ls[i] = ls[i],ls[j+i+1]

print("从大到小排序：\n",ls)
