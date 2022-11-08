def print_star3_5():
    n = int(input("Enter your number :"))
    k = 1
    for i in range((n + 1) // 2):
        for blank in range(1, ((n + 1) // 2) - i):
            print(' ', end='')
        print('*' * k, end='')
        k += 2
        print()
    if (n % 2 == 0):
        print('*' * (k - 2), end='')
        print()
        k = n - 1
    else:
        k = n
    for i in range(1, ((n) // 2 + 1)):
        for blank in range(i):
            print(' ', end='')
        k -= 2
        print('*' * k, end='')
        print()


if __name__ == '__main__':
    print_star3_5()