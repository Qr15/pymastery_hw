string = input("Enter a string: ")
text = ''
for i in range(len(string)):
    if i % 3 != 0:
        text = text + string[i]
print(text)
