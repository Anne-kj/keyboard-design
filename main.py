from lib.cal_balance import balance
from lib.count_text_alpha import count_text

if __name__ == '__main__':
    count = count_text('data/text1.txt')
    print(count)
    print(balance(count))