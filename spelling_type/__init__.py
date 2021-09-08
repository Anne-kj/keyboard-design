from spelling_type.parameters.balance.cal_balance import balance
from spelling_type.parameters.efficiency.cal_efficiency import efficiency
from spelling_type.heatmap import draw_heatmap_by_alpha_count

class SpellingType:
    # 键盘与字母的对应关系
    alphabet_dict = {}
    # 测试文章
    # 各类指标
    balance = None
    efficiency = None

    def calculate_parameters(self):
        self.balance = balance()
        self.correspondence = efficiency()
        self.character_key_ratio =
        self.distance_between_keys = distance()
        # 加权求和

    def draw_heatmap(self):
        draw_heatmap_by_alpha_count()

    def show_parameters(self):
        pass
