filename = 'data/text1.txt'
alphabet = "abcdefghijklmnopqrstuvwxyz"

initials = ["b","p","m","f","d","t","n","l","g","k","h",
            "j","q","x","zh","ch","sh","r","z","c","s",
            "y","w"]
finals = ["a","o","e","i","u","v","ai","ei","ui","ao",
          "ou","iu","ie","ve","er","an","en","in","un",
          "vn","ang","eng","ing","ong"]


# 全拼键盘与字母的对应关系
def create_alphabet_dict_old() -> dict:
    alphabet_dict_old = {}
    for i in alphabet:
        alphabet_dict_old[i] = i
    return alphabet_dict_old


# 新的编码方法中键盘与字母的对应关系
def create_alphabet_dict_new() -> dict:
    alphabet_dict_new = {}
    for i in alphabet:
        alphabet_dict_new[i] = 0
    return alphabet_dict_new
