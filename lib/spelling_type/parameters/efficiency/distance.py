from lib.constants import alphabet
from lib.text_info import text_info


class KeyDistance:
    distance = {alpha: {alpha: 0 for alpha in alphabet} for alpha in alphabet}

    distance_pairs_dict = {1: ["qa", "az", "ws", "sx", "ed", "dc", "rf", "fv",
                               "ol", "ik", "uj", "jm",
                               "rt", "rf", "tf", "tg", "fg", "fv", "gv", "gb", "vb",
                               "yu", "yh", "uh", "uj", "hj", "hn", "jn", "jm", "nm"],
                           2: ["qz", "wx", "ec", "rv", "tb", "yn", "um",
                               "rg", "rv", "tv", "tb", "fb", "yn", "um", "yj", "un", "hm"],
                           3: ["rb", "ym"]}

    def __init__(self):
        for dis, pairs in self.distance_pairs_dict.items():
            for pair in pairs:
                a, b = list(pair)
                self.distance[a][b] = dis
                self.distance[b][a] = dis


key_distance = KeyDistance()


def cal_average_distance_between_keys(alpha_key_dict: dict, key_number_total: int, spelling_type: str) -> float:
    key_distance_total = 0
    if spelling_type == "old":
        alpha_number_2d_dict = text_info.alpha_number_2d_dict
    else:
        alpha_number_2d_dict = text_info.initial_final_number_2d_dict
    for i in alpha_number_2d_dict.keys():
        for j in alpha_number_2d_dict[i].keys():
            key_distance_total += key_distance.distance[alpha_key_dict[i]][alpha_key_dict[j]] * alpha_number_2d_dict[i][j]
    return key_distance_total / key_number_total
