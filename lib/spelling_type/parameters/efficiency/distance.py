from lib.constants import alphabet


class KeyDistance:
    distance = {alpha: {alpha: 0 for alpha in alphabet} for alpha in alphabet}

    distance_pairs_dict = {1: ["qa", "az", "ws", "sx", "ed", "dc", "rf", "fv",
                               "ol", "ik", "uj", "jm",
                               "tg", "gb", "tr", "gf", "bv", "yh", "hn", "yu", "hj", "nm"],
                           2: ["qz", "wx", "ec", "rv", "tb", "yn", "um",
                               "tf", "rg", "gv", "fb", "yj", "jn", "uh", "hm"],
                           3: ["rb", "tv", "ym", "un"]}

    def __init__(self):
        for dis, pairs in self.distance_pairs_dict:
            for pair in pairs:
                a, b = list(pair)
                self.distance[a][b] = dis
                self.distance[b][a] = dis


key_distance = KeyDistance()
