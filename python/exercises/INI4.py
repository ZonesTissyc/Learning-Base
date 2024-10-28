## 给定内容：两个正整数 a 和 b（a<b<10000）。
## 要求：返回从 a 到 b（包括 a 和 b）所有奇数整数的和。

# 定义a,b

a = int(4164)
b = int(8386)

# while循环

i = a 
x = 0
while i <= b :
    if i%2==1 :
        x += i
        i += 1
    else :
        i += 1
else :
    print(x)



