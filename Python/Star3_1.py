def print_star3_1():
    n = int(input("Enter your number :"))
    for i in range(n+1):
        for j in range(i):
            print("*" , end="")
        print('')



if __name__ == '__main__':
    print_star3_1()