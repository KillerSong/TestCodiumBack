def print_leap_year(num):
    if num % 400 == 0 :
        print(str(num) +" -> "+"true")
    elif num % 400 != 0 and num % 100 != 0 and num % 4 == 0  :
        print(str(num) +" -> "+"true")
    else :
        print(str(num) +" -> "+ "false")


if __name__ == '__main__':
    print_leap_year()