sales= []

monday = sales.insert(1,float(input('Введите сумму за понедельник: ')))
tuesday = sales.insert(1,float(input('Введите сумму за вторник: ')))
wednesday = sales.insert(1,float(input('Введите сумму за среду: ')))
thursday = sales.insert(1,float(input('Введите сумму за четверг: ')))
friday = sales.insert(1,float(input('Введите сумму за пятницу: ')))
saturday = sales.insert(1,float(input('Введите сумму за субботу: ')))
sunday = sales.insert(1,float(input('Ведите сумму за воскресенье: ')))

total_sales = 0

for number in sales:
    total_sales += number

print(f"Общая сумма продаж: {total_sales}")
