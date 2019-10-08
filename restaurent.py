class Food:

    def __init__(self):
        self.name = "Faraz Khan"
        self.orders = {}

    def order(self):

        lis1 = ["Veg", "Non-Veg","drinks"]
        type = ["Indian", "French", "Portugese"]
        vegi = ["rice", "roti", "paneer"]
        vegf = ["lardon", "gourera", "Jambon persillé"]
        vegg = ["Kartoffelkloesse", "Sauerkraut", "german paneer"]
        non_vegi = ["chiken tikka", "mutton", "kabab"]
        non_vegf = ["Coq au vin", "Bœuf bourguignon", "Jambon persillé"]
        non_vegg = ["Sauerbraten", "Bratwurst", "Schweinshaxe"]
        drinks = ["Mojiata", "Martini", "Gin Rickey"]


            # while True:

        for i in range(len(lis1)):
            print(f"{i + 1}: {lis1[i]}")
        a = int(input("Do you want veg or non veg :"))
        if a == 1:
            def my_orders_veg():
                for j in range(len(type)):
                    print(f"{j + 1} {type[j]}")
                b = int(input("Do you want indian, french or german food :"))
                if b == 1:
                    for j in range(len(vegi)):
                        print(f"{j + 1} {vegi[j]}")
                    c = input('What do you want to order :')
                    k = c.split(",")
                    for e in k:
                        d = int(input("how much do you want :"))
                        self.orders.update({d: vegi[int(e) - 1]})
                    print(self.orders)
                elif b == 2:
                    for j in range(len(vegf)):
                        print(f"{j + 1} {vegf[j]}")
                    c = input('What do you want to order :')
                    k = c.split(",")
                    for e in k:
                        d = int(input("how much do you want :"))
                        self.orders.update({d: vegf[int(e) - 1]})
                    print(self.orders)
                elif b == 3:
                    for j in range(len(vegg)):
                        print(f"{j + 1} {vegg[j]}")
                    c = input('What do you want to order :')
                    k = c.split(",")
                    for e in k:
                        d = int(input("how much do you want :"))
                        self.orders.update({d: vegg[int(e)-1]})
                    print(self.orders)

                l = input(" enter s to switch to non-veg \n and n to continue ordering from veg \n ")
                if l == "s":
                    my_orders()
                else:
                    my_orders_veg()

            my_orders_veg()
        elif a == 2:
            def my_orders():
                for j in range(len(type)):
                    print(f"{j + 1} {type[j]}")
                b = int(input("Do you want indian, french or german food :"))
                if b == 1:
                    for j in range(len(non_vegi)):
                        print(f"{j + 1} {non_vegi[j]}")
                    c = input('What do you want to order :')
                    k = c.split(",")
                    for e in k:
                        d = int(input("how much do you want :"))
                        self.orders.update({d: non_vegi[int(e) - 1]})
                    print(self.orders)
                elif b == 2:
                    for j in range(len(non_vegf)):
                        print(f"{j + 1} {non_vegf[j]}")
                    c = input('What do you want to order :')
                    k = c.split(",")
                    for e in k:
                        d = int(input("how much do you want :"))
                        self.orders.update({d: non_vegf[int(e) - 1]})
                    print(self.orders)
                elif b == 3:
                    for j in range(len(non_vegg)):
                        print(f"{j + 1} {non_vegg[j]}")
                    c = input('What do you want to order :')
                    k = c.split(",")
                    for e in k:
                        d = int(input("how much do you want :"))
                        self.orders.update({d: non_vegg[int(e) - 1]})
                    print(self.orders)

                l = input("Enter s to switch to veg \nor enter d to jump to drinks  \nand n to continue ordering from non veg \n ")
                if l == "s":
                    my_orders_veg()
                elif l == "d":
                    drinkss()
                else:
                    my_orders()

            my_orders()
        elif a == 3:
            def drinkss():
                for i in range(len(drinks)):
                    print(f"{i+1} {drinks[i-1]}")
                c = input("What drink you want to have:")
                k = c.split(",")
                for e in k:
                    d = int(input("How many drinks you want:"))
                    self.orders.update({d : drinks[int(e)-1]})
                l = input(" enter s to switch to veg \n and n to continue ordering from non veg \n ")
                if l == "s":
                    my_orders_veg()
                else:
                    drinkss()
            drinkss()

    # if food not in self.list:
    #     print("sorry the food is not available please try another thing:")
    # else:
    #     self.orders.update({quantity : food})
    #     print("your order is done")
    def payments(self):
        pass

if __name__ == "__main__":

    while True:
        f = Food()
        print("1: to order food")
        print("2: to do payments")
        i = int(input())
        if i == 1:

            f.order()

        elif i == 2:
            print("Your payment is :")

        q = input("'q' to quit or any key to continue")
        if q == "q":
            quit()
        else:
            break