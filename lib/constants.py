alphabet = "abcdefghijklmnopqrstuvwxyz"

initials = ["b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h",
            "j", "q", "x", "zh", "ch", "sh", "r", "z", "c", "s",
            "y", "w"]
finals = ["a", "o", "e", "i", "u", "v", "ai", "ei", "ui", "ao",
          "ou", "iu", "ie", "ve", "er", "an", "en", "in", "un",
          "vn", "ang", "eng", "ing", "ong"]


# 全拼键盘与字母的对应关系
def create_alphabet_key_dict_old() -> dict:
    return {i: i for i in alphabet}


# 新的编码方法中键盘与字母的对应关系
def create_alphabet_key_dict_new() -> dict:
    return {i: '' for i in initials + finals}
