def print_star3_2():
    n = int(input("Enter your number :"))
    for i in range(n+1) :
        num = 1
        for j in range(n,0,-1):
            if j > i :
                print(" ", end=" ")
            else:
                print("*",end=" ")
                num += 1
        print("")



if __name__ == '__main__':
    print_star3_2()