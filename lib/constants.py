alphabet = "abcdefghijklmnopqrstuvwxyz"

initials = ["b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h",
            "j", "q", "x", "zh", "ch", "sh", "r", "z", "c", "s",
            "y", "w"]
finals = ["a", "ai", "an", "ang", "ao",
          "e", "ei", "en", "eng", "er",
          "i", "ia", "ian", "iang", "iao", "ie", "in", "ing", "iong", "iu",
          "o", "ong", "ou",
          "u", "ua", "uai", "uan", "uang", "ue", "ui", "un", "uo",
          "v", "ve"]


# 全拼键盘与字母的对应关系
def create_alpha_key_dict_old() -> dict:
    return {i: i for i in alphabet}


# 新的编码方法中键盘与字母的对应关系
def create_alpha_key_dict_new() -> dict:
    return {i: '' for i in initials + finals}
