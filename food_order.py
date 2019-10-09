#
# class Food:
#     def __init__(self):
#         self.name = "Faraz Restaurent"
#     def menu(self):
#         while True:
#             foods = []
#             print(" a: Veg\n b: Non veg\n c: Drinks\n d: Desert\n")
#             a = input("Enter the following character for order:")
#             if a == "a":
#                 print(" 1: chinese\n 2: Indian\n 3: French")
#                 i = int(input("Enter to order food:"))
#                 if i == 1:
#                     arr1 = ["noodles", "shushi", "chuchi"]
#                     for i in range(len(arr1)):
#                         print(f"{i}: {arr1[i]}")
#                     b = int(input("enter to order food "))
#                     if b == i:
#                         foods.append(arr1[i])
#                         print(foods)
#                         print("'p' to pass and 'q' to break")
#                         if input() == "p":
#                             continue
#                         elif input() == "q":
#                             break
#                 if i == 2:
#                     arr2 = ["roti", "rajma-chawal", "paneer"]
#                 if i == 3:
#                     arr3 = ["lardon", "gourera", "Jambon persillé"]
#
#     def orders(self):
#         pass
#     def payment(self):
#         pass
#
# if __name__ == "__main__":
#     s1 = Food()
#     s1.menu()

orders = [{'2': 'Schweinshaxe'}, {'3': 'paneer'}]


for i in orders:
    print(i[0])
    # k = i.split(":")
    # print(i.split(":")[1])


money_list = [
"rice = 5" , "roti = 10", "paneer = 15",
"lardon = 23", "gourera = 21", "Jambon persillé = 56",
"Kartoffelkloesse = 43", "Sauerkraut = 11", "german paneer = 24",
"chiken tikka = 543", "mutton = 54", "kabab = 33",
"Coq au vin = 12", "Bœuf bourguignon = 123", "Jambon persillé = 45",
"Sauerbraten = 32", "Bratwurst = 65", "Schweinshaxe = 87",
"Mojiata = 43", "Martini = 55", "Gin Rickey = 87"]
# sas = 0
# for j in orders:
#     k = j.split(":")
#     for i in money_list:
#         if k[1] == i.split("=")[0]:
#             sas = sas + int(k[0]) * i[1]
#             print(sas)