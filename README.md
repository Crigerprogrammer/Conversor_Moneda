## Curso Básico de Python  


Curso por Platzi, link del curso [aquí](https://platzi.com/clases/python/).
---
### Conceptos Básicos de Python  


**Operadores Aritméticos**  
- Suma(+)  
- Resta(-)  
- Multiplicación(*)  
- División(/)  
- Otros  


**Variables**  


En Python las variables son como cajas, y puede almacenar cualquier valor, númerico o strings sin antes ser definidos como otros lenguajes de programación, para almacenar un valor númerico bastará con solo agregar el valor, mientras que con textos deberá utilizarse "" o ''. Ejemplos:  

```python
texto = "Esta es una variable texto"
numero = 20
```  

**Tipos de datos sencillos**  

En python existen tipos de datos, entre los más fáciles son: *int* *str* *float* son valores **enteros** **cadenas** **decimales** respectivamente  

**Convertir tipos de datos**  

Para convertir un número a cadena o viceversa se puede utilizar funciones de los valores correspondientes Ejemplo:  

```python
texto = "2" #El numero 2 es un valor text porque esta dentro de comillas
text = int(texto) #Ahora en la variable text almacenaremos el valor de texto en valor entero
```  

**Operadores Lógicos y de Comparación**  


Los operadores lógicos son aquellos que nos permiten verificar el valor booleano de expresiones, dentro de la programación existen dos posibles valores para tipos de datos booleanos, esos son: **True** ó **False**, existen varios operadores lógicos como: *and*, *or* ó *not* . Ejemplos:  

```python
expresion1 = True #Asignamos valor booleano
expresion2 = False #Asignamos valor booleano

expresion1 and expresion2 #Esto retornará False ya que una de las expresiones es falsa, hace que toda la expresión sea falsa

expresion1 or expresion2 #Esto retornará True ya que una de las dos expresiones es verdadera

not expresion1 #Esto retornará False, ya que invierte el valor original booleano a su contraparte
```   


**Operadores de Comparación**  
En python existen operadores para comparar nuestras expresiones, los más comunes son: **==**, **<** , **>** **>=** **<=**, estos operadores pueden utilizarse como en valores númericos como en valores string, Ejemplo: 

```python
numero1 = 10
numero2 = 20
numero1 > numero2 #Esto retornará un valor booleano, en esta ocasión será, falso ya que 10 no es mayor a 20
```  

### Condicionales  


---  

Las palabras reservadas para realizar una condición en python son: *if*, *elif* y *else*, estas palabras reservadas nos permitirá crear distintos caminos en un programa, ejemplos: 

```python
# Preguntar usuario edad y guardarlo como entero
edad = int(input("Escribe tu edad: "))
# usar condicional
if edad > 17:
    print ('Eres mayor de edad')
else:
    print ('Eres menor de edad')
``` 

Tomar en nota que después de terminar una regla if va seguido del caracter **:** y luego en la siguiente línea indentación (4 espacios)  

---  


### Funciones

Las funciones en python ayudan a no repetir código, las funciones se declaran con la palabra reservada **def** seguido del nombre de la funcion y luego **()** y al finalizar con **:**, luego se coloca el bloque de código y esa sería la función, luego se puede llamar la función o invocar, con el nombre de la función más parametros dentro de parentesis si en dado caso se declararon antes.

Sintaxis:
```python
def imprimir_mensaje():
    print('Mensaje especial: ')
    print('Estoy aprendiendo a usar funciones')

imprimir_mensaje()
imprimir_mensaje()
imprimir_mensaje()
```   
**RETURN**  

Existe una palabra reservada llamada *return* que nos permite dentro de las funciones retornar el valor de la función y poder utilizarla a lo largo del programa almacenandola en una variable. EJEMPLO:

```python
def suma(a, b):
    print('Se suman dos números')
    resultado = a + b
    return resultado

sumatoria = suma(1, 4)
print(sumatoria)
```   

### Metodos  


Existen métodos ya establecidos para objetos en python, a continuación veremos los métodos para los objetos tipo string:  

- **upper()** : Este metodo permite colocar toda la cadena de texto en mayúsculas 
- **lower()** : Este método permite colocar toda la cadena de texto en minúsculas 
- **capitalize()** : Este método permite colocar la inicial del texto en mayúscula
- **strip()** : Este método permite eliminar los espacios de las cadenas de texto 
- **replace** : Este método obtiene 2 parametros, el primero es el valor que queremos buscar dentro de la cadena y el segundo paramentro es el valor por el que lo reemplazaremos.  
- **len()** : Este método retorna la longitud de la cadena de cáracteres

### Indices 

En python podemos acceder a los cáracteres de la cadena de caracteres. Ejemplo: 
```python
nombre = "Cristian"
nombre[1] #Esto retornará el caracter r 
nombre[0] #Esto retornará el caracter C
```   

### Slices de cadenas  

En python se puede hacer slices de cadenas, para obtener una porción de la cadena original y poderla almacenar en variables o realizar diferentes funcionalidadaes.  
La sintaxis es:  

```python
nombre = "Cristian"
nombre[0:3] #Esto retornará Cri
nombre[:3] #Esto retornará Cri también
nombre[3:] #Esto retornará stian
print(nombre[0:7:2]) #Retornará Cita, ya que hace saltos de 2
```   




