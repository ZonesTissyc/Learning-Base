# 编写一个函数，计算并返回两个数的最大公约数。

"""
采用辗转相除法： 设a>b，则a/b的余数为c，若c=0，则b为最大公约数，否则，a=b，b=c，再求a/b的余数，直到余数为0，此时的b即为最大公约数。

"""

def gcd(a,b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

# 测试

print(gcd(10,20))
    