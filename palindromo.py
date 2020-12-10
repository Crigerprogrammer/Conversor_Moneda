def palindromo(palabra):
    palabra = palabra.replace(' ', '') # Eliminar los espacios
    palabra = palabra.lower() # Colocar la palabra en minusculas
    palabra_invertida = palabra[::-1] # Hace palabra invertida
    if palabra == palabra_invertida:
        return True
    else: 
        return False

def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


# Entry point (Función principal)
if __name__ == '__main__':
    run()