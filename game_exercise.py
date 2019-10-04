import random

def play(l1, l2):
    r = random.randint(l1, l2)
    count = 1
    while True:
        play = int(input("Enter your number :\n"))
        if play > r:
            print(f"Enter a number less than {play}\n")
            count = count + 1
        elif play < r:
            print(f"Enter a number greater than {play}\n")
            count = count + 1
        elif l1 > play or l2 < play:
            print("Enter a number within range:\n")
        else:
            print(count)
            return count

if __name__ == "__main__":

    l1 = int(input("Enter the lower range :\n"))
    l2 = int(input("Enter the upper range :\n"))
    name1 = input("Enter the name of the first contestent:\n")
    c1 = play(l1, l2)
    name2 = input("Enter the name of the second contestent:\n")
    c2 = play(l1, l2)

    if c1 > c2:
        print(f"Player {name2} wins :\n")
    elif c1 < c2:
        print(f"Player {name1} wins :\n")
    else:
        print("Match is draw :\n")

