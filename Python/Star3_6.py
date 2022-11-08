def print_star3_6():
    n = int(input("Enter your number :"))
    for i in range(n):
        for j in range(n - i - 1):
            print('A', end='')
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i:
                print('+', end='')
            else:
                print('E', end='')
        for j in range(n-1, i, -1):
            print("B", end="")
        print()

    for i in range(n - 1):
        for j in range(i + 1):
            print('C', end='')
        for j in range(2 * (n - i - 1) - 1):
            if j == 0 or j == 2 * (n - i - 1) - 2:
                print('+', end='')
            else:
                print('E', end='')
        for k in range(0, i + 1):
            print("D", end="")
        print()



if __name__ == '__main__':
    print_star3_6()