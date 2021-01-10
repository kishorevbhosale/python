"""
Find out the closest palindrom number of a given number
ex.   1) Input = 399 output = 404
      2) Input = 396 output = 393

"""

num = int(input())


def reverse_number(num):
    number_str = str(num)
    reverse_str = number_str[::-1]
    r_number = int(reverse_str)
    return r_number


def search_palidrom(num):
    lnumber = left_search(num)
    rnumber = right_search(num)
    ldiff = num - lnumber
    rdiff = rnumber - num
    if ldiff < rdiff:
        print(lnumber)
    else:
        print(rnumber)


def left_search(num):
    start = num
    stop = 0
    while (start > stop):
        rev = reverse_number(start)
        if start == rev:
            return start
        start = start - 1


def right_search(num):
    start = num
    stop = num * 2
    while (start < stop):
        rev = reverse_number(start)
        if start == rev:
            return start
        start += 1


search_palidrom(num)
