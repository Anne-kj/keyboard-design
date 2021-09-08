from lib.cal_balance import balance
from lib.cal_efficiency import efficiency
from lib.constants import alphabet_dict_old
from lib.count_text_alpha import count_text, count_character_number, count_press_number

if __name__ == '__main__':
    filename = 'data/text1.txt'
    count = count_text(filename)
    print(count)
    print(balance(count))
    print(efficiency(alphabet_dict_old))
    print(count_character_number(filename))
    print(count_press_number(filename, "old"))