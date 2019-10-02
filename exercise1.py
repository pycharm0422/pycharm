
def turn_100(m):
    if len(m)<=3:
        at_100 = 100 - int(m)

        if at_100 > 100:
            print("You already lived more than a century")
        elif at_100 < 0:
            print("You are not born yet")
        else:
            if int(m) > 125:
                print("You seems to be the oldest person alive :")
            print("You will turn 100 after ")
            return at_100

    elif len(m)==4:
        at_100 = (int(m) + 100) - 2019
        print("You will turn 100 after")
        return at_100

    else:
        print("You entered wrong input")

def future_age(m):
    f = int(input("Enter the year you want to find your age:"))


if __name__ == "__main__":
    print("1: To enter age:")
    print("2: To enter year of birth:")
    n = input()
    if n == "1":
        m = input("Enter your age:")
    elif n == "2":
        m = input("Enter you birth year:")
    else:
        print("Enter 1 or 2 only ")
    result = turn_100(m)
    print(result)
    print()

