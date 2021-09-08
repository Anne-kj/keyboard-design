# 用按键使用频率的方差来衡量均衡性
import numpy as np


def balance(d: dict):
    v = d.values()
    variance = np.var(np.fromiter(v, float))
    return variance