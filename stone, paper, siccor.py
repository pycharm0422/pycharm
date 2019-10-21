import random

l = int(input("enter 1: to play against computer 2: to play against human \n"))
if l == 1:
    n = int(input("Enter the no. of point you want to play till "))
    p1 = 0
    p2 = 0
    while n >= 0:

        r = random.randint(1,3)
        # if r == 1:
        #     c = "stone"
        # if r == 2:
        #     c = "paper"
        # if r ==3:
        #     c = "scissor"

        i = int(input("1:stone\n2:paper\n3:scissor\n"))

        if r == 1 and i == 1:
            print("draw")
        if r == 1 and i == 2:
            p1 = p1+1
            print("computer got 1 point")
        if r == 1 and i == 3:
            p2 = p2+1
            print("Player2 got 1 point")
        if r == 2 and i == 1:
            p1 = p1+1
            print("computer got 1 point")
        if r == 2 and i == 2:
            print("draw")
        if r == 2 and i == 3:
            p2 = p2+1
            print("Player2 got 1 point")
        if r == 3 and i == 1:
            p1 = p1+1
            print("computer got 1 point")
        if r == 3 and i == 2:
            p2 = p2+1
            print("Player2 got 1 point")
        if r == 3 and i == 3:
            print("draw")

        if n == 0:
            print("computer point is ", p1)
            print("player 2 point is ", p2)
            if p1 > p2:
                print("player one wins ")
            elif p1 < p2:
                print("player two wins ")
            else:
                print("match is draw ")
        n -= 1
elif l == 2:
        n = int(input("Enter the no. of point you want to play till "))
        p1 = 0
        p2 = 0
        while n >= 0:
            print("player 1 turn :")
            r = int(input("1:stone\n2:paper\n3:scissor\n"))
            # if r == 1:
            #     c = "stone"
            # if r == 2:
            #     c = "paper"
            # if r ==3:
            #     c = "scissor"
            print("player 2 turn :")
            i = int(input("1:stone\n2:paper\n3:scissor\n"))

            if r == 1 and i == 1:
                print("draw")
            if r == 1 and i == 2:
                p2 = p2 + 1
                print("player2 got 1 point")
            if r == 1 and i == 3:
                p1 = p1 + 1
                print("Player1 got 1 point")
            if r == 2 and i == 1:
                p2 = p2 + 1
                print("player2 got 1 point")
            if r == 2 and i == 2:
                print("draw")
            if r == 2 and i == 3:
                p2 = p2 + 1
                print("Player2 got 1 point")
            if r == 3 and i == 1:
                p1 = p1 + 1
                print("player1 got 1 point")
            if r == 3 and i == 2:
                p1 = p1 + 1
                print("Player1 got 1 point")
            if r == 3 and i == 3:
                print("draw")

            if n == 0:
                print("player 1 point is ", p1)
                print("player 2 point is ", p2)
                if p1 > p2:
                    print("player one wins ")
                elif p1 < p2:
                    print("player two wins ")
                else:
                    print("match is draw ")
            n -= 1
else:
    print("enter a valid number ")