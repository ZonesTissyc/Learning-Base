## 给定内容：一个长度不超过 200 个字母的字符串 s 和四个整数 a、b、c、d。
## 要求：返回这个字符串的切片，从索引 a 到 b 和索引 c 到 d（中间有空格），包括 s [b] 和 s [d]。

import numpy

# 定义a,b,c and d

a = int(75)
b = int(81)
c = int(128)
d = int(137)

# 定义字符 string_0
string_0 = "sM191wpjllSpxVT6evVqv8cVu3eZn0dM4JwZOxG4s6eprunFvBg68pkOQIMtLxy6K7EJnD0NlmiLeiurusUHtxjSombw4drwE7PcRgAG2FllixAyXKWn1olNie5VAQb5ladogensisazXPy3kPjSZHumOwUFlfReeguvL8ojNcAnG1UJmVj."

# 处理

pr_0 = string_0[a:b+1] + " " + string_0[c:d+1]
print(pr_0)