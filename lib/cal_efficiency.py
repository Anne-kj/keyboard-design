# 用以下三个指标的加权来衡量输入效率
# 1. 新的编码方式与 26 全拼键盘上字母的对应程度（若对应程度高，则可降低学习成本，熟练度增加，输入效率增加） in [0, 26]
# 2. 总汉字数 /总按键数  in [1/6, 1]
# 3. 键位之间的距离（仅计算相同手指键位间的距离，不同手指间的均记为 0） in[0, 2]
from lib.constants import alphabet


def efficiency(alphabet_dict):
    effi = 0
    # 指标 1：对应程度
    correspondence = 0
    for i in alphabet:
        if alphabet_dict[i] == i:
            correspondence += 1

    # 指标 2：总汉字数 / 总按键数

    return effi
