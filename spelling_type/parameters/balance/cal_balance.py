# 用按键使用频次的方差来衡量均衡性
import numpy as np


# 计算方差
# d: 按键 -> 使用频次
def balance(d: dict):
    v = d.values()
    variance = np.var(np.fromiter(v, float))
    return variance


if __name__=='__main__':
    print(1)