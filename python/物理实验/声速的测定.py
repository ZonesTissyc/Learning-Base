# 声速的测定
import numpy as np

def theoretical_value():
    try:
        # 获取用户输入的大气压，单位：Pa
        p0 = float(input("请输入大气压p0:\t/(Pa)"))
        # 获取用户输入的室温，单位：°C
        t = float(input("输入室温t：\t/(°C)"))
        # 获取用户输入的水的饱和蒸汽压，单位：Pa
        e = float(input("输入水的饱和蒸汽压e：\t/(Pa)"))
        # 获取用户输入的相对湿度，单位：%
        H = float(input("输入相对湿度H：\t/(%)"))
        # 计算理论声速
        u = 331.6 * np.sqrt((1 + t / 273.15) * (1 + 0.326 * e * H / p0))
        print("理论声速为：", u)
        return u
    except ValueError:
        print("输入无效，请输入有效的数字。")
        return None

# 调用函数计算理论声速
u_theory = theoretical_value()
print(u_theory)