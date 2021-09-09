from lib.constants import alphabet
from lib.spelling_type import SpellingType
from lib.spelling_type.random import generate_alpha_key_dict_randomly


def evaluate_old_quanpin():
    old_spelling_type = SpellingType({i: i for i in alphabet}, "old")
    old_spelling_type.draw_heatmap()
    old_spelling_type.cal_parameters()
    old_spelling_type.show_parameters()


def evaluate_specific_shuangpin(alpha_key_dict):
    old_spelling_type = SpellingType(alpha_key_dict, "specific")
    old_spelling_type.draw_heatmap()
    old_spelling_type.cal_parameters()
    old_spelling_type.show_parameters()


def evaluate_common_shuangpin():
    from lib.spelling_type.test import test_alpha_key_dicts
    for alpha_key_dict, spelling_name in test_alpha_key_dicts:
        spelling_type = SpellingType(alpha_key_dict, spelling_name)
        spelling_type.draw_heatmap(spelling_name + '.png')
        spelling_type.cal_parameters()
        spelling_type.show_parameters()


def find_new_pinyin():
    # 每计算 10 组输出到文件 1 次，减少 I/O
    BATCH = 10
    output_filename = 'output.txt'
    buffer = ''
    i = 0
    while True:
        i += 1
        alpha_key_dict = generate_alpha_key_dict_randomly()
        spelling_type = SpellingType(alpha_key_dict, str(alpha_key_dict))
        spelling_type.cal_parameters()
        buffer += '|'.join(spelling_type.get_parameters())
        buffer += '\n'
        if i % BATCH == 0:
            print(f'已完成{i}组')
            with open(output_filename, 'a+', encoding='utf-8') as f:
                f.write(buffer)
            buffer = ''


if __name__ == "__main__":
    find_new_pinyin()