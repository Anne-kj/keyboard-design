from lib.constants import alphabet, initials, finals

# 使用网上成熟的双拼方案进行测试 https://zh.wikipedia.org/wiki/双拼
# 需要手动录入，于是选择最方便的方式录入后，再转换成 alpha_key_dict
shuang_pin_template_alpha_key_dict = {
    "b": "b",
    "p": "p",
    "m": "m",
    "f": "f",
    "d": "d",
    "t": "t",
    "n": "n",
    "l": "l",
    "g": "g",
    "k": "k",
    "h": "h",
    "j": "j",
    "q": "q",
    "x": "x",
    "r": "r",
    "z": "z",
    "c": "c",
    "s": "s",
    "y": "y",
    "w": "w",
    "a": "a",
    "e": "e",
    "i": "i",
    "o": "o",
    "v": "v",
    "u": "u",
}

xiao_he_shuang_pin_extra_key_alpha_dict = {
    "q": ["iu"],
    "w": ["ei"],
    "e": ["er"],
    "r": ["uan" ,"van"],
    "t": ["ue", "ve"],
    "y": ["un", "vn"],
    "u": ["sh"],
    "i": ["ch"],
    "o": ["uo"],
    "p": ["ie"],
    "a": [],
    "s": ["ong", "iong"],
    "d": ["ai"],
    "f": ["en"],
    "g": ["eng"],
    "h": ["ang"],
    "j": ["an"],
    "k": ["ing", "uai"],
    "l": ["iang", "uang"],
    "z": ["ou"],
    "x": ["ia", "ua"],
    "c": ["ao"],
    "v": ["zh", "ui"],
    "b": ["in"],
    "n": ["iao"],
    "m": ["ian"]
}

zi_ran_ma_extra_key_alpha_dict ={
    "q": ["iu"],
    "w": ["ia", "ua"],
    "e": ["er"],
    "r": ["uan", "van"],
    "t": ["ue", "ve"],
    "y": ["ing", "uai"],
    "u": ["sh"],
    "i": ["ch"],
    "o": ["uo"],
    "p": ["un", "vn"],
    "a": [],
    "s": ["ong", "iong"],
    "d": ["iang", "uang"],
    "f": ["en"],
    "g": ["eng"],
    "h": ["ang"],
    "j": ["an"],
    "k": ["ao"],
    "l": ["ai"],
    "z": ["ei"],
    "x": ["ie"],
    "c": ["iao"],
    "v": ["zh", "ui"],
    "b": ["ou"],
    "n": ["in"],
    "m": ["ian"]
}

pin_yin_jia_jia_extra_key_alpha_dict = {
    "q": ["er", "ing"],
    "w": ["ei"],
    "e": [],
    "r": ["en"],
    "t": ["eng"],
    "y": ["iong", "ong"],
    "u": ["ch"],
    "i": ["sh"],
    "o": ["uo"],
    "p": ["ou"],
    "a": [],
    "s": ["ai"],
    "d": ["ao"],
    "f": ["an"],
    "g": ["ang"],
    "h": ["iang", "uang"],
    "j": ["ian"],
    "k": ["iao"],
    "l": ["in"],
    "z": ["un", "vn"],
    "x": ["ue", "ve", "uai"],
    "c": ["uan", "van"],
    "v": ["zh", "ui"],
    "b": ["ia", "ua"],
    "n": ["iu"],
    "m": ["ie"]
}

zhi_neng_abc_extra_key_alpha_dict = {
    "q": ["ei"],
    "w": ["ian"],
    "e": ["ch"],
    "r": ["er", "iu"],
    "t": ["iang", "uang"],
    "y": ["ing"],
    "u": [],
    "i": [],
    "o": ["uo"],
    "p": ["uan", "van"],
    "a": ["zh"],
    "s": ["iong", "ong"],
    "d": ["ia", "ua"],
    "f": ["en"],
    "g": ["eng"],
    "h": ["ang"],
    "j": ["an"],
    "k": ["ao"],
    "l": ["ai"],
    "z": ["iao"],
    "x": ["ie"],
    "c": ["in", "uai"],
    "v": ["sh", "ve"],
    "b": ["ou"],
    "n": ["un", "vn"],
    "m": ["ui", "ue"]
}

guo_biao_extra_key_alpha_dict = {
    "q": ["ia", "ua"],
    "w": ["uan", "van"],
    "e": [],
    "r": ["en"],
    "t": ["ie"],
    "y": ["iu", "uai"],
    "u": ["sh"],
    "i": ["ch"],
    "o": ["uo"],
    "p": ["ou"],
    "a": [],
    "s": ["ong", "iong"],
    "d": ["ian"],
    "f": ["an"],
    "g": ["ang"],
    "h": ["eng"],
    "j": ["ing"],
    "k": ["ai"],
    "l": ["er", "in"],
    "z": ["un", "vn"],
    "x": ["ue", "ve"],
    "c": ["ao"],
    "v": ["zh", "ui"],
    "b": ["ei"],
    "n": ["iang", "uang"],
    "m": ["iao"]
}


def generate_alpha_key_dict(extra_key_alpha_dict: dict, spelling_type: str) -> list:
    print(f"生成{spelling_type}...", end='')
    alpha_key_dict = shuang_pin_template_alpha_key_dict.copy()
    for key in extra_key_alpha_dict.keys():
        for value in extra_key_alpha_dict[key]:
            if value in alpha_key_dict:
                raise KeyError(value + ' already exists')
            alpha_key_dict[value] = key
    for i in initials + finals:
        if i not in alpha_key_dict:
            raise KeyError(i)
    print('完成')
    return [alpha_key_dict, spelling_type]


test_alpha_key_dicts = [
    [{i: i for i in alphabet}, "old"],
    generate_alpha_key_dict(xiao_he_shuang_pin_extra_key_alpha_dict, "小鹤双拼"),
    generate_alpha_key_dict(zi_ran_ma_extra_key_alpha_dict, "自然码双拼"),
    generate_alpha_key_dict(pin_yin_jia_jia_extra_key_alpha_dict, "拼音加加双拼"),
    generate_alpha_key_dict(zhi_neng_abc_extra_key_alpha_dict, "智能ABC双拼"),
    generate_alpha_key_dict(guo_biao_extra_key_alpha_dict, "国标双拼"),
]
