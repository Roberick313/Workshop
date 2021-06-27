### Prime Number

while True:

    a = int(input("Enter your Number: "))

    if a <= 1:
        print('the number that just entered is 1 or below 1...')
        continue

    elif a > 1:

        for i in range(2, a):
            if (a % i) == 0:
                print("the number isn't prime")
                break

        else:
            print(f"{a} is a prime number.")
            break
