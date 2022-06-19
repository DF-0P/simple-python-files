import random as r
r_n = r.randint(0, 30)
print(r_n)
while True:
    g_n = int(input("enter a number: "))
    if r_n > g_n:
        print("g_n is less than r_n")
    elif r_n < g_n:
        print("g_n is greater than r_n")
    else:
        print("you got it right!")
        break