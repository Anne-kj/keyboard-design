from random import random, sample, choices

from lib.constants import alphabet, initials, finals


def generate_alpha_key_dict_randomly() -> dict:
    # 最终生成的 alpha_key_dict
    alpha_key_dict = {}
    # 表示每一个 key 出现的次数
    key_number = {a: 0 for a in alphabet}
    # key 出现次数越多，再次出现的概率应当越小。这里使用权重 w=(1/2)^n 实现
    key_weight = {a: 1 for a in alphabet}

    # 向 alpha_key_dict 增加新的映射，并同步修改 key_number 和权重
    def push(key, alpha):
        if alpha in alpha_key_dict:
            return
        alpha_key_dict[alpha] = key
        key_number[key] += 1
        key_weight[key] /= 2

    # 80% 概率都会生成26单字母和键盘对应的方案
    if random() < 0.8:
        correspondence = 26
    else:
        correspondence = int(random() * 16) + 10
    alpha_key_same_list = choices(alphabet, k=correspondence)
    for alpha in alpha_key_same_list:
        push(alpha, alpha)
    # push 剩下还没出现的 alpha
    for alpha in initials + finals:
        if alpha in alpha_key_dict:
            continue
        key = choices(alphabet, list(key_weight.values()))[0]
        push(key, alpha)
    # 返回生成的 alpha_key_dict
    return alpha_key_dict
