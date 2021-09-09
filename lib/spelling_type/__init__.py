from lib.constants import alphabet
from lib.spelling_type.heatmap import draw_heatmap_by_key_number_dict
from lib.spelling_type.parameters.balance import cal_balance
from lib.spelling_type.parameters.efficiency.cal_efficiency import efficiency
from lib.spelling_type.parameters.efficiency.ck_ratio import cal_key_character_ratio
from lib.spelling_type.parameters.efficiency.correspondence import cal_correspondence
from lib.spelling_type.parameters.efficiency.distance import cal_average_distance_between_keys
from lib.text_info import text_info


class SpellingType:
    # spelling_type 为 old 表示全拼，为 new 表示新的编码方法
    spelling_type = ''
    # 键盘与字母的对应关系
    alpha_key_dict = {}
    # 按键的频次
    key_number_dict = {i: 0 for i in alphabet}
    key_number_total = 0
    # 各类指标
    balance = 0
    correspondence = 0
    key_character_ratio = 0
    average_distance_between_keys = 0
    efficiency = 0
    score = 0

    # spelling_type 为 old 表示全拼，为 new 表示新的编码方法
    def __init__(self, alpha_key_dict: dict, spelling_type: str):
        if spelling_type not in ("old", "new"):
            raise ValueError
        self.spelling_type = spelling_type

        self.alpha_key_dict = alpha_key_dict.copy()
        if spelling_type == "old":
            self.key_number_dict = text_info.alpha_number_dict.copy()
        else:
            for key, value in alpha_key_dict.items():
                self.key_number_dict[value] += text_info.initial_final_number_dict[key]
        self.key_number_total = sum(self.key_number_dict.values())

    def cal_parameters(self):
        self.balance = cal_balance(self.key_number_dict)
        self.correspondence = cal_correspondence(self.alpha_key_dict)
        self.key_character_ratio = cal_key_character_ratio(self.key_number_total)
        self.average_distance_between_keys = \
            cal_average_distance_between_keys(self.alpha_key_dict,
                                              self.key_number_total,
                                              self.spelling_type)
        # 加权求和
        self.efficiency = self.correspondence * 5 \
                          + 12 / self.key_character_ratio \
                          + 0.2 / self.average_distance_between_keys
        self.score = self.balance * self.efficiency

    def draw_heatmap(self):
        key_frequency_dict = {}
        for key, value in self.key_number_dict.items():
            key_frequency_dict[key] = value / self.key_number_total

        draw_heatmap_by_key_number_dict(key_frequency_dict)

    def show_parameters(self):
        print(f'''
1. 均衡性——按键频率方差的倒数（越高越好）：{self.balance}
2. 输入效率——和拼音的对应程度（越高越好）：{self.correspondence}
3. 输入效率——总按键频率（越低越好）：{self.key_character_ratio}
4. 输入效率——键位之间平均距离（越低越好）：{self.average_distance_between_keys}
5. 综合输入效率（越高越好）：{self.efficiency}
6. 编码方法综合评价（越高越好）：{self.score}
''')
