# 用按键使用频次的方差来衡量均衡性
import numpy as np


# 计算方差
def cal_balance(key_number_dict: dict):
    v = key_number_dict.values()
    variance = np.var(np.fromiter(v, float))
    return variance
