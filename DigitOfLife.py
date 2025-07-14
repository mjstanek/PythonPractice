#!/usr/bin/env python3

def birthday_checker(birthday):
    try:
        bday_list = list(birthday)
        birthday = int(birthday)
        if len(bday_list) > 8 or len(bday_list) < 6:
            raise ValueError
        else:
            calculate_digit(bday_list)
    except:
        print('Please enter a valid birthday using a total of eight digits.')


def calculate_digit(birthday):
    valid = False
    while not valid:
        bday_list = [int(i) for i in birthday]
        bday_sum = sum(bday_list)
        if len(str(bday_sum)) != 1:
            birthday = str(bday_sum)
        else:
            valid = True
    print(f'Your "digit of life" is {bday_sum}!')

if __name__ == "__main__":
    print('Let\'s calculate your "digit of life"!')
    print('A person\'s digit of life is the single digit that comes from adding the day, month, and year they were born.')
    print('Please note that the order does not matter, but we do need a four-digit year, two-digit month, and two-digit day.')
    birthday = input('Please enter the day you were born: ')
    birthday_checker(birthday)
