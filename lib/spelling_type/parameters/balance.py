# 用按键使用频次的方差倒数来衡量均衡性
# 为了使得均衡性不受文本规模影响（即均衡性在一定程度上只与编码方式有关），
# 故将方差除以汉字个数的平方后取倒数以得到最终结果
import numpy as np

from lib.text_info import text_info


# 计算均衡性
def cal_balance(key_number_dict: dict):
    v = key_number_dict.values()
    variance = np.var(np.fromiter(v, float))
    variance /= text_info.character_number_total ** 2
    variance *= 100
    return 1 / variance
