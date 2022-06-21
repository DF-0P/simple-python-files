'''auto capitalize the first letter of any sentence or group of sentences
made by Kurai Umi'''

print("capitalize the first letter of the sentence")


text = input("text: ")

if text.endswith("."):
    text = text.split(".")
else:
    text += "."
    text = text.split(".")

#new text variable to update to capitals with "." that was removed by the split func
new_text = '.'


#new empty list that would get filled up by the iterables of "text" used to make the new_text
found = []


#note the variable a doesnt have any spacial func , you can change it to 0 in where its used
a = 0

#for loop to iterate through each element in the list of "text"
for i in text:

    #try except block to catch the error of "out of list index error"
    try:
        
        #first if is to get the first letter by the i index then update the found list with the captial and rest of string
        if text.index(i) == a:
            found.append(f"{i[a].upper() + i[a+1:]}")
        
        #second if to run as long as the index is within the length of the text list 
        #In the third part i used a+1+1 so that undertsanding the syntax would be easy
        elif text.index(i) <= len(text) - 2:
            found.append(f"{i[a] + i[a+1].upper() + i[a+1+1:]}")
        
        #third if to run if the the index is same as the length
        elif text.index(i) == len(text) - 1:
            found.append(f"{i[:]}")
            break
    except:
        print("error")

#print the new capitalized text
print(new_text.join(found))