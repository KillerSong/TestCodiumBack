def medium_prime_number():
    n = int(input("Enter your number :"))
    for i in range(n+1):
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                print(i)

if __name__ == '__main__':
    medium_prime_number()