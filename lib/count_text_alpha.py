from xpinyin import Pinyin


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