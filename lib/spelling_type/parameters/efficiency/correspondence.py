from lib.constants import alphabet


# 计算按键和字母的重合度
# alphabet_key_dict：字母 -> 按键
def cal_correspondence(alphabet_key_dict: dict) -> int:
    correspondence = 0
    for i in alphabet:
        if alphabet_key_dict[i] == i:
            correspondence += 1
    return correspondence
