from lib.constants import create_alpha_key_dict_old
from lib.spelling_type import SpellingType

if __name__ == "__main__":
    old_spelling_type = SpellingType(create_alpha_key_dict_old(), "old")
    old_spelling_type.draw_heatmap()
    old_spelling_type.cal_parameters()
    old_spelling_type.show_parameters()
    # count = count_text(filename)
    # print(count)
    # print(cal_balance(count))
    # print(efficiency(alpha_dict_old))
    # print(count_character_number(filename))
    # print(count_press_number(filename, "old"))
    # 将拼音切分成声母和韵母




