from spelling_type import SpellingType
from spelling_type.parameters.balance.cal_balance import balance
from spelling_type.parameters.efficiency.cal_efficiency import efficiency
from spelling_type.count_text_alpha import count_text, count_character_number, count_press_number

if __name__ == '__main__':
    old_spelling_type = SpellingType()

    count = count_text(filename)
    print(count)
    print(balance(count))
    print(efficiency(alphabet_dict_old))
    print(count_character_number(filename))
    print(count_press_number(filename, "old"))