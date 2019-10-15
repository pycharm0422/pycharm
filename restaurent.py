class Food:

    def __init__(self):
        self.name = "Faraz Khan"
        self.orders = []

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
            l = int(input("Do you want \n1:to continue ordering\n2:Remove order from list\n3:Done Ordering(Payments)\n"))
            try:
                if l == 2:
                    self.removes()
                if l == 3:
                    self.payments()
                if l == 1:
                    n = int(input("Do you want \n1:Drinks\n2:Veg\n3:Non Veg\n4:Menu Card \n"))
                    self.order(n)
            except:
                print("Invalid Input")
                my_orders_veg()

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

            l = int(input("Do you want \n1:to continue ordering\n2:Remove order from list\n3:Done Ordering(Payments)\n"))
            try:
                if l == 2:
                    self.removes()
                if l == 3:
                    self.payments()
                if l == 1:
                    n = int(input("Do you want \n1:Drinks\n2:Veg\n3:Non Veg\n4:Menu Card \n"))
                    self.order(n)
            except:
                print("Invalid input")
                my_orders()

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
            l = int(input("Do you want \n1:to continue ordering\n2:Remove order from list\n3:Done Ordering(Payments)\n"))
            try:
                if l == 2:
                    self.removes()
                if l == 3:
                    self.payments()
                if l == 1:
                    n = int(input("Do you want \n1:Drinks\n2:Veg\n3:Non Veg\n4:Menu Card \n"))
                    self.order(n)
            except:
                print("Invalid input")
                drinkss()
        try:
            if p == 1:
                drinkss()
            if p == 2:
                my_orders_veg()
            if p == 3:
                my_orders()
            if p ==4:
                self.menu()
        except:
            print("Invalid Input ")

  
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
        print(f"You have to pay ${sas} amount.\nThank you for coming to our restaurent\n___PLEASE VISIT AGIAN__!")

    def menu(self):
        print("____Vegetarian _____:")
        print("Indian")
        print(["rice", "roti", "paneer"])
        print("\nFrench")
        print(["lardon", "gourera", "Jambon persillé"])
        print("\nGerman")
        print(["Kartoffelkloesse", "Sauerkraut", "german paneer"])
        print("\n____Non Vegetarian____:")
        print("\nIndian")
        print(["chiken tikka", "mutton", "kabab"])
        print("\nFrench")
        print(["Coq au vin", "Bœuf bourguignon", "Jambon persillé"])
        print("\nGerman")
        print(["Sauerbraten", "Bratwurst", "Schweinshaxe"])
        print("\n___Drinks___:")
        print(["Mojiata", "Martini", "Gin Rickey"])
        l = int(input("Do you want \n1:Drinks\n2:Veg\n3:Non Veg\n"))
        self.order(l)

    def removes(self):
        print(self.orders)
        l = int(input("What element you want to remove:"))
        self.orders.pop(l)
        print(self.orders)
        n = int(input("Enter \n1:To go to ordering\n2:To do payments "))
        try:
            if n == 1:
                l = int(input("Do you want \n1:Drinks\n2:Veg\n3:Non Veg\n"))
                self.order(l)
            if n ==2:
                self.payments()
        except:
            print("Invalid input")
            self.removes()

if __name__ == "__main__":

    while True:
        f = Food()
        print("1: to order food ")
        print("2: to see menu\n")
        # print("3: to see orders\n")
        i = int(input())
        if i == 1:
            l = int(input("Do you want \n1:Drinks\n2:Veg\n3:Non Veg\n"))
            f.order(l)
        if i == 2:
            f.menu()
        if i == 3:
            f.removes()

        q = input("'q' to quit or any key to ordering ")
        if q == "q":
            quit()
        else:
            continue
        print("faraz")
