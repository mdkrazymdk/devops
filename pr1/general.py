
def print_product_names(product_names, index=0):
    if index < len(product_names):
        print(product_names[index])
        print_product_names(product_names, index + 1)


def find_product_by_name(products, product_name, index=0):
    product_keys = list(products.keys())


    if index >= len(product_keys):
        print("\nТовар не знайдено.")
        return


    if product_keys[index] == product_name:

        info = products[product_name]
        print(f"\nТовар знайдено: {product_name}")
        print(f"Ціна: {info['Ціна']}, Залишок: {info['Залишок']}")
        return


    find_product_by_name(products, product_name, index + 1)