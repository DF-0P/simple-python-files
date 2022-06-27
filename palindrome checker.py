'''write a progam to determine if a wod is a palindrome(a word thtas still the same even if spelled backwards)'''
'''eg MADAM'''

#code below to get the text of the word
text = input("what is the word: ")
#two lines below to assign the values to new list in but normal arrangement and reversed arrangemnet
#line below is not v=even needed again sef
c = text[:] 
d = c[::-1]

print(c)
print(d)
#if statement to compare the list slice of the two list 
# you can use c[:] == d[:] in the if statement condition or go with the one below
if text[:] == text[::-1]:
    print("Palindrome")
else:
    print("it is not")