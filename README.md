## Python

Un algoritmo es una lista finita de instrucciones que describen un cómputo, que cuando se ejectua con ciertas entradas (inputs) ejecuta pasos intermedios para llegar a un resultado (output)

Python es un lenguaje orientado a matematicas y por eso es uno de los más utilizados en la ciencia de datos

### Conceptos Básicos de Python  


**Operadores Aritméticos**  
- Suma(+)  
- Resta(-)  
- Multiplicación(*)  
- División(/)  
- Otros  


**Variables**  

*Reglas para declarar variables en Python* :  

- Pueden contener mayúsculas, minúsculas, números (sin comenzar con uno) y el símbolo _ 
- No pueden llamarse como las palabras reservadas


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

**Abstracción**  
No se necesita saber como opera internamente para poderlo operar 

#### Decomposición  

- Permite dividir el códgio en componentes que colaboran con un fin en común 

- Se puede pensar como mini programas dentro de un programa mayor

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

### Bucles 

Los bucles en python son una solución para repetir *n* cantidad de acciones con un bloque más simplificado de código, existen varios tipos de bucles dentro de python

**While**  

El ciclo while en python permite iterar una instrucción mientras se cumpla una condición. Ejemplo: 
```python
    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print('2 elevado a ' + str(contador) + 
        ' es igual a: ' + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador
```   
**For** 

El ciclo for permite iterar de una manera más simplificada instrucciones hasta un rango definido. Ejemplo:  

```python
    for contador in range(1, 1001): # Siempre llega al número -1 del 2do parametro
        print(contador)

    for i in range(10):
        print(11 * i)
```   

En los ciclos existen dos palabras reservadas que ayudan a interrumpir el funcionamiento de los ciclos, estas son: **break** y **continue**, la palabra reservada break interrumpe el ciclo cuando se encuentra con una condición antes dada por el algoritmo, mientras que continue hace que el ciclo corra después de encontrar la condición.  


### Estructuras de Datos  

---  

Las estructuras de datos son formas para guardar varios datos en una misma variable

**Listas**
Las listas tienen métodos los cuáles ayudan a poder trabajar con estas estructuras de datos, los métodos vistos son: *append*, *pop* y también se puede recorrar las listas con ciclos, Ejemplos:

```python
# Declarar una lista
numeros = [1, 3, 6, 8, 9, 45, 90]
print(numeros)

objetos = ['Hola', 3, 4.5, True]
print(objetos)

# Acceder a valores dentro de la lista
print(objetos[1])

# Metodo para lista, append, agrega un valor a la lista
objetos.append(False)

# Metodo para eliminar elemento de la lista, pop
objetos.pop(1)

# Recorrer lista con bucle

for elemento in objetos:
    print(elemento)
```   

**Tuplas** 
Las tuplas son similares a las listas, únicamente que son estáticas, no puede tener valores repetidas, ni tampoco eliminar datos de la tupla, tiene beneficios versus las listas, como por ejemplo que se recorre más rapido las tuplas  

- Son secuencias inmutables de objetos
- A diferencia de las cadenas pueden contener cualquier tipo de objeto
- Puede utilizarse para devolver varios valores en una función.


### Otros conceptos 

**Garbage Collector**  

Un recolector de basura (del inglés garbage collector) es un mecanismo implícito de gestión de memoria implementado en algunos lenguajes de programación de tipo interpretado o semiinterpretado.

Recolección de basura informática. El espacio de memoria se va llenando con diferentes “objetos”, también pueden destruirse algunos de ellos, dejando “huecos” en el espacio de memoria. Cuando ya no queda espacio disponible, o cuando lo decide la rutina de recolección de basura, la memoria es “compactada”, colocando todos los “objetos” que se están usando al principio, y consolidando todos los “huecos” de memoria al final, quedando así una gran área de memoria disponible para la futura creación de objetos.

### Algoritmos de Aproximación de soluciones  

---

- Similar a enumeración exhaustiva, pero no necesita una respuesta exacta

- Podemos aproximar soluciones con un margen de error que llamaremos epsilon

### Búsqueda Binaria

---

- Cuando la respuesta se encuentra en un conjunto ordenado, podemos utilizar búsqueda binaria

- Es altamente eficiente, pues corta el espacio de  búsqeuda en dos por cada iteración 

### Docstring
El docstring o la documentación está dividido en tres partes importantes que son las siguientes:

- Primero se da una descripción clara y concisa de la función y su funcionamiento

- En medio se agrega la descripción de los diferentes parámetros, su tipo, su nombre y que es lo que se espera de esos parámetros

- Por ultimo se agrega que es lo que devuelve nuestra función

### Recursividad

**Algoritmica** 
- Una forma de crear soluciones utilizando el principio de "divide y venceras" 

**Programatica**
- Una técnica programática mediante la cual una función se llama a sí misma. 

### Rangos

- Representan una secuencia de enteros.
- range(comienzo, fin, pasos)
- Al igual que las cadenas y las tuplas, los rangos son inmutables

### Listas y multibilidad

- Son secuencias de objetos, pero a diferente de las tuplas, sí son mutables.
- Cuando modificas una lista, pueden existir efectos secundarioas
- Es posible iterar con ellas
**Clonación**  
- Casi siempre es mejor clonar una lista en vez de mutarla
- Para clonar una lista podemos utilizar rebanadas (slices) o la función list
**List comprehension**
- Es una forma concisa de aplicar operaciones a los valores de una secuencia.
- También se pueden aplicar condiciones para filtrar.

### Diccionarios

- Son como listas, pero en lugar de usar índices utilizan llaves
- No tienen orden interno
- Los diccionarios son mutables
- Pueden iterarse

### Pruebas de caja negra

- Se basan en la especificación de la función o el programa
- Prueba inputs y valida outputs
- Unit testing o integration testing