from xpinyin import Pinyin

from spelling_type.constants import filename, alphabet, initials, finals


# 将拼音切分成声母和韵母
def split_pinyin(pinyin: str):
    if pinyin[0] in initials:
        if pinyin[0:2] in initials:
            return pinyin[0:2], pinyin[2:]
        else:
            return pinyin[0:1], pinyin[1:]
    else:
        return None, pinyin


class TextInfo:
    # 文本原文
    text = ''
    # 文本中汉字数
    character_number = 0
    # 文本中拼音字母数
    alpha_number_total = 0
    # 文本中每个字母对应的频次
    alpha_number = {i: 0 for i in list(alphabet)}
    # 文本中声母韵母总数
    initial_final_number_total = 0
    # 文本中每个声母和韵母对应的总数
    initial_final_number = {i: 0 for i in initials + finals}

    def __init__(self):
        with open(filename, encoding='utf-8') as f:
            self.text = f.read()

        p = Pinyin()
        for word in self.text:
            # 统计汉字个数
            if '\u4e00' <= word <= '\u9fff':
                self.character_number += 1
                pinyin = p.get_pinyin(word)
                # 分别统计拼音的每个字母对应频次
                for c in word:
                    self.alpha_number[c] += 1
                # 统计声母韵母个数
                initial, final = split_pinyin(pinyin)
                if initial:
                    self.initial_final_number[initial] += 1
                if final:
                    self.initial_final_number[final] += 1
        # 统计所有字母的总频次
        self.alpha_number_total = sum(self.alpha_number)
        # 统计声母+韵母的总个数
        self.initial_final_number_total = sum(self.initial_final_number)


text_info = TextInfo()
