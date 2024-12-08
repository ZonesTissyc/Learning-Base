import sympy
from scipy.integrate import quad
import numpy as np

# 定义符号变量
x = sympy.Symbol('x')
# 定义被积函数（使用符号表达式）
f_sympy = x ** 2
# 求原函数（不定积分），得到的F是一个包含原函数表达式及常数项的对象
F = sympy.integrate(f_sympy, x)
# 将符号表达式转换为可调用的Python函数
F_lambda = sympy.lambdify(x, F, 'numpy')

# 示例输入一组x值
x_numpy = np.array([1, 2, 3])
# 计算对应x值的原函数的值（相当于求不定积分在这些点的取值）
result = F_lambda(x_numpy)
print(result)