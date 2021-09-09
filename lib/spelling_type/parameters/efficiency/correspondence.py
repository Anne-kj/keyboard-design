from lib.constants import alphabet


# 计算按键和字母的重合度
def cal_correspondence(alpha_key_dict: dict) -> float:
    correspondence = 0
    for i in alphabet:
        if alpha_key_dict[i] == i:
            correspondence += 1
    return correspondence * 0.01
