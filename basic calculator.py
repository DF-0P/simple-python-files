while 1 == 1:
    num1 = int(input("what is your first digit; "))
    num2 = int(input("what is your second digit; "))
    op = input("what operation do you want to do: ")


    if (op == "+"):
        print("the sum of the digits are: ", (num1 + num2))
    elif (op == "-"):
        print("the differnce of the digits are: ", (num1 - num2))
    elif (op == "*") or (op == "x"):
        print("the product of the digits are: ", (num1 * num2))
    elif (op =="/"):
        print("the division of the digits are: ", (num1 / num2))
    print("porgram finished")
    print("                ")