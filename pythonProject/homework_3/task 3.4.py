shop_list = {}

while True:
    print("Выберете 1 что-бы добавить продукт")
    print("Выберете 2 что-бы удалить продукт")
    print("Выберете 3 что-бы посмотреть список продуктов")
    print("Выберете 4 что-бы посмотреть общую стоимотсть продуктов")
    print("Выберете 0 выход")

    choice = input("Введите номер действия 0-4: ")

    if choice == "0":
        print("Выход из программы.")
        break
    elif choice == "1":
        item = input('Введите надвание продукта :')
        price = float(input('Введите сумму продукта :'))
        quantity = int(input("Введите количество товара: "))
        if item in shop_list:
            shop_list[item]['quantity'] += quantity
        else:
            shop_list[item] = {'price': price, 'quantity': quantity}
    elif choice == "2":
        item = input("Введите название товара для удаления: ")
        if item in shop_list:
            del shop_list[item]
        else:
            print(f"{item} не найден в списке покупок.")
    elif choice == '3':
        if not shop_list:
            print("Список покупок пуст.")
        else:
            print("Список покупок:")
            for item, details in shop_list.items():
                print(f"{item} - {details['quantity']} шт. по {details['price']} USD за шт.")
    elif choice == '4':
        total = sum(details['price'] * details['quantity'] for details in shop_list.values())
        print(f"Общая стоимость покупок: {total} USD.")
    else:
        print("Некорректный ввод. Попробуйте снова.")




