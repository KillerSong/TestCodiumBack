def print_sta3_4():
    n = int(input("Enter your number :"))
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()



if __name__ == '__main__':
    print_sta3_4()