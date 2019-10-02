
def turn_100(m):
    if len(m)<=3:
        at_100 = 100 - int(m)
        if at_100 > 100:
            print("You are not born yet")

        elif at_100 < 0:
            print("You already lived more than a century")
        else:
            if int(m) > 125:
                print("You seems to be the oldest person alive :")
            print(f"You will turn 100 after {at_100} years old")

    elif len(m)==4:
        at_100 = (int(m) + 100) - 2019
        if at_100 > 100:
            print("You are not born yet :")
        elif at_100<0:
            print("You already lived more than a century:")
        else:
            print(f"You will turn 100 after {at_100} years old")


    else:
        print("You entered wrong input")

def future_age(m):
    if len(m) == 4:
        b = int(input("Enter the year when you want to find your age:"))
        print(f"You will be {b - int(m)} years old")


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
    result1 = turn_100(m)
    result2 = future_age(m)