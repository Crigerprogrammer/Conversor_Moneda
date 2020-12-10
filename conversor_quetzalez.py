menu = """
Bienvenido al conversor de monedas 😜

1 - Quetzales
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción"""

opcion = input(menu)

if opcion == '1':
    quetzalez = input("¿Cuántos quetzalez tienes?: ")
    quetzalez = float(quetzalez)
    valor_dolar = 7.83
    dolares = quetzalez / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $ " + dolares + " dolares")
elif opcion == '2':
    quetzalez = input("¿Cuántos pesos argentinos tienes?: ")
    quetzalez = float(quetzalez)
    valor_dolar = 65
    dolares = quetzalez / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $ " + dolares + " dolares")
elif opcion == '3':
    quetzalez = input("¿Cuántos pesos mexicanos tienes?: ")
    quetzalez = float(quetzalez)
    valor_dolar = 24
    dolares = quetzalez / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $ " + dolares + " dolares")
else:
    print("Favor colocar una opción válida")

