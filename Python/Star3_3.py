def print_star3_3():
    n = int(input("Enter your number :"))
    i = 1
    while i <= n:
        j = n
        while j > i:
            # display space
            print(' ', end=' ')
            j -= 1
        print('*', end=' ')
        k = 1
        while k < 2 * (i - 1):
            print(' ', end=' ')
            k += 1
        if i == 1:
            print()
        else:
            print('*')
        i += 1


if __name__ == '__main__':
    print_star3_3()