from xpinyin import Pinyin


# 统计每个字母在文本中出现的频次
def count_text(filename: str) -> dict:
    with open(filename, encoding='utf-8') as f:
        a = f.read()
        p = Pinyin()
        pinyin = p.get_pinyin(a)
        s = pinyin.split('-')
        s1 = ''.join(s[0:])

        # 统计字母出现频次
        alpha_count = {}
        for i in "abcdefghijklmnopqrstuvwxyz":
            alpha_count[i] = s1.count(i)
        return alpha_count


def count_character_number(filename: str):
    character_number = 0
    with open(filename, encoding= 'utf-8') as f:
        str = f.read()
        for s in str:
            if '\u4e00' <= s <= '\u9fff':
                character_number += 1
    return character_number


def count_press_number(filename: str):
    press_number = sum(count_text(filename).values())
    return press_number
