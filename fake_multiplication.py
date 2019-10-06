import random
def rohan_multiplication(n, x):

    r = [n*i for i in range(1, 11)]
    r[x] = r[x]+2
    return r

def is_correct(n):
    return [n*i for i in range(1, 11)]

if __name__ == "__main__":
    n = int(input("Enter the number you want to find the table of :"))
    x = random.randint(1, 9)
    r = rohan_multiplication(n, x)
    print(r)
    i = is_correct(n)
    print(i)
    for k in (r,i):
        if r!=i:
            print(f"Table is wrong at position {x+1}")
            break
