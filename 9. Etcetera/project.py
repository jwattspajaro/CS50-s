import json
import re

class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - {self.category} - ${self.price:.2f} - x{self.quantity}"

class ShoppingList:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        self.products = [product for product in self.products if product.name.lower() != product_name.lower()]

    def mark_product_as_bought(self, product_name):
        for product in self.products:
            if product.name.lower() == product_name.lower():
                product.quantity -= 1

    def show_products(self):
        for product in self.products:
            print(product)

    def filter_by_category(self, category):
        filtered_products = [product for product in self.products if product.category.lower() == category.lower()]
        return filtered_products

    def calculate_total_cost(self):
        total_cost = sum(product.price * product.quantity for product in self.products)
        return total_cost

    def sort_products(self, by="name"):
        if by.lower() == "name":
            self.products.sort(key=lambda product: product.name.lower())
        elif by.lower() == "category":
            self.products.sort(key=lambda product: product.category.lower())

    def get_categories(self):
        categories = sorted(set(product.category for product in self.products))
        return categories

def main():
    shopping_list = ShoppingList()

    while True:
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Marcar producto como comprado")
        print("4. Mostrar productos")
        print("5. Filtrar productos por categoría")
        print("6. Calcular costo total estimado")
        print("7. Ordenar productos")
        print("8. Salir")

        try:
            option = int(input("\nSeleccione una opción: "))
        except ValueError:
            print("Opción no válida. Intente nuevamente.")
            continue

        if option == 1:
            name = input("Ingrese el nombre del producto: ")
            category = input("Ingrese la categoría del producto: ")
            price = float(input("Ingrese el precio del producto: "))
            quantity = int(input("Ingrese la cantidad del producto: "))
            product = Product(name, category, price, quantity)
            shopping_list.add_product(product)

        elif option == 2:
            name = input("Ingrese el nombre del producto a eliminar: ")
            shopping_list.remove_product(name)

        elif option == 3:
            name = input("Ingrese el nombre del producto comprado: ")
            shopping_list.mark_product_as_bought(name)

        elif option == 4:
            shopping_list.show_products()

        elif option == 5:
            categories = shopping_list.get_categories()
            print("Categorías disponibles

        elif option == 6:
            total_cost = shopping_list.calculate_total_cost()
            print(f"Costo total estimado: ${total_cost:.2f}")

        elif option == 7:
            sort_by = input("Ordenar productos por [name/category]: ")
            shopping_list.sort_products(sort_by)
            shopping_list.show_products()

        elif option == 8:
            shopping_list.show_products()
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
