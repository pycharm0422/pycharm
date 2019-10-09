
vowels = "AEIOU"
v = 0
nv = 0

a = input("Enter any word (CAPS ON)")
l = list(a)
c = len(l)

for j in range(len(a)):
    for i in range(len(a), 0, -1):
        # print(a[j:i])
        if a[j:i] == "":
            pass
        else:
            if a[j] in vowels:
                v+= 1
            else:
                nv+= 1
if v > nv:
    print("Faraz wins and point is {}".format(v))
else:
    print("Himanshu wins and point is {}".format(nv))


