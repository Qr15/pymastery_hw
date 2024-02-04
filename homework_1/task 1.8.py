def greet(name, owner):
    if name.lower() == owner.lower():
        greeting = 'Hello boss'
    else:
        greeting = 'Hello gues'
    return greeting


name_input = input("Enter you name : ")
owner_input = input("Enter name owner : ")
result = greet(name_input, owner_input)
print(result)
