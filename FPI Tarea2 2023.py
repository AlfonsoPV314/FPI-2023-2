# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA/FUNDAMENTOS DE COMPUTACIÓN Y PROGRAMACIÓN
# SECCIÓN DEL CURSO: 0-C-1 
# PROFESOR DE TEORÍA: CARLOS VERA 
# PROFESOR DE LABORATORIO: ANDRÉS MUÑOZ
#  
# AUTOR  
# NOMBRE: Alfonso Sebastian Palacios Vergara
# RUT: 21.775.623-5
# CARRERA: Ingeniería Civil Informática
#____________________________________________________________

# NOTA: Considere que las variables que son sólo una letra no poseen
# nombre representativo pues sólo representan itreadores en procesos 'while'
# o bien representan variables auxiliares puntuales.

#____________________________________________________________

# Definimos la primera función, que validará la posición en el tablero
def validar_posicion(pos,tablero):
  
  # Asignamos valores numéricos (posiciones) a las letras del
  # alfabeto, considerando que 0 es el primer elemento en Python
  LETRAS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  
  # Definimos la fila como el inverso aditivo del primer elemento
  # del input para que vaya "de abajo hacia arriba" en el tablero
  fila=(-1)*(int(pos[1]))
  
  # Definimos la columna como el número con la misma posición que la letra del input
  columna=LETRAS.index(pos[0].upper())
  
  # Verificamos los casos posibles y retornamos de manera acorde
  if columna>7 or fila>=0 or fila<-8:
    return(-1)
  elif tablero[fila][columna]=='  ':
    return(0)
  else:
    return(1)

#____________________________________________________________

# Luego, definimos la 2da función, que entregará el tablero según
# las piezas y posiciones de un input
def entregar_tablero(piezas):

  # Definimos el tablero inicial
  tablero = [['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']]

  # Al igual que en la funcion anterior, definimos constantes para
  # asignarle números a las letras
  LETRAS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  
  # Tomamos en cuenta las piezas válidas para el tablero
  PIEZAS_DISPONIBLES=["NP","NT","NC","NA","ND","NR", "BP", "BT", "BC", "BA", "BD", "BR"]

  # Separamos el input para crear una lista con las piezas ingresadas
  elemento = piezas.split(",")

  # Realizamos un ciclo 'while' que recorra la lista anterior
  i=0
  while i < len(elemento):

    # Definimos el elemento de la iteración actual
    elemento_iter = elemento[i]

    # Identificamos la pieza de la iteración
    pieza = elemento_iter[:2]

    # Identificamos la fila de la iteración
    fila_iter = int(elemento_iter[-1])

    # Identificamos la columna de la iteración
    columna_iter = elemento_iter[2]

    # Identificamos la fila en el tablero en la que irá esta pieza,
    # considerando que la fila_iter "1" es la fila "0" en el tablero
    fila_tablero = tablero[fila_iter - 1]

    # Definimos la columna en el tablero como el número con la
    # misma posición que la letra del input
    columna_tablero = LETRAS.index(columna_iter)

    # Verificamos si la pieza ingresada es válida y, de ser así, modificamos el tablero.
    # Luego, pasamos a la siguiente iteración
    if pieza in PIEZAS_DISPONIBLES and 0<=fila_iter<9 and 0<=columna_tablero<9 and fila_tablero[columna_tablero]=="  ":
      fila_tablero[columna_tablero] = pieza
    i = i + 1

  # Por último, retornamos el tablero modificado
  return(tablero[::-1])

#____________________________________________________________

# Una vez hecho esto, definimos la 3° función, que verificará si el tablero es válido
def es_valido(tablero):
  
  # Se definirán las variables de la función, incluyendo el número
  # de piezas blancas, negras y el tipo de las mismas para cada
  # color (y el índice del primer ciclo 'while'). Adicionalmente, creamos una
  # variable para guardar las posiciones de los alfiles, para
  # verificar su validez luego.
  i=0
  blancas=0
  negras=0
  rey_b=0
  rey_n=0
  caballos_b=0
  caballos_n=0
  torres_b=0
  torres_n=0
  alfiles_b=0
  alfiles_n=0
  peones_b=0
  peones_n=0
  reina_b=0
  reina_n=0
  pos_alfiles_b=[]
  pos_alfiles_n=[]

  # Mediante 2 ciclos 'while', recorreremos tanto las filas del
  # tablero como las posiciones en las mismas
  while i<len(tablero):
    j=0
    while j<len(tablero[i]):

      # Verificamos si es una pieza blanca y qué tipo de pieza es, aumentando 
      # la cantidad de las variables asociadas a esta cantidad
      if tablero[i][j][0]=="B":
        blancas+=1
        if tablero[i][j][1]=="C":
          caballos_b+=1
        elif tablero[i][j][1]=="T":
          torres_b+=1
        elif tablero[i][j][1]=="A":
          alfiles_b+=1

          # Guardamos la posición del alfil en la variable de
          # su color para verificar su validez más adelante.
          pos_alfiles_b=pos_alfiles_b+[i,j]
        elif tablero[i][j][1]=="P":
          peones_b+=1
          
          # Como caso especial, si los peones se encuentran en la
          # primera o última fila, retornamos 'False'
          if i==0 or i==7:
            return False
        elif tablero[i][j][1]=="D":
          reina_b+=1
        elif tablero[i][j][1]=="R":
          rey_b+=1
          
        # Si la pieza no cumple ninguna de las anteriores
        # características, retornamos 'False'
        else:
          return False
          
      # Realizamos el mismo tratamiento con las piezas negras
      elif tablero[i][j][0]=="N":
        negras+=1
        if tablero[i][j][1]=="C":
          caballos_n+=1
        elif tablero[i][j][1]=="T":
          torres_n+=1
        elif tablero[i][j][1]=="A":
          alfiles_n+=1
          pos_alfiles_n=pos_alfiles_n+[i,j]
        elif tablero[i][j][1]=="P":
          peones_n+=1
          if i==0 or i==7:
            return False
        elif tablero[i][j][1]=="D":
          reina_n+=1
        elif tablero[i][j][1]=="R":
          rey_n+=1
        else:
          return False
          
      # Luego, si la posición del tablero está vacía, no realizamos cambio alguno
      elif tablero[i][j][0]==" ":
        j=j

      # Por último, si la pieza no encaja en los casos anteriores, retornamos 'False'
      else:
        return False
        
      j+=1
    i+=1

  # Verificamos que la cantidad de piezas de ambos colores esté entre 0 y 16
  if 0<=blancas<17 and 0<=negras<17:

    # Verificamos que las piezas de cada color se repitan en
    # una cantidad válida. Creamos diferentes variables
    # para validar la cantidad de piezas individuales
    ca_valid=caballos_b<3 and caballos_n<3
    to_valid=torres_b<3 and torres_n<3
    al_valid=alfiles_b<3 and alfiles_n<3
    pe_valid=peones_b<9 and peones_n<9
    da_valid=reina_b<2 and reina_n<2
    re_valid=rey_b<2 and rey_n<2
    valido=ca_valid and to_valid and al_valid and pe_valid and da_valid and re_valid

    # Creamos dos variables extra, que nos servirán para
    # verificar si la posición de un alfil es válido.
    # Si hay 1 alfil en ambos colores, no sabemos qué alfil es, y por ende cualquier
    # posición que posea es válida. Pero, si hay 2 o más de un color o ambos, se
    # debe verificar que uno de ellos esté en una posición impar y
    # el otro en una posición par.

    # Verificamos lo anterior en el caso de que hayan 2 alfiles blancos y 1 negro
    if alfiles_n==2 and alfiles_b!=2:
      al_caso_a=pos_alfiles_n[0]%2==0 and pos_alfiles_n[1]%2==0
      al_caso_b=pos_alfiles_n[2]%2==0 and pos_alfiles_n[3]%2==0

      # Evaluamos si alguno de los casos creados anteriormente pasan.
      # Si esto es así, la posición de uno o más alfiles es inválida y
      # retornamos 'False'
      if al_caso_a or al_caso_b:
        return False

      # Si hay dos o más alfiles de este color en el tablero pero sus
      # posiciones son válidas, y la cantidad de piezas
      # es válida, retornamos 'True'
      elif valido:
        return valido

      # En otro caso, retornanos 'False'
      else:
        return False

    # Realizamos el mismo procedimiento para el caso en el que hayan
    # 2 alfiles blancos y 1 negro
    elif alfiles_b==2 and alfiles_n!=2:
      al_caso_c=pos_alfiles_b[0]%2==0 and pos_alfiles_b[1]%2==0
      al_caso_d=pos_alfiles_b[2]%2==0 and pos_alfiles_b[3]%2==0
      if al_caso_c or al_caso_d:
        return False
      elif valido:
        return valido
      else:
        return False

    # Realizamos el mismo procedimiento para el caso en el que hayan
    # 2 alfiles de cada color, considerando todas las variables anteriores.
    elif alfiles_b==2 and alfiles_n==2:
      al_caso_a=pos_alfiles_b[0]%2==0 and pos_alfiles_b[1]%2==0
      al_caso_b=pos_alfiles_b[2]%2==0 and pos_alfiles_b[3]%2==0
      al_caso_c=pos_alfiles_n[0]%2==0 and pos_alfiles_n[1]%2==0
      al_caso_d=pos_alfiles_n[2]%2==0 and pos_alfiles_n[3]%2==0
      if al_caso_a or al_caso_b or al_caso_c or al_caso_d:
        return False
      elif valido:
        return valido
      else:
        return False

    # Si no hay 2 alfiles se al menos 1 color ej el tablero y la
    # cantidad de las piezas es válida, retornamos 'True'
    elif valido:
      return valido

    # En otro caso, retornamos 'False'
    else:
      return False
  
  # Para finalizar, si nada de lo anterior se cumple, retornamos 'False'
  else:
      return False

#____________________________________________________________

# Finalmente, procedemos a definir la última función, que
# verificará si hay cero, uno o más reyes amenazados
def hay_jaque(tablero):

  # En primera instancia, definimos las variables de
  # 2 ciclos 'while' que recorrerán las posiciones de las
  # filas con el objetivo de encontrar las posiciones de los reyes.
  i=0
  j=0
  pos_rey_b=[0,0]
  pos_rey_n=[0,0]

  # Recorremos las posiciones del tablero guardando las posiciones
  # de cada rey. Estas son guardadas con las especificaciones del tablero.
  while i<len(tablero):
    while j<len(tablero[i]):
      if tablero[i][j][1]=="R":
        if tablero[i][j][0]=="B":
          pos_rey_b=[8-i,j+1]
        else:
          pos_rey_n=[8-i,j+1]
      j+=1
    j=0
    i+=1

  # Definimos los iteradores y variables para comprobar si
  # algún rey está amenazado en el siguiente par de ciclos 'while'
  k=0
  l=0
  amenaza_rey_b=False
  amenaza_rey_n=False

  # Los ciclos 'while' a continuación recorren, primero, las
  # filas del tablero y, segundo, las columnas de esa fila
  while k<len(tablero):
    while l<len(tablero[k]):

      # Guardamos la posición de la pieza en una variable
      # considerando las especificaciones de un tablero
      # de ajedrez (de 1 a 8, abajo a arriba e izq a der)
      pos_pieza=[8-k,l+1]

      # Si la pieza es negra, creamos las variables de su
      # fila, su columna, un índice para un ciclo 'while'
      # y una variable auxiliar 'p'
      if tablero[k][l][0]=="N":
        m=0
        n=pos_pieza[0]
        o=pos_pieza[1]
        p=1

        # Realizamos las condiciones, para cada pieza, de
        # todos los casos en los que esta pieza negra
        # amenaza al rey blanco.
        while m<len(tablero):

          # Creamos una variable booleana auxiliar para verificar
          # si hay alguna pieza entre la pieza de la iteración
          # y el rey blanco
          aux=True

          # Las condiciones de los alfiles
          cond_alfil_1=pos_pieza[0]+m==pos_rey_b[0] and pos_pieza[1]+m==pos_rey_b[1]
          cond_alfil_2=pos_pieza[0]+m==pos_rey_b[0] and pos_pieza[1]-m==pos_rey_b[1]
          cond_alfil_3=pos_pieza[0]-m==pos_rey_b[0] and pos_pieza[1]+m==pos_rey_b[1]
          cond_alfil_4=pos_pieza[0]-m==pos_rey_b[0] and pos_pieza[1]-m==pos_rey_b[1]

          # Las condiciones de las torres
          cond_torre_1=pos_pieza[1]==pos_rey_b[1]
          cond_torre_1a=pos_pieza[0]+m==pos_rey_b[0]
          cond_torre_1b=pos_pieza[0]-m==pos_rey_b[0]
          cond_torre_2=pos_pieza[0]==pos_rey_b[0]
          cond_torre_2a=pos_pieza[1]+m==pos_rey_b[1]
          cond_torre_2b=pos_pieza[1]-m==pos_rey_b[1]

          # Las condiciones de los peones
          cond_peon_1=pos_pieza[0]-1==pos_rey_b[0]
          cond_peon_2=pos_pieza[1]+1==pos_rey_b[1]
          cond_peon_3=pos_pieza[1]-1==pos_rey_b[1]

          # Las condiciones de los caballos
          cond_caballo_1=pos_pieza[0]+2==pos_rey_b[0]
          cond_caballo_2=pos_pieza[0]+1==pos_rey_b[0]
          cond_caballo_3=pos_pieza[0]-2==pos_rey_b[0]
          cond_caballo_4=pos_pieza[0]-1==pos_rey_b[0]
          cond_caballo_a=pos_pieza[1]+2==pos_rey_b[1]
          cond_caballo_b=pos_pieza[1]+1==pos_rey_b[1]
          cond_caballo_c=pos_pieza[1]-2==pos_rey_b[1]
          cond_caballo_d=pos_pieza[1]-1==pos_rey_b[1]
          cond_caballo_d=pos_pieza[1]-1==pos_rey_b[1]

          # Adicionalmente, acortamos las variables stackeándolas
          cond_caballo_final_1=(cond_caballo_1 or cond_caballo_3) and (cond_caballo_b or cond_caballo_d)
          cond_caballo_final_2=(cond_caballo_2 or cond_caballo_4) and (cond_caballo_a or cond_caballo_c)
          cond_caballo_final=cond_caballo_final_1 or cond_caballo_final_2

          # Las condiciones del rey
          cond_rey_1=pos_pieza[1]+1==pos_rey_b[1]
          cond_rey_2=pos_pieza[1]-1==pos_rey_b[1]
          cond_rey_3=pos_pieza[0]+1==pos_rey_b[0]
          cond_rey_4=pos_pieza[0]-1==pos_rey_b[0]

          # Adicionalmente, acortamos las varianles stackeándolas
          cond_rey_final=(cond_rey_1 or cond_rey_2) and (cond_rey_3 or cond_rey_4)

          # Si la pieza es un alfil
          if tablero[k][l][1]=="A":

            # Si (potencialmente) amenaza al rey por la condición 1
            # (el rey está en diagonal hacia arriba y derecha)
            if cond_alfil_1:

              # Verificamos que no haya ninguna pieza entre
              # el alfil y el rey. Si es así, 'aux'
              # se vuelve false
              while n<pos_rey_b[0]-1 and o<pos_rey_b[1]-1:
                if tablero[-1*(pos_pieza[0]+p)][pos_pieza[1]+p-1]!="  ":
                  aux=False
                n+=1
                o+=1
                p+=1

              # Si 'aux' no se convirtió en falso, esto es, si
              # no hay piezas entre el alfil y el rey, el rey está amenazado
              if aux:
                amenaza_rey_b=True

            # Si (potencialmente) amenaza al rey por la condición 2
            # (el rey está en diagonal hacia arriba e izquierda)
            # realizamos un procedimiento análogo al anterior para la condición 2
            elif cond_alfil_2:
              while n<pos_rey_b[0]-1 and o>pos_rey_b[1]+1:
                if tablero[-1*(pos_pieza[0]+p)][pos_pieza[1]-p-1]!="  ":
                  aux=False
                n+=1
                o-=1
                p+=1
              if aux:
                amenaza_rey_b=True

            # Si (potencialmente) amenaza al rey por la condición 3
            # (el rey está en diagonal hacia abajo y derecha)
            # realizamos un procedimiento análogo al anterior para la condición 3
            elif cond_alfil_3:
              while n>pos_rey_b[0]+1 and o<pos_rey_b[1]-1:
                if tablero[-1*(pos_pieza[0]-p)][pos_pieza[1]+p-1]!="  ":
                  aux=False
                n-=1
                o+=1
                p+=1
              if aux:
                amenaza_rey_b=True

            # Si (potencialmente) amenaza al rey por la condición 4
            # (el rey está en diagonal hacia abajo e izquierda)
            # realizamos un procedimiento análogo al anterior para la condición 4
            elif cond_alfil_4:
              while n>pos_rey_b[0]+1 and o>pos_rey_b[1]+1:
                if tablero[-1*(pos_pieza[0]-p)][pos_pieza[1]-p-1]!="  ":
                  aux=False
                n-=1
                o-=1
                p+=1
              if aux:
                amenaza_rey_b=True

          # Si la pieza es una torre
          elif tablero[k][l][1]=="T":

            # Si (potencialmente) amenaza al rey por la condición 1
            # (la torre y el rey están en la misma columna)
            # y la condición 1a (el rey está arriba de la torre)
            if cond_torre_1 and cond_torre_1a:

              # Verificamos que no haya ninguna pieza entre
              # la torre y el rey. Si es así, 'aux'
              # se vuelve false
              while n<pos_rey_b[0]-1:
                if tablero[-1*(pos_pieza[0]+p)][pos_pieza[1]-1]!="  ":
                  aux=False
                n+=1
                p+=1

              # Si 'aux' no se convirtió en falso, esto es, si
              # no hay piezas entre la torre y el rey, el rey está amenazado
              if aux:
                amenaza_rey_b=True

            # Si (potencialmente) amenaza al rey por la condición 1
            # (la torre y el rey están en la misma columna)
            # y la condición 1b (el rey está abajo de la torre)
            # realizamos un procedimiento análogo al anterior para la condición 1b
            elif cond_torre_1 and cond_torre_1b:
              while n>pos_rey_b[0]+1:
                if tablero[-1*(pos_pieza[0]-p)][pos_pieza[1]-1]!="  ":
                  aux=False
                n-=1
                p+=1
              if aux:
                amenaza_rey_b=True

            # Si (potencialmente) amenaza al rey por la condición 2
            # (la torre y el rey están en la misma fila)
            # y la condición 2a (el rey está a la derecha de la torre)
            # realizamos un procedimiento análogo al anterior para las condciones 2 y 2a
            elif cond_torre_2 and cond_torre_2a:
              while o<pos_rey_b[1]-1:
                if tablero[-1*pos_pieza[0]][pos_pieza[1]+p-1]!="  ":
                  aux=False
                o+=1
                p+=1
              if aux:
                amenaza_rey_b=True

            # Si (potencialmente) amenaza al rey por la condición 2
            # (la torre y el rey están en la misma fila)
            # y la condición 2b (el rey está a la izquierda de la torre)
            # realizamos un procedimiento análogo al anterior para la condición 2b
            elif cond_torre_2 and cond_torre_2b:
              while o>pos_rey_b[1]+1:
                if tablero[-1*pos_pieza[0]][pos_pieza[1]-p-1]!="  ":
                  aux=False
                o-=1
                p+=1
              if aux:
                amenaza_rey_b=True

          # Si la pieza es un peón
          elif tablero[k][l][1]=="P":

            # Si el peón está en la misma columna que el rey
            # (cond1) y el rey está directamente en las casillas
            # diagonales al peón (considerando su color)
            # entonces el rey está amenazado
            if (cond_peon_1 and cond_peon_2) or (cond_peon_1 and cond_peon_3):
              amenaza_rey_b=True

          # Si la pieza es un caballo
          elif tablero[k][l][1]=="C":

            # Si el rey está en el rango del caballo, está en peligro
            if cond_caballo_final:
              amenaza_rey_b=True

          # Si la pieza es una dama, se verifica si se cumple
          # alguna de las condiciones de torres o alfiles.
          # Veanse los comentarios de alfiles y/o torres
          elif tablero[k][l][1]=="D":
            if cond_alfil_1:
              while n<pos_rey_b[0]-1 and o<pos_rey_b[1]-1:
                if tablero[-1*(pos_pieza[0]+p)][pos_pieza[1]+p-1]!="  ":
                  aux=False
                n+=1
                o+=1
                p+=1
              if aux:
                amenaza_rey_b=True
            elif cond_alfil_2:
              while n<pos_rey_b[0]-1 and o>pos_rey_b[1]+1:
                if tablero[-1*(pos_pieza[0]+p)][pos_pieza[1]-p-1]!="  ":
                  aux=False
                n+=1
                o-=1
                p+=1
              if aux:
                amenaza_rey_b=True
            elif cond_alfil_3:
              while n>pos_rey_b[0]+1 and o<pos_rey_b[1]-1:
                if tablero[-1*(pos_pieza[0]-p)][pos_pieza[1]+p-1]!="  ":
                  aux=False
                n-=1
                o+=1
                p+=1
              if aux:
                amenaza_rey_b=True
            elif cond_alfil_4:
              while n>pos_rey_b[0]+1 and o>pos_rey_b[1]+1:
                if tablero[-1*(pos_pieza[0]-p)][pos_pieza[1]-p-1]!="  ":
                  aux=False
                n-=1
                o-=1
                p+=1
              if aux:
                amenaza_rey_b=True
            elif cond_torre_1 and cond_torre_1a:
              while n<pos_rey_b[0]-1:
                if tablero[-1*(pos_pieza[0]+p)][pos_pieza[1]-1]!="  ":
                  aux=False
                n+=1
                p+=1
              if aux:
                amenaza_rey_b=True
            elif cond_torre_1 and cond_torre_1b:
              while n>pos_rey_b[0]+1:
                if tablero[-1*(pos_pieza[0]-p)][pos_pieza[1]-1]!="  ":
                  aux=False
                n-=1
                p+=1
              if aux:
                amenaza_rey_b=True
            elif cond_torre_2 and cond_torre_2a:
              while o<pos_rey_b[1]-1:
                if tablero[-1*pos_pieza[0]][pos_pieza[1]+p-1]!="  ":
                  aux=False
                o+=1
                p+=1
              if aux:
                amenaza_rey_b=True
            elif cond_torre_2 and cond_torre_2b:
              while o>pos_rey_b[1]+1:
                if tablero[-1*pos_pieza[0]][pos_pieza[1]-p-1]!="  ":
                  aux=False
                o-=1
                p+=1
              if aux:
                amenaza_rey_b=True

            # Por último, si la pieza es un rey, y si el otro
            # rey está en su alcance, como no podemos saber
            # el turno siguiente ni a que color le toca, concluimos
            # que ambos están en jaque
            elif tablero[k][l][1]=="R" and cond_rey_final:
              amenaza_rey_n=True
              amenaza_rey_b=True
          m+=1

      # De la misma forma, si la pieza es de color blanco, se
      # realizará un proceso análogo para estas piezas
      # (considerando al rey negro en vez del blanco).
      # Por ende, se repetirán los comentarios.
      else:
        m=0
        n=pos_pieza[0]
        o=pos_pieza[1]
        p=1

        # Realizamos las condiciones, para cada pieza, de
        # todos los casos en los que esta pieza negra
        # amenaza al rey blanco
        while m<len(tablero):
          
          # Creamos una variable booleana auxiliar para verificar
          # si hay alguna pieza entre la pieza de la iteración
          # y el rey blanco
          aux=True

          # Las condiciones de los alfiles
          cond_alfil_1=pos_pieza[0]+m==pos_rey_n[0] and pos_pieza[1]+m==pos_rey_n[1]
          cond_alfil_2=pos_pieza[0]+m==pos_rey_n[0] and pos_pieza[1]-m==pos_rey_n[1]
          cond_alfil_3=pos_pieza[0]-m==pos_rey_n[0] and pos_pieza[1]+m==pos_rey_n[1]
          cond_alfil_4=pos_pieza[0]-m==pos_rey_n[0] and pos_pieza[1]-m==pos_rey_n[1]

          # Las condiciones de las torres
          cond_torre_1=pos_pieza[1]==pos_rey_n[1]
          cond_torre_1a=pos_pieza[0]+m==pos_rey_n[0]
          cond_torre_1b=pos_pieza[0]-m==pos_rey_n[0]
          cond_torre_2=pos_pieza[0]==pos_rey_n[0]
          cond_torre_2a=pos_pieza[1]+m==pos_rey_n[1]
          cond_torre_2b=pos_pieza[1]-m==pos_rey_n[1]

          # Las condiciones de los peones
          cond_peon_1=pos_pieza[0]+1==pos_rey_n[0]
          cond_peon_2=pos_pieza[1]+1==pos_rey_n[1]
          cond_peon_3=pos_pieza[1]-1==pos_rey_n[1]

          # Las condiciones de los caballos
          cond_caballo_1=pos_pieza[0]+2==pos_rey_n[0]
          cond_caballo_2=pos_pieza[0]+1==pos_rey_n[0]
          cond_caballo_3=pos_pieza[0]-2==pos_rey_n[0]
          cond_caballo_4=pos_pieza[0]-1==pos_rey_n[0]
          cond_caballo_a=pos_pieza[1]+2==pos_rey_n[1]
          cond_caballo_b=pos_pieza[1]+1==pos_rey_n[1]
          cond_caballo_c=pos_pieza[1]-2==pos_rey_n[1]
          cond_caballo_d=pos_pieza[1]-1==pos_rey_n[1]

          # Adicionalmente, acortamos las variables stackeándolas
          cond_caballo_final_1=(cond_caballo_1 or cond_caballo_3) and (cond_caballo_b or cond_caballo_d)
          cond_caballo_final_2=(cond_caballo_2 or cond_caballo_4) and (cond_caballo_a or cond_caballo_c)
          cond_caballo_final=cond_caballo_final_1 or cond_caballo_final_2

          # Las condiciones del rey
          cond_rey_1=pos_pieza[1]+1==pos_rey_n[1]
          cond_rey_2=pos_pieza[1]-1==pos_rey_n[1]
          cond_rey_3=pos_pieza[0]+1==pos_rey_n[0]
          cond_rey_4=pos_pieza[0]-1==pos_rey_n[0]

          # Adicionalmente, acortamos las variables stackeándolas
          cond_rey_final=(cond_rey_1 or cond_rey_2) and (cond_rey_3 or cond_rey_4)

          # Si la pieza es un alfil
          if tablero[k][l][1]=="A":

            # Si (potencialmente) amenaza al rey por la condición 1
            # (el rey está en diagonal hacia arriba y derecha)
            if cond_alfil_1:

              # Verificamos que no haya ninguna pieza entre
              # el alfil y el rey. Si es así, 'aux'
              # se vuelve false
              while n<pos_rey_n[0]-1 and o<pos_rey_n[1]-1:
                if tablero[-1*(pos_pieza[0]+p)][pos_pieza[1]+p-1]!="  ":
                  aux=False
                n+=1
                o+=1
                p+=1

              # Si 'aux' no se convirtió en falso, esto es, si
              # no hay piezas entre el alfil y el rey, el rey está amenazado
              if aux:
                amenaza_rey_n=True

            # Si (potencialmente) amenaza al rey por la condición 2
            # (el rey está en diagonal hacia arriba e izquierda)
            # realizamos un procedimiento análogo al anterior para la condición 2
            elif cond_alfil_2:
              while n<pos_rey_n[0]-1 and o>pos_rey_n[1]+1:
                if tablero[-1*(pos_pieza[0]+p)][pos_pieza[1]-p-1]!="  ":
                  aux=False
                n+=1
                o-=1
                p+=1
              if aux:
                amenaza_rey_n=True

            # Si (potencialmente) amenaza al rey por la condición 3
            # (el rey está en diagonal hacia abajo y derecha)
            # realizamos un procedimiento análogo al anterior para la condición 2
            elif cond_alfil_3:
              while n>pos_rey_n[0]+1 and o<pos_rey_n[1]-1:
                if tablero[-1*(pos_pieza[0]-p)][pos_pieza[1]+p-1]!="  ":
                  aux=False
                n-=1
                o+=1
                p+=1
              if aux:
                amenaza_rey_n=True

            # Si (potencialmente) amenaza al rey por la condición 4
            # (el rey está en diagonal hacia abajo e izquierda)
            # realizamos un procedimiento análogo al anterior para la condición 4
            elif cond_alfil_4:
              while n>pos_rey_n[0]+1 and o>pos_rey_n[1]+1:
                if tablero[-1*(pos_pieza[0]-p)][pos_pieza[1]-p-1]!="  ":
                  aux=False
                n-=1
                o-=1
                p+=1
              if aux:
                amenaza_rey_n=True

          # Si la pieza es una torre
          elif tablero[k][l][1]=="T":

            # Si (potencialmente) amenaza al rey por la condición 1
            # (la torre y el rey están en la misma columna)
            # y la condición 1a (el rey está arriba de la torre)
            if cond_torre_1 and cond_torre_1a:

              # Verificamos que no haya ninguna pieza entre
              # la torre y el rey. Si es así, 'aux'
              # se vuelve false
              while n<pos_rey_n[0]-1:
                if tablero[-1*(pos_pieza[0]+p)][pos_pieza[1]-1]!="  ":
                  aux=False
                n+=1
                p+=1

              # Si 'aux' no se convirtió en falso, esto es, si
              # no hay piezas entre la torre y el rey, el rey está amenazado
              if aux:
                amenaza_rey_n=True

            # Si (potencialmente) amenaza al rey por la condición 1
            # (la torre y el rey están en la misma columna)
            # y la condición 1b (el rey está abajo de la torre)
            # realizamos un procedimiento análogo al anterior para la condición 1b
            elif cond_torre_1 and cond_torre_1b:
              while n>pos_rey_n[0]+1:
                if tablero[-1*(pos_pieza[0]-p)][pos_pieza[1]-1]!="  ":
                  aux=False
                n-=1
                p+=1
              if aux:
                amenaza_rey_n=True

            # Si (potencialmente) amenaza al rey por la condición 2
            # (la torre y el rey están en la misma fila)
            # y la condición 2a (el rey está a la derecha de la torre)
            # realizamos un procedimiento análogo al anterior para las condciones 2 y 2a
            elif cond_torre_2 and cond_torre_2a:
              while o<pos_rey_n[1]-1:
                if tablero[-1*pos_pieza[0]][pos_pieza[1]+p-1]!="  ":
                  aux=False
                o+=1
                p+=1
              if aux:
                amenaza_rey_n=True

            # Si (potencialmente) amenaza al rey por la condición 2
            # (la torre y el rey están en la misma fila)
            # y la condición 2b (el rey está a la izquierda de la torre)
            # realizamos un procedimiento análogo al anterior para la condición 2b
            elif cond_torre_2 and cond_torre_2b:
              while o>pos_rey_n[1]+1:
                if tablero[-1*pos_pieza[0]][pos_pieza[1]-p-1]!="  ":
                  aux=False
                o-=1
                p+=1
              if aux:
                amenaza_rey_n=True

          # Si la pieza es un peón
          elif tablero[k][l][1]=="P":

            # Si el peón está en la misma columna que el rey
            # (cond1) y el rey está directamente en las casillas
            # diagonales al peón (considerando su color)
            # entonces el rey está amenazado
            if (cond_peon_1 and cond_peon_2) or (cond_peon_1 and cond_peon_3):
              amenaza_rey_n=True

          # Si la pieza es un caballo
          elif tablero[k][l][1]=="C":

            # Si el rey está en el rango del caballo, está en peligro
            if cond_caballo_final:
              amenaza_rey_n=True

          # Si la pieza es una dama, se verifica si se cumple
          # alguna de las condiciones de torres o alfiles.
          # Veanse los comentarios de alfiles y/o torres
          elif tablero[k][l][1]=="D":
            if cond_alfil_1:
              while n<pos_rey_n[0]-1 and o<pos_rey_n[1]-1:
                if tablero[-1*(pos_pieza[0]+p)][pos_pieza[1]+p-1]!="  ":
                  aux=False
                n+=1
                o+=1
                p+=1
              if aux:
                amenaza_rey_n=True
            elif cond_alfil_2:
              while n<pos_rey_n[0]-1 and o>pos_rey_n[1]+1:
                if tablero[-1*(pos_pieza[0]+p)][pos_pieza[1]-p-1]!="  ":
                  aux=False
                n+=1
                o-=1
                p+=1
              if aux:
                amenaza_rey_n=True
            elif cond_alfil_3:
              while n>pos_rey_n[0]+1 and o<pos_rey_n[1]-1:
                if tablero[-1*(pos_pieza[0]-p)][pos_pieza[1]+p-1]!="  ":
                  aux=False
                n-=1
                o+=1
                p+=1
              if aux:
                amenaza_rey_n=True
            elif cond_alfil_4:
              while n>pos_rey_n[0]+1 and o>pos_rey_n[1]+1:
                if tablero[-1*(pos_pieza[0]-p)][pos_pieza[1]-p-1]!="  ":
                  aux=False
                n-=1
                o-=1
                p+=1
              if aux:
                amenaza_rey_n=True
            elif cond_torre_1 and cond_torre_1a:
              while n<pos_rey_n[0]-1:
                if tablero[-1*(pos_pieza[0]+p)][pos_pieza[1]-1]!="  ":
                  aux=False
                n+=1
                p+=1
              if aux:
                amenaza_rey_n=True
            elif cond_torre_1 and cond_torre_1b:
              while n>pos_rey_n[0]+1:
                if tablero[-1*(pos_pieza[0]-p)][pos_pieza[1]-1]!="  ":
                  aux=False
                n-=1
                p+=1
              if aux:
                amenaza_rey_n=True
            elif cond_torre_2 and cond_torre_2a:
              while o<pos_rey_n[1]-1:
                if tablero[-1*pos_pieza[0]][pos_pieza[1]+p-1]!="  ":
                  aux=False
                o+=1
                p+=1
              if aux:
                amenaza_rey_n=True
            elif cond_torre_2 and cond_torre_2b:
              while o>pos_rey_n[1]+1:
                if tablero[-1*pos_pieza[0]][pos_pieza[1]-p-1]!="  ":
                  aux=False
                o-=1
                p+=1
              if aux:
                amenaza_rey_n=True
          elif tablero[k][l][1]=="R"and cond_rey_final:
            amenaza_rey_n=True
            amenaza_rey_b=True

          # Se procede a realizar las operaciones necesarias
          # para el ciclo 'while'
          m+=1
      l+=1
    l=0
    k+=1

  # Por último, luego de encontrar el "estado de jaque"
  # de cada rey, se procede a evaluar en qué caso se
  # encuentra y se definen las salidas de manera acorde
  # con lo pedido.
  if amenaza_rey_n and not amenaza_rey_b:
    return 1
  elif amenaza_rey_b and not amenaza_rey_n:
    return 0
  elif amenaza_rey_n and amenaza_rey_b:
    return 2
  else:
    return -1