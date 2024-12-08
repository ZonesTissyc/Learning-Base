#定积分
import numpy as np
from scipy.integrate import quad #单重积分
def func(x):
    return np.arctan(np.sin(x)) #被积分函数
solution = quad(func, 0, np.pi/2) #返回一个元组，第0项为结果，第1项为误差
print(solution[0])
