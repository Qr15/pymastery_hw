youre_numbers = input("Enter numbers: ").split()
string_make_iteger = [int(i) for i in youre_numbers]
a = [i for i in string_make_iteger if i % 3 == 0]
print(a)
