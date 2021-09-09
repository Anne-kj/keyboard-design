from lib.constants import alphabet
from lib.spelling_type.heatmap import draw_heatmap_by_key_number_dict
from lib.spelling_type.parameters.balance import cal_balance
from lib.spelling_type.parameters.efficiency.cal_efficiency import efficiency
from lib.spelling_type.parameters.efficiency.ck_ratio import cal_character_key_ratio
from lib.spelling_type.parameters.efficiency.correspondence import cal_correspondence
from lib.text_info import text_info


class SpellingType:
    # spelling_type 为 old 表示全拼，为 new 表示新的编码方法
    spelling_type = ''
    # 键盘与字母的对应关系
    alphabet_key_dict = {}
    # 按键的频次
    key_number_dict = {i: 0 for i in alphabet}
    # 各类指标
    balance = None
    correspondence = None
    character_key_ratio = None
    distance_between_keys = None

    # spelling_type 为 old 表示全拼，为 new 表示新的编码方法
    def __init__(self, alphabet_key_dict: dict, spelling_type: str):
        if spelling_type not in ('old', 'new'):
            raise ValueError
        self.spelling_type = spelling_type

        self.alphabet_key_dict = alphabet_key_dict.copy()
        if spelling_type == 'old':
            self.key_number_dict = text_info.alpha_number_dict.copy()
        else:
            for key, value in alphabet_key_dict:
                self.key_number_dict[value] += text_info.initial_final_number_dict[key]

    def calculate_parameters(self):
        self.balance = cal_balance(self.key_number_dict)
        self.correspondence = cal_correspondence(self.alphabet_key_dict)
        self.character_key_ratio = cal_character_key_ratio(sum(self.key_number_dict.values()))
        self.distance_between_keys = distance()
        # 加权求和

    def draw_heatmap(self):
        draw_heatmap_by_key_number_dict(self.key_number_dict)

    def show_parameters(self):
        pass
