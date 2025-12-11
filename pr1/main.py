from data_input import input_product
from calculations import calculate_stock_value, calculate_discount
from general import print_product_names, find_product_by_name


def main():
    print("--- Система управління товарами ---")

    # 1. Введення товарів
    products = input_product()
    # Виводимо словник (як на слайді 20, рядок 91)
    print("\nПоточна база:", products)

    # 2. Розрахунки
    calculate_stock_value(products)
    calculate_discount(products)

    # 3. Виведення списку
    print("\n--- Список товарів ---")
    product_names = list(products.keys())
    print_product_names(product_names)

    # 4. Пошук товару (ТЕПЕР У ЦИКЛІ)
    while True:
        print("\n----------------------------------")
        search_query = input("Введіть назву товару для пошуку (або 'exit' для виходу): ")

        # Перевірка на вихід
        if search_query.lower() == 'exit':
            print("Програму завершено. До побачення!")
            break

        # Виклик функції пошуку
        find_product_by_name(products, search_query)


if __name__ == "__main__":
    main()