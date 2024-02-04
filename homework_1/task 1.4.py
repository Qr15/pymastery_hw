text = 'para bellum'
s = text.find(' ')
a = text[s + 1:] + text[s] + text[:s]
print(a)
