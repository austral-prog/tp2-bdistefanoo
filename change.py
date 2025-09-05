def change():
    expense = 23.75
    money = 100

    Vuelto = money - expense
    Pesos = int(Vuelto)
    Centavos = int(((Vuelto - Pesos)) * 100)

    print(f"Ingresar gasto:\n{expense}")
    print(f"Dinero recibido\n{money}")
    print("\nVuelto")
    print(f"\nPesos:\n{Pesos}")
    print(f"Centavos:\n{Centavos}")

change()
