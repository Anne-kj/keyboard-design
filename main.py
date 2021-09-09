from lib.spelling_type import SpellingType
from lib.spelling_type.parameters.balance import cal_balance
from lib.spelling_type.parameters.efficiency.cal_efficiency import efficiency
from lib.spelling_type import count_text, count_character_number, count_press_number

if __name__ == '__main__':
    old_spelling_type = SpellingType()

    count = count_text(filename)
    print(count)
    print(cal_balance(count))
    print(efficiency(alphabet_dict_old))
    print(count_character_number(filename))
    print(count_press_number(filename, "old"))