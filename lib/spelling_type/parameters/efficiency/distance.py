from lib.constants import alphabet


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
        for dis, pairs in self.distance_pairs_dict:
            for pair in pairs:
                a, b = list(pair)
                self.distance[a][b] = dis
                self.distance[b][a] = dis


key_distance = KeyDistance()


def cal_average_distance_between_keys():
    pass