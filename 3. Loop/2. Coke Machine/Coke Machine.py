# Función principal para ejecutar el proceso de pago
def main():
    # Establece el monto adeudado inicialmente
    amount_due = 50
    # Define las monedas aceptadas en la lista
    accepted_coins = [25, 10, 5]

    # Continúa solicitando monedas hasta que el monto adeudado sea 0
    while amount_due > 0:
        try:
            # Solicita al usuario que inserte una moneda
            coin = int(input("Insert Coin: "))
            # Si la moneda ingresada está en la lista de monedas aceptadas
            if coin in accepted_coins:
                # Reduce el monto adeudado por el valor de la moneda
                amount_due -= coin
                # Si aún queda un monto adeudado, imprime el monto restante
                if amount_due > 0:
                    print(f"Amount Due: {amount_due}")
                # Si no hay monto adeudado, imprime el cambio a devolver
                else:
                    print(f"Change Owed: {-amount_due}")
            # Si la moneda ingresada no es aceptada, imprime el monto adeudado
            else:
                print(f"Amount Due: {amount_due}")
        # Si se ingresa un valor no numérico, muestra el monto adeudado
        except ValueError:
            print(f"Amount Due: {amount_due}")

# Si el script se ejecuta directamente (no importado como módulo)
if __name__ == "__main__":
    # Llama a la función principal para iniciar el proceso de pago
    main()
