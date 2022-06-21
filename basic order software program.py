'''
basic order system made by kurai umi 

'''
import time
menu = {"chicken burger": 20, "smoothy": 10, "meat pie": 15}
resources = {"1" : 30, "2": 20 , "3": 23}
menu_list = {"1": "chicken burger", "2": "smoothy", "3": "meat pie"}
pr = []
sr = []
fr = []
while True:
    print(""""
     welcome to cloud chicken service 
     what would you like to eat:
     1. chicken burger
     2. smoothy
     3. meat pie""")
    def kkkk():
        a = input("what's your order: ")
        def pieces():
            b = int(input("how many pieces?: "))
            total_price = 0
            if b > resources.get(a):
                print(f"not enough {ab}")
            else:
                print(total_price)
                pr.append(menu.get(ab) * b)
                sr.append(b)
                fr.append(ab)
                resources[a] = (resources.get(a)- b)
                print("do you want to add an order?(y/n):")
                answer = input()
                if answer == "y":
                    kkkk()
                else:
                    gr = 0
                    sum = 0
                    for i in pr:
                        sum += i
                    for i in sr:
                        gr += i
                    print(f"your order for {fr}, {gr} quantity price is {sum}")
        if (a == "chicken burger") or (a == "1"):
            if a == "1":
                ab = menu_list.get(a)
            pieces()
        elif (a == "smoothy") or (a == "2"):
            if a == "2":
                ab = menu_list.get(a)
            pieces()
        elif (a == "meat pie") or (a == "3"):
            if a == "3":
                ab = menu_list.get(a)
            pieces()
        elif (a == "r"):
            print(menu)
            print(resources)
    kkkk()
    print("""Thank you for Shopping at Cloud Chicken Service.
    your satisfaction is our concern.
    See you Soon.""")
    print("program finished")
    pr = []
    sr = []
    fr = []
    time.sleep(3)