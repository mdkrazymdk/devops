def input_product():
    products = {}
    while True:
        name = input("Введіть назву товару (або 'stop' щоб закінчити): ")

        if name.lower() == 'stop':
            break


        if name.lower() == 'demo':
            return {
                "Товар1": {'Ціна': 100.50, 'Залишок': 10},
                "Товар2": {'Ціна': 200.75, 'Залишок': 5},
                "Товар3": {'Ціна': 50.30, 'Залишок': 20}
            }

        try:

            price = float(input("Введіть ціну товару: "))  # код отримання ціни
            stock = int(input("Введіть кількість товару: "))  # код отримання кількості


            products[name] = {'Ціна': price, 'Залишок': stock}
        except ValueError:
            print("Помилка! Введіть числа.")

    return products