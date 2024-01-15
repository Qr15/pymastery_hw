text = '123h 456 789 h753'
first_h, second_h = text.find('h'), text.rfind('h')
result = text[:first_h] + ' ' + text[second_h + 1:]
print(result)
