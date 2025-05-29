#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(s):
    return s[:5]

def last_seven(s):
    return s[-7:]

def middle_number(num):
    if isinstance(num, int):
        num_str = str(num)
        length = len(num_str)
        middle_start = (length - 2) // 2
        return num_str[middle_start:middle_start + 2]
    else:
        num_str = str(num)
        if '.' in num_str:
            parts = num_str.split('.')
            decimal_part = parts[1]
            return '.' + decimal_part[0]  # Return '.' followed by the first digit
        else:
            return ''

def first_three_last_three(s1, s2):
    first_part = s1[:3]
    last_part = s2[-3:] if len(s2) >= 3 else s2
    return first_part + last_part

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
