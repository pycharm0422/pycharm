class Food:

    def __init__(self):
        self.name = "Faraz Khan"
        self.orders = []
        self.payments()

    def order(self, p):

        lis1 = ["Veg", "Non-Veg", "drinks"]
        type = ["Indian", "French", "Portugese"]
        vegi = ["rice", "roti", "paneer"]
        vegf = ["lardon", "gourera", "Jambon persillé"]
        vegg = ["Kartoffelkloesse", "Sauerkraut", "german paneer"]
        non_vegi = ["chiken tikka", "mutton", "kabab"]
        non_vegf = ["Coq au vin", "Bœuf bourguignon", "Jambon persillé"]
        non_vegg = ["Sauerbraten", "Bratwurst", "Schweinshaxe"]
        drinks = ["Mojiata", "Martini", "Gin Rickey"]

        # while True:
        # for i in range(len(lis1)):
        #     print(f"{i + 1}: {lis1[i]}")
        # a = int(input("Do you want veg or non veg :"))
        # if a == 1:
        def my_orders_veg():
            for j in range(len(type)):
                print(f"{j + 1} {type[j]}")
            b = int(input("Do you want indian, french or german food :\n"))
            if b == 1:
                for j in range(len(vegi)):
                    print(f"{j + 1} {vegi[j]}")
                c = input('What do you want to order :\n')
                k = c.split(",")
                for e in k:
                    d = int(input("how much do you want :\n"))
                    self.orders.append({d: vegi[int(e) - 1]})
                print(self.orders)
                print("\nThank you for ordering our food\n")
            elif b == 2:
                for j in range(len(vegf)):
                    print(f"{j + 1} {vegf[j]}")
                c = input('What do you want to order :\n')
                k = c.split(",")
                for e in k:
                    d = int(input("how much do you want :"))
                    self.orders.append({d: vegf[int(e) - 1]})
                print(self.orders)
                print("\nThank you for ordering our food\n")
            elif b == 3:
                for j in range(len(vegg)):
                    print(f"{j + 1} {vegg[j]}")
                c = input('What do you want to order :\n')
                k = c.split(",")
                for e in k:
                    d = int(input("how much do you want :"))
                    self.orders.append({d: vegg[int(e) - 1]})
                print(self.orders)
                print("\nThank you for ordering our food\n")
            l = int(input("Do you want \n1:Drinks\n2:Veg\n3:Non Veg\n9:Payments\n"))
            if l == 2:
                my_orders_veg()
            if l == 3:
                my_orders()
            if l == 1:
                drinkss()
            if l == 9:
                self.payments()

        def my_orders():
            for j in range(len(type)):
                print(f"{j + 1} {type[j]}")
            b = int(input("Do you want indian, french or german food :\n"))
            if b == 1:
                for j in range(len(non_vegi)):
                    print(f"{j + 1} {non_vegi[j]}")
                c = input('What do you want to order :\n')
                k = c.split(",")
                for e in k:
                    d = int(input("how much do you want :\n"))
                    self.orders.append({d: non_vegi[int(e) - 1]})
                print(self.orders)
                print("\nThank you for ordering our food\n")
            elif b == 2:
                for j in range(len(non_vegf)):
                    print(f"{j + 1} {non_vegf[j]}")
                c = input('What do you want to order :')
                k = c.split(",")
                for e in k:
                    d = int(input("how much do you want :\n"))
                    self.orders.append({d: non_vegf[int(e) - 1]})
                print(self.orders)
                print("\nThank you for ordering our food\n")
            elif b == 3:
                for j in range(len(non_vegg)):
                    print(f"{j + 1} {non_vegg[j]}")
                c = input('What do you want to order :\n')
                k = c.split(",")
                for e in k:
                    d = int(input("how much do you want :\n"))
                    self.orders.append({d: non_vegg[int(e) - 1]})
                print(self.orders)
                print("\nThank you for ordering our food\n")

            l = int(input("Do you want \n1:Drinks\n2:Veg\n3:Non Veg\n9:Payments\n"))
            if l == 2:
                my_orders_veg()
            if l == 3:
                my_orders()
            if l == 1:
                drinkss()
            if l == 9:
                self.payments()

        def drinkss():
            for i in range(len(drinks)):
                print(f"{i + 1} {drinks[i - 1]}")
            c = input("What drink you want to have:\n")
            k = c.split(",")
            for e in k:
                d = int(input("How many drinks you want:\n"))
                self.orders.append({d: drinks[int(e) - 1]})
            print(self.orders)
            print("\nThank you for ordering our Drinks\n")
            # l = input("Enter s to switch to veg \nEnter nv to jump to non veg \nand n to continue ordering from drinks \nIf done ordering press p to go to payments ")
            l = int(input("Do you want \n1:Drinks\n2:Veg\n3:Non Veg\n9:Payments\n"))
            if l == 2:
                my_orders_veg()
            if l == 3:
                my_orders()
            if l == 1:
                drinkss()
            if l == 9:
                self.payments()

        if p == 1:
            drinkss()
        if p == 2:
            my_orders_veg()
        if p == 3:
            my_orders()

    # if food not in self.list:
    #     print("sorry the food is not available please try another thing:")
    # else:
    #     self.orders.update({quantity : food})
    #     print("your order is done")
    def payments(self):
        money_list = [
            "rice=5", "roti=10", "paneer=15",
            "lardon=23", "gourera=21", "Jambon persillé=56",
            "Kartoffelkloesse=43", "Sauerkraut=11", "german paneer=24",
            "chiken tikka=543", "mutton=54", "kabab=33",
            "Coq au vin=12", "Bœuf bourguignon=123", "Jambon persillé=45",
            "Sauerbraten=32", "Bratwurst=65", "Schweinshaxe=87",
            "Mojiata=43", "Martini=55", "Gin Rickey=87"]
        sas = 0
        # for i in arr:
        # print(i)
        # for key, value in i:
        #     print(value, key)
        # print(k)
        for l in self.orders:
            for j, k in l.items():
                # print(k)
                for m in money_list:
                    n = m.split("=")
                    if n[0] == k:
                        sas = sas + j * int(n[1])
            print(f"You have to pay ${sas} amount.\nThankyou for coming to our restaurent\n___PLEASE VISIT AGIAN__!")



if __name__ == "__main__":

    while True:

        f = Food()
        print("1: to order food\n")
        print("2: to see menu\n")
        i = int(input())
        if i == 1:
            l = int(input("Do you want \n1:Drinks\n2:Veg\n3:Non Veg\n"))
            f.order(l)
        if i == 2:
            f.payments()

        q = input("'q' to quit or any key to continue")
        if q == "q":
            quit()
        else:
            continue