"""
Funciones M3
"""
#--------------------------------------------------------------------------------------------------------------------------------------------------

# Crearemos la función para Ejercicio 1.
# Con la palabra reservada def-que define la función, luego indicamos como se llamara la función y en los
# paréntesis se ingresan los atributos de la función que en caso de nosotros serian números.
def sort_out_numbers(number):

    """
    Ejercicio 1
    Escribir un programa que lea entre 10 a 20 números ingresados por el usuario, los 
    almacene en una lista y los muestre ordenados de mayor o menor. Debe recibir el ingreso 
    de números hasta que el usuario ingrese 0. Pero el 0 no se debe mostrar en pantalla.
    """
    """
    Nota: Con el 0 se puede detener el funcionamiento si ingresamos mas de 10 numeros hasta 20,
          si son los 20 numeros ingresados programa se detendra sola.
    """
    # Crearemos una variable que sería una lista vacía, donde guardaremos los numeros ingresados por el usuario.
    list_number = []

    # Con el ciclo while, le indicamos que mientras es verdadero hacer las siguientes acciones:
    while True:

        # Con palabra reservada try vamos a tratar el bloque de código de tal forma que los errores que están
        # esperados, tratarlos como una excepción que los indicaremos más adelante.
        try:
            # Crearemos una variable donde guardaremos el valor ingresado por el usuario transformándolo de cadena a tipo entero.
            number = int ( input ("\nIngresa el número, para finalizar presione '0'\n"))

            # Con el ciclo if controlaremos cuando el usuario ingresara 0 para salir y también revisaremos que ingreso mas de
            # 10 números si se cumple la condición, organizaremos la lista de numeros del mayor a menor con el metodo
            # .sort(reverse=True), luego le indicamos que realizaremos la salida del ciclo con la instrucción break.
            if number == 0 and len(list_number) > 9:

                # Organizaremos la lista de mayor a menor.
                list_number.sort(reverse=True)

                # Instrucción de salida del ciclo.
                break
            
            # Con el siguiente condicional vamos a prevenir la salida del usuario din el programa si ingresa menos de 10 números.
            elif number == 0 and len(list_number) < 9:
                # Mostramos un mensaje por pantalla indicándole cuantos números le faltan por ingresar.
                print(f"Faltan para ingresar {(10 - len(list_number))} numeros mas.")
            
            # Con este condicional vamos a interrumpir la función si se intentara ingresar mas de 20 números.
            elif len(list_number) >= 19:
                print("\nAlcanzaste el volumen máximo de elementos admisibles. El ejercicio finalizara.\n")
                list_number.sort(reverse=True)
                break
            
            # En caso si la condición del if y elif no se cumple, con el método .append() agregaremos el elemento a la lista list_number.
            elif number != 0:
                list_number.append(number)
        
        # Como indicamos anteriormente en la instrucción try llegamos al punto donde tenemos que hacer el manejo de errores.
        # Con el except indicaremos que: el error de tipo ValueError (se trata de los caracteres que ingresara el usuario
        # que no corresponden a valores numéricos) que sella tratado como una excepción y tiene que retornar
        # el print que lo contiene la excepción.
        except ValueError:
            print ("\nError. Ingrese un número.\n")

    # Y por último indicaremos que la siguiente función nos entregara como resultado la lista de números ingresadas por el usuario
    # y ordenada de menor a mayor.
    return list_number
#--------------------------------------------------------------------------------------------------------------------------------------------------

# Crearemos la función para Ejercicio 2.
# Con la palabra reservada def-que define la función, luego indicamos como se llamara la función y en los
# paréntesis se ingresan los atributos de la función que en caso de nosotros serian palabras.
def sort_out_words(word):

    """
    Ejercicio 2
    Escribir un programa que almacene palabras ingresadas por el usuario. Debe recibir 
    ingreso de palabras hasta que el usuario ingrese tres asteriscos ***. Luego de esto, las 
    palabras se deben mostrar por pantalla una única vez. Es decir que, si el usuario ingresó
    palabras repetidas, se deben mostrar solo una vez.
    """

    # Crearemos una variable que sería una lista vacía, donde guardaremos las palabras ingresadas por el usuario.
    list_words = []
    
    # Crearemos una variable que sería una lista vacía, donde guardaremos las palabras ingresadas por el usuario
    # pero eliminando las palabras que se repiten.
    list_without_duplicates = []
    
    # Con el ciclo while, le indicamos que mientras es verdadero hacer las siguientes acciones:
    while True:
            
            # Crearemos una variable donde guardaremos el valor ingresado por el usuario.
            word = input ("\nIngresa palabra, para finalizar ingrese '***'\n")

            # Con el ciclo if revisaremos si la palabra ingresada es idéntica a 3 asteriscos
            # sí es así, usaremos la función set para eliminar las palabras repetidas,
            # y con la función list los guardaremos en la lista creada anteriormente list_without_duplicates.
            # Finalmente indicamos la salida din ciclo while con la instrucción break.
            if word == "***":

                # Eliminación de palabras repetidas y los asignamos a la lista vacía creada anteriormente.
                list_without_duplicates = list(set(list_words))

                # La instrucción de salida del ciclo while.
                break

            # Creación de otra condición que nos ayudaria a manejar errores.
            # Si los caracteres que ingrese el usuario no son de formato alfabético,
            # imprimir en pantalla un mensaje de error.
            elif not word.isalpha():
                
                # Mensaje de error.
                print ("\nError, ingresa solo palabras\n")
            
            # En todos los demás casos, con el método: .lower() cambiaremos todo los caracteres de la palabra
            # ingresada por el usuario en minúsculas y finalmente mediante el método: .append() agregaremos la palabra
            # a la lista list_words creada anteriormente.
            else:

                # Conversión de los caracteres de la palabra ingresada por el usuario a minúsculas.
                word = word.lower()

                # Agregamos la palabra a la lista list_words creada anteriormente.
                list_words.append(word)
    
    # Con el return le indicamos que la función devolverá la lista list_without_duplicates sin palabras repetidas.
    return list_without_duplicates
#--------------------------------------------------------------------------------------------------------------------------------------------------

# Crearemos la función para Ejercicio 3.
# Con la palabra reservada def-que define la función, luego indicamos como se llamara la función y en los
# paréntesis se ingresan los atributos de la función que en caso de nosotros serian palabras.
def proceso_scrable(word):

    
    """
    Ejercicio 3
    ¡Juguemos Scrabble!
    Construir un diccionario con los siguientes valores. Luego, el usuario ingresa una palabra 
    por pantalla, y el programa devuelve el puntaje.
    """

    # Creacion de dicionario que se utilizara para desaroyo de la funcion en continuacion.
    dictionary_scrabble = {"A":1,"E":1,"I":1,"L":1,"N":1,"O":1,"R":1,"S":1,"T":1,"U":1,"D":2,"G":2,"B":3,
                           "C":3,"M":3,"P":3,"F":4,"H":4,"V":4,"W":4,"Y":4,"K":5,"J":8,"X":8,"Q":10,"Z":10}
    
    # Creacion de una variable que almacenara un valor entero que coresponde al puntaje de cada palabra.
    score = int(0)
    
    # Con el ciclo for bamos a recorer la llave y valor en cada par del diccionario dictionary_scrabble
    for key, value in dictionary_scrabble.items():
        
        # con otro for indicaremos que para cada caracter de la palabra ingresada por el usuario
        # haremos lo siguente:
        for character in word:
            
            # Si el caracter de la palabra es igual con la llave del diccionario a la variable score
            # le sumaremos el valor de la cada llave que coincida.
            if character == key:
                
                # Suma de un valor a un valor existente en una variable (encremiento de un valor contenido).
                score += value

    # Y finalmente le indicamos que resultado que debe entregarnos la funcion, es el valor de la variable score.
    return (score)
#--------------------------------------------------------------------------------------------------------------------------------------------------

# Crearemos la función para Ejercicio 4.
# Con la palabra reservada def-que define la función, luego indicamos como se llamara la función y en los
# paréntesis se ingresan los atributos de la función que en caso de nosotros quedara vacia.
def words_anagrams (word_1, word_2):

    """
    Ejercicio 4
    Construir un programa que determine si dos palabras ingresadas por el usuario son 
    anagramas.
    """

    # Con el ciclo while, le indicamos que mientras es verdadero hacer las siguientes acciones:
    while True:
        
        # Pediremos al usuario que ingrese una palabra y lo guardaremos en variable word_1.
        word_1 = input ("\nIngresa palabra 1:\n")
        
        # Pediremos al usuario que ingrese otra palabra y lo guardaremos en variable word_2.
        word_2 = input ("\nIngresa palabra 2:\n")
        
        # Con el método .lover() cambiaremos las palabras a minúsculas y con método
        # .replace(" ", "") vamos a substituir los espacios por nada,
        # (con otras palabras, si usuario ingresara algún espacio vacío el método replace lo eliminara).
        word_1 = word_1.replace(" ", "").lower()
        word_2 = word_2.replace(" ", "").lower()
        
        # Con el ciclo if controlaremos que el usuario no ingrese caracteres que no son alfabéticos.
        # Si detecta números u otros caracteres especiales enviaremos un mensaje de error.
        if not word_1.isalpha() or not word_2.isalpha():
            
            # Mensaje de error.
            print ("\nError, ingresa solo palabras.\n")
        
        # Con la condicional elif controlamos que el largo de las palabras sella igual.
        # Si es diferente mandaremos un mensaje de error.
        elif len(word_1) != len(word_2):

            # Mensaje de error.
            print ("\nError, las palabras ingresadas deben tener mismo largo y caracteres, no importa el orden.\n")
        
        # En los demás casos le indicaremos que con la instrucción break salga del ciclo while.
        else:
            break
    
    # Crearemos dos diccionarios vacíos.
    dictionary_word_1 = {}
    dictionary_word_2 = {}

    # Con el ciclo for vamos a recorrer para cada carácter (char_1) en palabra (word_1)
    # y los guardaremos en diccionario (dictionary_word_1), con el método .get(char_1, 0) + 1
    # toma un carácter como clave y le da un valor el primero seria 0+1 si encuentra el mismo
    # carácter en otra posición le agrega uno más seria 1+1 y vendrá modificando el diccionario
    # por cada carácter hasta terminar todos los caracteres de la palabra.
    for char_1 in word_1:
        dictionary_word_1[char_1] = dictionary_word_1.get(char_1, 0) +1
    
    # Actúa lo mismo como en primer ciclo for solo que se trata de la segunda palabra
    for char_2 in word_2:
        dictionary_word_2[char_2] = dictionary_word_2.get(char_2, 0) +1
    
    # Con el if hacemos la comparación de los diccionarios si son idénticos nos devuelve un True
    # si no con el else: nos devuelve un False, en esta ocasión la función nos devolvera un valor booleano como resultado.
    if dictionary_word_1 == dictionary_word_2:
        return True
    else:
        return False
#--------------------------------------------------------------------------------------------------------------------------------------------------

# Crearemos la función para Ejercicio 5.
# Con la palabra reservada def-que define la función, luego indicamos como se llamara la función y en los
# paréntesis se ingresan los atributos de la función que en caso de nosotros seria la numero.
def sum_up_number(number):

    """
    Ejercicio 5
    Construir un programa en donde el usuario ingrese número por pantalla y el programa 
    devuelva la suma de cada número ingresado por el usuario. Si el usuario ingresa un 
    carácter no numérico, debe mostrar mensaje de error y continuar solicitando números y 
    sumando. El programa finaliza cuando usuario presiona enter con espacio en blanco.
    """
    
    # Crearemos una variable sum_of_numbers que guardara la suma de los numeros que ingresara el usuario.
    sum_of_numbers = 0
    
    # Con el ciclo while, le indicamos que mientras es verdadero hacer las siguientes acciones:
    while True:
        
        # Con palabra reservada try vamos a tratar el bloque de código de tal forma que los errores que están
        # esperados, tratarlos como una excepción que los indicaremos más adelante.
        try:
            # Crearemos una variable numero que guardara el valor ingresado por el usuario seria guardado como cadena.
            number = input("\nIngresa numero a sumar, para finalizar ingresar un espacio en blanco seguido de enter:\n")
            
            # Con el condicional if compararemos si el ingreso corresponde a un espacio en blanco
            # terminaremos la función con la instrucción break.
            if number == " ":
                break
            
            # Si no con el else transformaremos el valor guardado en variable number a numero flotante
            # ya que el usuario pueda ingresar numeros con decimales y lo guardamos en la misma variable
            # luego incrementamos el valor de la variable sum_of_numbers con el valor guardado en la
            # variable number, finalizando imprimiremos el mensaje con la suma de los numeros.
            else:
                # Transformación de cadena a numero flotante.
                number = float(number)
                # Incrementamos el valor de la variable sum_of_numbers con el valor que contiene la variable number.
                sum_of_numbers += number
                # Luego mostramos el mensaje con el valor de la suma.
                print(f"\nLa suma de los numeros es: {sum_of_numbers:.2f}\n")
        
        # Como indicamos anteriormente en la instrucción try llegamos al punto donde tenemos que hacer el manejo de errores.
        # Con el except indicaremos que: el error de tipo ValueError (se trata de los caracteres que ingresara el usuario
        # que no corresponden a valores numéricos) que sella tratado como una excepción y tiene que retornar
        # el print que contiene la excepción.
        except ValueError:
            print ("Error, ingresa solo numeros.")
    
    # Resultado de la función seria la suma de todos los numeros.
    return sum_of_numbers
#--------------------------------------------------------------------------------------------------------------------------------------------------

# Función para menú.

def menu ():
    print("\n******************************************************************")
    print("|                     MENU DEL TRABAJO M3:                       |\n")
    print("******************************************************************")
    print("* Ver funcionamiento del programa M3 completo:        presiona 1 *")
    print("* Ver funcionamiento del programa M3 por Ejercicios:  presiona 2 *")
    print("* Salir de la ejecución del programa M3:              presiona 3 *\n")
    print("******************************************************************\n")
    # No retorna nada
    return None

# Función para sub menú (opción 2 en menú).

def sub_menu_opcion_2 ():
    print("\n+-----------------------------------------------------------+")
    print("|               MENU EJERCICIOS TRABAJO M3:                 |")
    print("+-----------------------------------------------------------+")
    print("| Para ejercicio 1 'Numeros en lista':           presione 1 |")
    print("| Para ejercicio 2 'Almacenamiento de palabras': presione 2 |")
    print("| Para ejercicio 3 'Juguemos Scrabble':          presione 3 |")
    print("| Para ejercicio 4 'Palabras anagramas':         presione 4 |")
    print("| Para ejercicio 5 'Suma numeros ingresados':    presione 5 |")
    print("| Salir de la ejecucion del programa M3:         presiona 6 |")
    print("+-----------------------------------------------------------+\n")
    # No retorna nada
    return None
#--------------------------------------------------------------------------------------------------------------------------------------------------

"""
Cuerpo del programa
"""
# Con el ciclo while, le indicamos que mientras es verdadero hacer las siguientes acciones:
while True:

    # Llamando a la función menú.
    menu ()

    # Con palabra reservada try vamos a tratar el bloque de código de tal forma que los errores que están
    # esperados, tratarlos como una excepción que los indicaremos más adelante.
    try:

        # Crearemos una variable opción donde guardaremos la opción del menú seleccionado por el usuario.
        option = int(input("Selecione una opcion:\n"))
        if 1>option or option>3:
            raise ValueError ("Selecciona una opcion, un numero de 1 a 3.")
        # Si la opción seleccionada es 1 se ejecutarán todos los ejercicios seguidos uno de otro.
        if option == 1:
            # Mostraremos un mensaje de inicio de ejecución.
            print ("\nSe Ejecutará el programa completo")
#--------------------------------------------------------------------------------------------------------------------------------------------------
            """
            Ejercicio 1
            Escribir un programa que lea entre 10 a 20 números ingresados por el usuario, los 
            almacene en una lista y los muestre ordenados de mayor o menor. Debe recibir el ingreso 
            de números hasta que el usuario ingrese 0. Pero el 0 no se debe mostrar en pantalla.
            """
            # Mostraremos un mensaje indicando el número del ejercicio.
            print("\nEjercicio 1")
            
            # Creamos la variable list_for_print en cual guardaremos el resultado de la función 
            # del ejercicio 1 que esta al principio.
            # sort_out_numbers - Nombre de la función y en paréntesis number es el atributo que va iniciado en 0.
            list_for_print = sort_out_numbers(number = 0)
            
            # Imprimimos por pantalla el mensaje con la variable list_for_print que contiene el resultado de la función.
            print (f"\nLa lista de los numeros es:\n{list_for_print}")
#--------------------------------------------------------------------------------------------------------------------------------------------------
            """
            Ejercicio 2
            Escribir un programa que almacene palabras ingresadas por el usuario. Debe recibir 
            ingreso de palabras hasta que el usuario ingrese tres asteriscos ***. Luego de esto, las 
            palabras se deben mostrar por pantalla una única vez. Es decir que, si el usuario ingresó
            palabras repetidas, se deben mostrar solo una vez.
            """

            # Mostraremos un mensaje indicando el número del ejercicio.
            print("\nEjercicio 2")

            # Creamos la variable list_for_print en cual guardaremos el resultado de la función 
            # del ejercicio 1 que esta al principio.
            # sort_out_words - Nombre de la función y en paréntesis word es el atributo que va iniciado con una cadena vacía.
            list_for_print = sort_out_words(word = "")

            # Si el largo de la lista es igual a 0, imprimimos por pantalla el mensaje que no se ingresaron palabras.
            if len(list_for_print) == 0:
                print ("No hay palabras ingresadas")
            # Si la condicion del if no se cumple. Imprimimos por pantalla el mensaje con la variable list_for_print
            # que contiene el resultado de la función.
            else:
                print (f"La lista de las palabras es:\n{list_for_print}")
#--------------------------------------------------------------------------------------------------------------------------------------------------
            """
            Ejercicio 3
            ¡Juguemos Scrabble!
            Construir un diccionario con los siguientes valores. Luego, el usuario ingresa una palabra 
            por pantalla, y el programa devuelve el puntaje.
            """
            # Mostraremos un mensaje indicando el número del ejercicio.
            print("\nEjercicio 3\n")
            print("¡Juguemos Scrabble!")

            # Con el ciclo while, le indicamos que mientras es verdadero hacer las siguientes acciones:
            while True:

                # Con palabra reservada try vamos a tratar el bloque de código de tal forma que los errores que están
                # esperados, tratarlos como una excepción que los indicaremos más adelante.
                try:

                    # Crearemos una variable que guardara el numero transformado en entero, din cuantas palabras seria compuesto el juego,
                    # a su vez nos serviria de contador.
                    word_counter = int(input("\nDe cuantas palabras seria formado el Juego, de 1 a 'n': "))

                    # Crearemos una variable que guardara el puntaje total, pero por ahora le asignamos el 0.
                    total_score = 0

                    # Con el ciclo while mientras la variable word_counter es mayor a 0 haremos las siguiente acciones:
                    while word_counter > 0:
                        # Creamos una variable word donde guardaremos la palabra ingresada por el usuario.
                        word = input("\nIngrese una Palabra:\n")
                        # Luego convertimos todos los caracteres de la palabra a mayúscula con el metodo .upper().
                        word = word.upper()
                        # Creamos una variable game que recibirá el resultado de la función invocada proceso_scrable(word)
                        # donde la palabra word en los paréntesis es el atributo de la función.
                        game = proceso_scrable(word)
                        # Se mostrara en la pantalla el puntaje de cada palabra por separado.
                        print ("\nEl puntaje de la palabra es:", game)
                        # Puntaje total seria calculado incrementando el valor de la variable total_score con el valor de la variable game 
                        # que es el resultado de la función.
                        total_score += game
                        # Y finalmente al contador le restamos uno indicándole que cumplimos una vuelta.
                        word_counter -= 1
                        
                    # Una vez que el contador word_counter estará igual a 0 y saldrá din ciclo while imprimiremos por la pantalla
                    # un mensaje indicando el puntaje total obtenido.
                    print ("\nEl puntaje total de las palabras es:", total_score)

                # Como indicamos anteriormente en la instrucción try llegamos al punto donde tenemos que hacer el manejo de errores.
                # Con el except indicaremos que: el error de tipo ValueError (se trata de los caracteres que ingresara el usuario
                # que no corresponden a valores numéricos) que sella tratado como una excepción y tiene que retornar
                # el print que contiene la excepción.
                except ValueError:
                    print ("\nIngresa un numero entero mayor que 0")
                
                # Con el siguiente condicional controlamos la función del ciclo (while True:)
                # llegando el contador word_counter a 0 se romperá el ciclo con la instrucción break.
                if word_counter == 0:
                    break
#--------------------------------------------------------------------------------------------------------------------------------------------------
            """
            Ejercicio 4
            Construir un programa que determine si dos palabras ingresadas por el usuario son 
            anagramas.
            """
            # Mostraremos un mensaje indicando el número del ejercicio.
            print("\nEjercicio 4")
            # Con el if en la condición de este invocamos la función creada words_anagrams(word_1="", word_2=""),
            # donde word_1="" y word_2="" son los atributos de la función, las variables que almacenaran las dos palabras a comparar
            # e indicamos que almacenaran valores de tipo cadena. Y como la función retorna valores booleanos en caso de ser igual a
            # verdadero mostraremos por pantalla que las palabras son anagramas de otra forma si nos devuelve un falso se mostrara el
            # mensaje que las palabras no son anagramas.
            if words_anagrams(word_1="", word_2="") == True:
                # Mensaje para imprimir si la condición es verdadera.
                print ("\nLas palabras son anagramas.")
            else:
                # Mensaje para imprimir si la condición es falsa, ya que otros casos no tenemos se devuélvera un True o un False.
                print ("\nLas palabras no son anagramas.")
#--------------------------------------------------------------------------------------------------------------------------------------------------
            """
            Ejercicio 5
            Construir un programa en donde el usuario ingrese número por pantalla y el programa 
            devuelva la suma de cada número ingresado por el usuario. Si el usuario ingresa un 
            carácter no numérico, debe mostrar mensaje de error y continuar solicitando números y 
            sumando. El programa finaliza cuando usuario presiona enter con espacio en blanco.
            """
            # Mostraremos un mensaje indicando el número del ejercicio.
            print("\nEjercicio 5")
            # Creamos la variable sum_number en cual guardaremos el resultado de la función 
            # del ejercicio 5 que esta al principio.
            # sum_up_number - Nombre de la función y en paréntesis number=0 es el atributo que va iniciado con un 0.
            sum_number = sum_up_number(number=0)
            # Imprimimos por pantalla el mensaje con la variable sum_number:.2f que contiene el resultado de la función,
            # :.2f - indicamos que, como es un valor flotante nos entregue 2 decimales.
            print (f"La suma final de los numeros es: {sum_number:.2f}")
#--------------------------------------------------------------------------------------------------------------------------------------------------
        # Si la opción seleccionada es 2 se ejecutará el submenú.
        elif option == 2:
            # Hasta que es verdadero se muestra el submenú.
            while True:
                # Llamando a la función de submenú.
                sub_menu_opcion_2 ()
                # A continuación, me saltare los comentarios de los ejercicios ya que son idénticos a los anteriores.
                try:
                    # Pedimos al usuario que escoja la opción del submenú.
                    option = int(input("\nSelecione una opcion:\n"))
                    # Con el if verificamos que la opción sella en el rango de 1 a 6
                    # de otra forma mandaremos un mensaje por pantalla indicando el error.
                    if 1 > option or option > 6:
                        print ("Selecciona una opcion valida porfavor.")
                    
                    # Si la opción seleccionada es 1 se ejecutará el ejercicio 1
                    if option == 1:
                        print("\nEjercicio 1")
                        list_for_print = sort_out_numbers(number=0)
                        print (f"\nLa lista de los numeros es:\n{list_for_print}")
                    
                    # Si la opción seleccionada es 2 se ejecutará el ejercicio 2
                    elif option == 2:
                        print("\nEjercicio 2")
                        list_for_print = sort_out_words(word = "")
                        if len(list_for_print) == 0:
                            print ("No hay palabras ingresadas")
                        else:
                            print (f"La lista de las palabras es:\n{list_for_print}")
                    
                    # Si la opción seleccionada es 3 se ejecutará el ejercicio 3
                    elif option == 3:
                        print("\nEjercicio 3")
                        while True:
                            try:
                                word_counter = int(input("\nDe cuantas palabras seria formado el Juego, de 1 a 'n': "))
                                total_score = 0

                                while word_counter > 0:
                                    word = input("\nIngrese una Palabra:\n")
                                    word = word.upper()
                                    game = proceso_scrable(word)
                                    print ("\nEl puntaje de la palabra es:", game)
                                    total_score += game
                                    word_counter -= 1
                                    print ("\nEl puntaje de la palabra es:", total_score)
                                print ("\nEl puntaje total de las palabras es:", total_score)

                            except ValueError:
                                print ("Ingresa un numero entero mayor que 0")

                            if word_counter == 0:
                                break

                    # Si la opción seleccionada es 4 se ejecutará el ejercicio 4
                    elif option == 4:
                        print("\nEjercicio 4")
                        if words_anagrams(word_1="", word_2="") == True:
                            print ("\nLas palabras son anagramas.")
                        else:
                            print ("\nLas palabras no son anagramas.")
                    
                    # Si la opción seleccionada es 5 se ejecutará el ejercicio 5
                    elif option == 5:
                        print("\nEjercicio 5")
                        sum_number = sum_up_number(number=0)
                        print (f"La suma final de los numeros es: {sum_number:.2f}")

# En este apartado se hacen los controles de errores y opciones de salida del menú y submenú.
                    elif option == 6:
                        print("Gracias por revisar M3")
                        break
                except ValueError:
                    print ("Selecciona una opcion, un numero de 1 a 6.")
                except KeyboardInterrupt:
                    print ("Hasta luego.")
                    break     
        elif option == 3:
            print("\nGracias por revisar M3\n")
            break
    except ValueError:
        print ("Selecciona una opcion, un numero de 1 a 3.")
    except KeyboardInterrupt:
        print ("\nHasta luego.")
        print("\nGracias por revisar M3.\n")
        break