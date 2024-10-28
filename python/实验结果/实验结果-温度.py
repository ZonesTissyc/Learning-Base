import numpy as np

# 获取三次温度下的反应时间
t0 = float(input("输入第一次室温反应时间(s)："))
t30 = float(input("输入30度下的反应时间(s)："))
t50 = float(input("输入50度下的反应时间(s)："))

# 计算三次温度下的反应速率
v0 = 0.0008/t0
v30 = 0.0008/t30
v50 = 0.0008/t50
# 赋值 m,n
m = 1
n = 1
# 计算k值
k0 = v0/((0.08)(0.04))
k30 = v30/((0.08)(0.04))
k50 = v50/((0.08)(0.04))

# 计算T
T0 = 295.75
T30 = 303.15
T50 = 323.15

print(k0,k30,k50)


