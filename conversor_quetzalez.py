def conversor(tipo_moneda, valor_dolar):
    quetzalez = input("¿Cuántos " + tipo_moneda + " tienes?: ")
    quetzalez = float(quetzalez)
    dolares = quetzalez / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $ " + dolares + " dolares")

menu = """
Bienvenido al conversor de monedas 😜

1 - Quetzales
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción"""

opcion = input(menu)

if opcion == '1':
    conversor("quetzalez", 7.83)
elif opcion == '2':
    conversor("pesos argentinos", 65)
elif opcion == '3':
    conversor("pesos mexicanos", 24)
else:
    print("Favor colocar una opción válida")

