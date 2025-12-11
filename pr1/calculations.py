def calculate_stock_value(product_info):
    print("\n--- Вартість залишків ---")
    for product, details in product_info.items():

        stock_value = details['Ціна'] * details['Залишок']

        print(f"Вартість залишку для {product}: {stock_value:.2f}")


def calculate_discount(product_info):
    print("\n--- Розрахунок знижок ---")
    for product, details in product_info.items():
        if details['Залишок'] < 10:

            discount = details['Ціна'] * 0.05
            final_price = details['Ціна'] - discount
            print(f"Знижка для {product}: {discount:.2f} (Нова ціна: {final_price:.2f})")
        else:
            print(f"Для {product} знижка не застосовується (залишок {details['Залишок']} од.)")