# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA/FUNDAMENTOS DE COMPUTACIÓN Y PROGRAMACIÓN
# SECCIÓN DEL CURSO: 0-C-1
# PROFESOR DE TEORÍA: CARLOS VERA
# PROFESOR DE LABORATORIO: ANDRÉS MUÑOZ
#
# AUTOR
# NOMBRE: Alfonso Sebastian Palacios Vergara
# RUT: 23.345.432-2
# CARRERA: Ingeniería Civil Informática
#________________________________________________________________________________________________________
"""""
Considere que las variables que son sólo una letra representan simplemente índices para
ciclos 'while', y que aquellas que poseen "aux" en su nombre son nada más que variables
auxiliares para realizar los procesos pertinentes
"""""
#________________________________________________________________________________________________________


# Definiremos la primera función, que leerá un archivo '.lab' y retornará el
# laberinto contenido en él como una lista de listas
def cargar_laberinto(nombre):
  """"
  ENTRADA: Un nombre de un archivo que debe estar en formato '.lab'
  
  SALIDA: El laberinto contenido en este archivo, como una lista de listas cuyos
  elementos sean cada nivel del mismo y sus caracteres

  PROCESAMIENTO:
  """""

  # Primero, si el nombre del archivo no es '<arhcivo>.lab', retornamos una lista vacía
  if nombre.split(".")[-1] != "lab":
    return []

  # Luego, abrimos el archivo en modo lectura como una lista de stirngs usando readlines
  with open(nombre, "r") as archivo:
    laberinto = archivo.readlines()

    # Para eliminar los caracteres ',', recorremos la lista
    i = 0
    while i < len(laberinto):

      # Si encuentra un caracter ',', lo elimina
      if laberinto[i] == ",":
        laberinto.pop(i)
      i += 1

    # Definimos al laberinto como un string
    laberinto = "".join(laberinto)

    # Luego, separamos la lista por '\n' para eliminar estos caracteres
    laberinto = laberinto.split("\n")

    # Para eliminar los caracteres ' ', recorremos la lista
    i = 0
    while i < len(laberinto):

      # Como laberinto es una lista de strings, definimos sus elementos como
      # listas separadas por ' '
      laberinto[i] = laberinto[i].split(" ")
      i += 1

    # Por último, retornamos la lista de listas con el laberinto
    return laberinto


#________________________________________________________________________________________________________


# Para continuar, definiremos la segunda función, que encontrará la entrada del
# laberinto anterior y retornará una lista de 2 números enteros que
# representarán sus coordenadas
def encontrar_entrada(laberinto):
  """"
  ENTRADA: Un laberinto con las especificaciones de la salida de
  la función 'cargar_laberinto'
  
  SALIDA: La posición de la entrada en este laberinto, como una lista de 2
  números enteros
  
  PROCESAMIENTO:
  """""

  # Para encontrar la entrada, con la forma del caracter 'EE', recorremos la
  # lista de listas y recorremos cada lista contenida en esta lista de listas
  i = 0
  j = 0
  while i < len(laberinto):
    while j < len(laberinto[i]):

      # Si encuentra la entrada (caracter 'EE'), retorna una lista
      # con la posición en la lista de listas y la posición en
      # la lista elemento de la lista de listas en la que está
      if laberinto[i][j] == "EE":
        return [i, j]
      j += 1
    j = 0
    i += 1


#________________________________________________________________________________________________________


# Luego, definiremos la tercera función, que será análoga a la anterior pero
# encontrará la salida del laberinto en vez de la entrada
def encontrar_salida(laberinto):
  """"
  ENTRADA: Un laberinto con las especificaciones de la salida de
  la función 'cargar_laberinto'

  SALIDA: La posición de la salida en este laberinto, como una lista de 2
  números enteros

  PROCESAMIENTO:
  """""

  # Para encontrar la salida, con la forma del caracter 'SS', recorremos la
  # lista de listas y recorremos cada lista contenida en esta lista de listas
  i = 0
  j = 0
  while i < len(laberinto):
    while j < len(laberinto[i]):

      # Si encuentra la salida (caracter 'SS'), retorna una lista
      # con la posición en la lista de listas y la posición en
      # la lista elemento de la lista de listas en la que está
      if laberinto[i][j] == "SS":
        return [i, j]
      j += 1
    j = 0
    i += 1


#________________________________________________________________________________________________________


# Por último, defeiniremos la cuarta función, que encontrará la lista de movimientos
# a realizar para ir desde la entrada del laberinto hasta la salida
def recuperar_camino(laberinto):
  """"
  ENTRADA: Un laberinto con las especificaciones de la salida de
  la función 'cargar_laberinto'

  SALIDA: La lista de movimientos a realizar para ir desde la entrada
  hasta la salida del laberinto

  PROCESAMIENTO:
  """""

  # Primero, definimos la posición de la entrada y la salida usando las
  # funciones definidas anteriorente
  entrada = encontrar_entrada(laberinto)

  # Si el laberinto no es un valor incompatible con la función encontrar_entrada
  # decimos que la posición en primera instancia es la posición de la entrada
  if entrada is not None:
    pos = entrada

  # Si la el laberinto es incompatible con la función encontrar_entrada, retornamos None
  else:
    return None

  # Creamos una lista que será aquella que contenga los movimientos a hacer
  movimientos = ["Entrada"]

  # Definimos una variable de posición auxiliar como una posición inalcanzable
  # en el laberinto. Esta variable nos servirá luego para verificar si
  # la posición que estamos considerando no es la misma que teníamos antes
  pos_aux = [-1, -1]

  # Definimos la fila de la posición actual, que es el primer elemento de
  # la lista con la posición actual
  fila = pos[0]

  # Realizamos un tratamiento análogo para la columna de la posición actual
  columna = pos[1]

  # Recorremos el laberinto mientras no hayamos salido de él, esto es, que
  # el string "Salida" no esté en los movimientos ya hechos
  while "Salida" not in movimientos:

    # Definimos el largo de las filas y columnas del laberinto
    lar_filas = len(laberinto)
    lar_columnas = len(laberinto[0])

    # Definimos las condiciones que se deben cumplir para avanzar en el camino correcto
    # hacia cada una de las 4 direcciones (arriba, abajo, izquierda o derecha)

    # Si desde la posición actual debemos movernos hacia arriba para seguir
    # el camino correcto, significa que debemos restarle 1 a la fila (si es que
    # esta posición es posible en el tablero y si la posición que estamos verificando
    # no es aquella en la que estábamos antes). Es decir, el caracter en esta
    # posición debe ser el string "**" (que representa el camino correcto)
    cond_ar = fila - 1 >= 0 and laberinto[
        fila - 1][columna] == "**" and fila - 1 != pos_aux[0]

    # Si desde la posición actual debemos movernos hacia abajo para seguir
    # el camino correcto, significa que debemos sumarle 1 a la fila (si es que
    # esta posición es posible en el tablero y si la posición que estamos verificando
    # no es aquella en la que estábamos antes). Es decir, el caracter en esta
    # posición debe ser el string "**" (que representa el camino correcto)
    cond_ab = fila + 1 < lar_filas and laberinto[
        fila + 1][columna] == "**" and fila + 1 != pos_aux[0]

    # Si desde la posición actual debemos movernos hacia la derecha para seguir
    # el camino correcto, significa que debemos sumarle 1 a la columna (si es que
    # esta posición es posible en el tablero y si la posición que estamos verificando
    # no es aquella en la que estábamos antes). Es decir, el caracter en esta
    # posición debe ser el string "**" (que representa el camino correcto)
    cond_de = columna + 1 < lar_columnas and laberinto[fila][
        columna + 1] == "**" and columna + 1 != pos_aux[1]

    # Si desde la posición actual debemos movernos hacia la izquierda para seguir
    # el camino correcto, significa que debemos restarle 1 a la columna (si es que
    # esta posición es posible en el tablero y si la posición que estamos verificando
    # no es aquella en la que estábamos antes). Es decir, el caracter en esta
    # posición debe ser el string "**" (que representa el camino correcto)
    cond_iz = columna - 1 >= 0 and laberinto[fila][
        columna - 1] == "**" and columna - 1 != pos_aux[1]

    # Por otra parte, definimos las condiciones que se deben cumplir para avanzar hacia
    # cada una de las 4 direcciones (arriba, abajo, izquierda o derecha) si es que
    # la casilla a la que debemos avanzar es un portal, con un tratamiento similar

    # Si desde la posición actual debemos movernos hacia arriba para seguir
    # el camino correcto, significa que debemos restarle 1 a la fila (si es que
    # esta posición es posible en el tablero y si la posición que estamos verificando
    # no es aquella en la que estábamos antes). Es decir, el caracter en esta
    # posición debe ser el string "PP" (que representa un portal)
    cond_por_ar = fila - 1 >= 0 and laberinto[
        fila - 1][columna] == "PP" and fila - 1 != pos_aux[0]

    # Si desde la posición actual debemos movernos hacia abajo para seguir
    # el camino correcto, significa que debemos sumarle 1 a la fila (si es que
    # esta posición es posible en el tablero y si la posición que estamos verificando
    # no es aquella en la que estábamos antes). Es decir, el caracter en esta
    # posición debe ser el string "PP" (que representa un portal)
    cond_por_ab = fila + 1 < lar_filas and laberinto[
        fila + 1][columna] == "PP" and fila + 1 != pos_aux[0]

    # Si desde la posición actual debemos movernos hacia la derecha para seguir
    # el camino correcto, significa que debemos sumarle 1 a la columna (si es que
    # esta posición es posible en el tablero y si la posición que estamos verificando
    # no es aquella en la que estábamos antes). Es decir, el caracter en esta
    # posición debe ser el string "PP" (que representa un portal)
    cond_por_de = columna + 1 < lar_columnas and laberinto[fila][
        columna + 1] == "PP" and columna + 1 != pos_aux[1]

    # Si desde la posición actual debemos movernos hacia la izquierda para seguir
    # el camino correcto, significa que debemos restarle 1 a la columna (si es que
    # esta posición es posible en el tablero y si la posición que estamos verificando
    # no es aquella en la que estábamos antes). Es decir, el caracter en esta
    # posición debe ser el string "PP" (que representa un portal)
    cond_por_iz = columna - 1 >= 0 and laberinto[fila][
        columna - 1] == "PP" and columna - 1 != pos_aux[1]

    # Adicionalmente, definimos la condición que verificará si la casilla a la que
    # debemos avanzar es un portal en vez del string "**"
    cond_portal = (cond_por_ab or cond_por_ar or cond_por_de or cond_por_iz)

    # Si debemos movernos hacia arriba
    if cond_ar:

      # Guardamos la posición actual en la variable auxiliar de la posición para
      # verificar que la siguiente vez no retrocedamos sobre nuestros pasos
      pos_aux = pos

      # Agregamos el string "AR" (arriba) a los movimientos hechos
      movimientos += ["AR"]

      # Actualizamos la posición actual y la fila actual
      pos = [fila - 1, columna]
      fila -= 1

    # Por otra parte, si debemos movernos hacia abajo
    elif cond_ab:

      # Guardamos la posición actual en la variable auxiliar de la posición para
      # verificar que la siguiente vez no retrocedamos sobre nuestros pasos
      pos_aux = pos

      # Agregamos el string "AB" (abajo) a los movimientos hechos
      movimientos += ["AB"]

      # Actualizamos la posición actual y la fila actual
      pos = [fila + 1, columna]
      fila += 1

    # Por otra parte, si debemos movernos hacia la derecha
    elif cond_de:

      # Guardamos la posición actual en la variable auxiliar de la posición para
      # verificar que la siguiente vez no retrocedamos sobre nuestros pasos
      pos_aux = pos

      # Agregamos el string "DE" (derecha) a los movimientos hechos
      movimientos += ["DE"]

      # Actualizamos la posición actual y la columna actual
      pos = [fila, columna + 1]
      columna += 1

    # Por otra parte, si debemos movernos hacia la izquierda
    elif cond_iz:

      # Guardamos la posición actual en la variable auxiliar de la posición para
      # verificar que la siguiente vez no retrocedamos sobre nuestros pasos
      pos_aux = pos

      # Agregamos el string "IZ" (izquierda) a los movimientos hechos
      movimientos += ["IZ"]

      # Actualizamos la posición actual y la columna actual
      pos = [fila, columna - 1]
      columna -= 1

    # Por otra parte, si debemos movernos hacia un portal
    elif cond_portal:

      # Si ese portal está hacia abajo
      if cond_por_ab:

        # Agregamos los strings "AB" (abajo) y "PP" (portal) a los movimientos hechos
        movimientos += ["AB"]
        movimientos += ["Portal"]

        # Actualizamos la posición actual y la fila actual
        pos = [fila + 1, columna]

        # Guardamos la posición actual en la variable auxiliar de la posición de portales
        # para verificar que la siguiente vez no retrocedamos sobre nuestros pasos
        pos_aux_por = pos.copy()

        # Definimos índices para recorrer cada posición del laberinto con ciclos 'while'
        i = 0
        j = 0

        # Recorremos cada posición del laberinto con ciclos 'while'
        while i < len(laberinto):
          while j < len(laberinto[i]):

            # Definimos la condición para encontrar el portal de salida, esto es, que
            # la posición de la iteración actual contenga "PP" (un portal) y que no
            # sea el portal al cual entramos, es decir, la variable auxiliar de la
            # posición de portales
            cond_portal_salida = (laberinto[i][j] == "PP"
                                  and [i, j] != pos_aux_por)

            # Si la condición anterior pasa, debemos cambiar todas las variables de
            # posición para llegar al portal de salida
            if cond_portal_salida:
              fila = i
              columna = j
              pos = [i, j]

            # Por precaución, definimos la posición auxiliar (aquella que verificaba
            # que no estemos evaluando la misma posición de la cual veníamos) de vuelta
            # como una posición inalcanzable, puesto que al salir del portal esta
            # comparación es irrelevante
            pos_aux = [-1, -1]
            j += 1
          j = 0
          i += 1

      # Por otra parte, si ese portal está hacia arriba
      elif cond_por_ar:

        # Agregamos los strings "AR" (arriba) y "PP" (portal) a los movimientos hechos
        movimientos += ["AR"]
        movimientos += ["Portal"]

        # Actualizamos la posición actual y la fila actual
        pos = [fila - 1, columna]

        # Guardamos la posición actual en la variable auxiliar de la posición de portales
        # para verificar que la siguiente vez no retrocedamos sobre nuestros pasos
        pos_aux_por = pos.copy()

        # Definimos índices para recorrer cada posición del laberinto con ciclos 'while'
        i = 0
        j = 0

        # Recorremos cada posición del laberinto con ciclos 'while'
        while i < len(laberinto):
          while j < len(laberinto[i]):

            # Definimos la condición para encontrar el portal de salida, esto es, que
            # la posición de la iteración actual contenga "PP" (un portal) y que no
            # sea el portal al cual entramos, es decir, la variable auxiliar de la
            # posición de portales
            cond_portal_salida = (laberinto[i][j] == "PP"
                                  and [i, j] != pos_aux_por)

            # Si la condición anterior pasa, debemos cambiar todas las variables de
            # posición para llegar al portal de salida
            if cond_portal_salida:
              fila = i
              columna = j
              pos = [i, j]

            # Por precaución, definimos la posición auxiliar (aquella que verificaba
            # que no estemos evaluando la misma posición de la cual veníamos) de vuelta
            # como una posición inalcanzable, puesto que al salir del portal esta
            # comparación es irrelevante
            pos_aux = [-1, -1]
            j += 1
          j = 0
          i += 1

      # Por otra parte, si ese portal está hacia la derecha
      elif cond_por_de:

        # Agregamos los strings "DE" (derecha) y "PP" (portal) a los movimientos hechos
        movimientos += ["DE"]
        movimientos += ["Portal"]

        # Actualizamos la posición actual y la columna actual
        pos = [fila, columna + 1]

        # Guardamos la posición actual en la variable auxiliar de la posición de portales
        # para verificar que la siguiente vez no retrocedamos sobre nuestros pasos
        pos_aux_por = pos.copy()

        # Definimos índices para recorrer cada posición del laberinto con ciclos 'while'
        i = 0
        j = 0

        # Recorremos cada posición del laberinto con ciclos 'while'
        while i < len(laberinto):
          while j < len(laberinto[i]):

            # Definimos la condición para encontrar el portal de salida, esto es, que
            # la posición de la iteración actual contenga "PP" (un portal) y que no
            # sea el portal al cual entramos, es decir, la variable auxiliar de la
            # posición de portales
            cond_portal_salida = (laberinto[i][j] == "PP"
                                  and [i, j] != pos_aux_por)

            # Si la condición anterior pasa, debemos cambiar todas las variables de
            # posición para llegar al portal de salida
            if cond_portal_salida:
              fila = i
              columna = j
              pos = [i, j]

            # Por precaución, definimos la posición auxiliar (aquella que verificaba
            # que no estemos evaluando la misma posición de la cual veníamos) de vuelta
            # como una posición inalcanzable, puesto que al salir del portal esta
            # comparación es irrelevante
            pos_aux = [-1, -1]
            j += 1
          j = 0
          i += 1

      # Por otra parte, si ese portal está hacia la izquierda
      elif cond_por_iz:

        # Agregamos los strings "IZ" (izquierda) y "PP" (portal) a los movimientos hechos
        movimientos += ["IZ"]
        movimientos += ["Portal"]

        # Actualizamos la posición actual y la columna actual
        pos = [fila, columna - 1]

        # Guardamos la posición actual en la variable auxiliar de la posición de portales
        # para verificar que la siguiente vez no retrocedamos sobre nuestros pasos
        pos_aux_por = pos.copy()

        # Definimos índices para recorrer cada posición del laberinto con ciclos 'while'
        i = 0
        j = 0

        # Recorremos cada posición del laberinto con ciclos 'while'
        while i < len(laberinto):
          while j < len(laberinto[i]):

            # Definimos la condición para encontrar el portal de salida, esto es, que
            # la posición de la iteración actual contenga "PP" (un portal) y que no
            # sea el portal al cual entramos, es decir, la variable auxiliar de la
            # posición de portales
            cond_portal_salida = (laberinto[i][j] == "PP"
                                  and [i, j] != pos_aux_por)

            # Si la condición anterior pasa, debemos cambiar todas las variables de
            # posición para llegar al portal de salida
            if cond_portal_salida:
              fila = i
              columna = j
              pos = [i, j]

            # Por precaución, definimos la posición auxiliar (aquella que verificaba
            # que no estemos evaluando la misma posición de la cual veníamos) de vuelta
            # como una posición inalcanzable, puesto que al salir del portal esta
            # comparación es irrelevante
            pos_aux = [-1, -1]
            j += 1
          j = 0
          i += 1
        i = 0
        j = 0

    # Por último, si no encuentra el camino ni un portal, estamos en la salida
    else:

      # Si desde la posición actual debemos movernos hacia arriba para llegar
      # a la salida, significa que debemos restarle 1 a la fila (si es que
      # esta posición es posible en el tablero). Es decir, el caracter en esta
      # posición debe ser el string "SS" (que representa la salida)
      if fila - 1 >= 0 and laberinto[fila - 1][columna] == "SS":

        # Agregamos los strings "AR" (arriba) y "SS" (salida) a los movimientos hechos
        movimientos += ["AR"]
        movimientos += ["Salida"]

      # Por otra parte, si desde la posición actual debemos movernos hacia abajo
      # para llegar a la salida, significa que debemos sumarle 1 a la fila (si es que
      # esta posición es posible en el tablero). Es decir, el caracter en esta
      # posición debe ser el string "SS" (que representa la salida)
      elif fila + 1 < lar_filas and laberinto[fila + 1][columna] == "SS":

        # Agregamos los strings "AB" (abajo) y "SS" (salida) a los movimientos hechos
        movimientos += ["AB"]
        movimientos += ["Salida"]

      # Por otra parte, si desde la posición actual debemos movernos hacia la derecha
      # para llegar a la salida, significa que debemos sumarle 1 a la columna (si es que
      # esta posición es posible en el tablero). Es decir, el caracter en esta
      # posición debe ser el string "SS" (que representa la salida)
      elif columna + 1 < lar_columnas and laberinto[fila][columna + 1] == "SS":

        # Agregamos los strings "DE" (derecha) y "SS" (salida) a los movimientos hechos
        movimientos += ["DE"]
        movimientos += ["Salida"]

      # Por otra último, si no hallamos la salida en ninguna de las otras direcciones,
      # significa que debe estar a la izquierda, esto es, debemos restarle 1 a la
      # columna (si es que esta posición es posible en el tablero). Es decir, el
      # caracter en esta posición debe ser el string "SS" (que representa la salida)
      else:

        # Agregamos los strings "IZ" (izquierda) y "SS" (salida) a los movimientos hechos
        movimientos += ["IZ"]
        movimientos += ["Salida"]

  # Para finalizar, retornamos la lista de movimientos hechos desde la entrada
  # hasta la salida
  return movimientos
