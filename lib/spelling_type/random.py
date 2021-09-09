from random import random, sample

from lib.constants import alphabet


def generate_alpha_key_dict_randomly() -> dict:
    alpha_key_dict = {}
    # 80% 概率都会生成字母和键盘对应的概率
    if random() < 0.8:
        correspondence = 26
    else:
        correspondence = int(random() * 16) + 10
    alpha_key_same_list = sample(alphabet, correspondence)
    for a in alpha_key_same_list:
        alpha_key_dict[a] = a

