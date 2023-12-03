# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA/FUNDAMENTOS DE COMPUTACIÓN Y PROGRAMACIÓN
# SECCIÓN DEL CURSO: 0-C-1
# PROFESOR DE TEORÍA: CARLOS VERA
# PROFESOR DE LABORATORIO:  ANDRÉS MUÑOZ
#
# AUTOR
# NOMBRE: Alfonso Sebastián Palacios Vergara
# RUT: 21.775.623-5
# CARRERA: Ingeniería Civil Informática

#____________________________________________________________
# PARTE 1:

# Considere que 'presel' significa 'preseleccionados' (que se refiere al periodo anterior a la selección de los participantes en función de su fuerza medida), 'sel' significa 'seleccionados', 'partic' significa 'participantes', 'pod' significa 'poder', las variables que son sólo 1 letra sirven simplemente como índices para procesos 'while', y las variables 'aux' son simplemente variables auxiliares en estos mismos procesos.

# ENTRADAS:

# Los 2 primeros input son la cantidad de participantes de preselección y la cantidad de cupos.
cant_presel = int(input())
cant_cupos = int(input())

# El siguiente procedimiento toma los input (en una lista) de los nombres de los participantes y su fuerza medida
stop1 = False
i = 0
partic_presel = []
while not stop1:
  if i > cant_presel - 1:
    stop1 = True
  else:
    partic_presel = partic_presel + [input()]
  i = i + 1

# Y por último, se recibe el input de los números del sorteo
nums_partic = [input()]

# VARIABLES E ÍNDICES 1:

j = 0
k = 0
n = 0
m = 0
l = 1
p = 0
t = 0
b = 0
fuerza_max = 0
partic_sel = []
pod_partic_sel = []

# PROCESAMIENTO 1:

# Se separan los nombres de los participantes de los números de su fuerza medida
partic_presel = ",".join(partic_presel)
partic_presel = partic_presel.split(",")

# Se le hace el mismo tratamiento a los números obtenidos por los participantes en el sorteo
nums_partic = ",".join(nums_partic)
nums_partic = nums_partic.split(",")

# Luego, convertimos a los strings con los números del sorteo elegidos por los participantes a int
while t < len(nums_partic):
  nums_partic[t] = int(nums_partic[t])
  t = t + 1

# Guardamos una copia de la lista original de los participantes de la preselección
lista_original_presel = partic_presel
lista_original_presel = ",".join(lista_original_presel)
lista_original_presel = lista_original_presel.split(",")

# El siguiente procedimiento encuentra el valor máximo de la fuerza de los participantes medida por la máquina
while b < len(partic_presel):
  if partic_presel[b].isdigit():
    if int(partic_presel[b]) > int(fuerza_max):
      fuerza_max = int(partic_presel[b])
  b = b + 1

# El siguiente procedimiento ordena de menor a mayor los participantes (y su poder medido) según su poder medido
largo_partic_presel = len(partic_presel)
while j <= largo_partic_presel:
  while (2 * k) + 3 <= largo_partic_presel - j:
    if partic_presel[(2 * k) + 1] == "MAQUINA DESTRUIDA":
      partic_presel[(2 * k) + 1] = fuerza_max + 1
    elif partic_presel[(2 * k) + 3] == "MAQUINA DESTRUIDA":
      partic_presel[(2 * k) + 3] = fuerza_max + 1
    if int(partic_presel[(2 * k) + 1]) > int(partic_presel[(2 * k) + 3]):
      aux1 = partic_presel[(2 * k)]
      partic_presel[(2 * k)] = partic_presel[(2 * k) + 2]
      partic_presel[(2 * k) + 2] = aux1
      aux2 = partic_presel[(2 * k + 1)]
      partic_presel[(2 * k) + 1] = partic_presel[(2 * k) + 3]
      partic_presel[(2 * k) + 3] = aux2
    k = k + 1
  j = j + 1
  k = 0

# El siguiente procedimiento ordena, si el poder de 2 participantes es igual, a los mismos según el orden en el cual se sometieron al test de fuerza
while n <= largo_partic_presel:
  while (2 * m) + 3 <= largo_partic_presel:
    if partic_presel[(2 * m) + 1] == partic_presel[(2 * m) + 3]:
      posicion1 = lista_original_presel.index(partic_presel[2 * m])
      posicion2 = lista_original_presel.index(partic_presel[(2 * m) + 2])
      if posicion1 < posicion2:
        aux3 = partic_presel[(2 * m) + 2]
        partic_presel[(2 * m) + 2] = partic_presel[(2 * m)]
        partic_presel[(2 * m)] = aux3
    m = m + 1
  n = n + 1
  m = 0

# SALIDAS 1:

print("Y los participantes seleccionados son:")

# El siguiente procedimiento verifica que el programa presente aquellos participantes que quedaron en los cupos (los que están de últimos en la lista partic_presel)
while p < cant_cupos:
  partic_sel = partic_sel + [partic_presel[largo_partic_presel - (2 * l)]]
  pod_partic_sel = pod_partic_sel + [
    partic_presel[largo_partic_presel - (2 * l - 1)]
  ]
  print(partic_presel[largo_partic_presel - (2 * l)])
  l = l + 1
  p = p + 1

#____________________________________________________________
# PARTE 2:

# VARIABLES E ÍNDICES 2:

partic_sel
nums_partic
q = 0
r = 0
s = 0
combates = []

# PROCESAMIENTO:

largo_partic_sel = len(partic_sel)
print("\nYa tenemos los combates!!!!!")

# El siguiente procedimiento cambia las posiciones de los participantes en función de los números que eligieron para el sorteo, ordenando a su vez a los susodichos números de menor a mayor
while q <= largo_partic_sel:
  while r + 1 <= largo_partic_sel - 1:
    if nums_partic[r] > nums_partic[r + 1]:
      aux4 = nums_partic[r]
      aux5 = partic_sel[r]
      nums_partic[r] = nums_partic[r + 1]
      partic_sel[r] = partic_sel[r + 1]
      nums_partic[r + 1] = aux4
      partic_sel[r + 1] = aux5
    r = r + 1
  q = q + 1
  r = 0

# SALIDAS:

while s + 1 <= largo_partic_sel - 1:
  combates = combates + [partic_sel[s], partic_sel[s + 1]]
  print(partic_sel[s], "vs", partic_sel[s + 1])
  s = s + 2

#____________________________________________________________
# PARTE 3:

# VARIABLES E ÍNDICES 3:

largo_partic_sel
partic_sel
v = 0
pod_oculto_partic = []
u = 0
y = 0
z = 0
largo_budokai_tenkaichi = largo_partic_sel

# PROCESAMIENTO:

print("\nY se lleva a cabo el torneo:")

# El siguiente proceso calcula los poderes ocultos de los participantes
while v < largo_partic_sel:
  partic_iter = list(partic_sel[v])
  w = 0
  caracter = []
  while w < len(partic_iter):
    caracter = caracter + [int(ord(partic_iter[w]))]
    w = w + 1
  x = 0
  suma_caracter = 0
  while x < len(caracter):
    suma_caracter = suma_caracter + caracter[x]
    x = x + 1
  pod_oculto_iter = [suma_caracter // len(caracter)]
  pod_oculto_partic = pod_oculto_partic + pod_oculto_iter
  v = v + 1

# El siguiente proceso realiza el cálculo de cada batalla individual del torneo con las especificaciones dadas
while u < largo_budokai_tenkaichi:
  while z < largo_budokai_tenkaichi:
    while y < largo_budokai_tenkaichi:
      if pod_oculto_partic[y] == pod_oculto_partic[y + 1]:
        if pod_oculto_partic[y] % 2 == 0 and pod_oculto_partic[y + 1] % 2 == 0:
          print(combates[y], "vs", combates[y + 1], "-> Gana ", combates[y])
          pod_oculto_partic.pop(y + 1)
          combates.pop(y + 1)
        else:
          print(combates[y], "vs", combates[y + 1], "-> Gana ",
                combates[y + 1])
          pod_oculto_partic.pop(y)
          combates.pop(y)
      else:
        if pod_oculto_partic[y] > pod_oculto_partic[y + 1]:
          print(combates[y], "vs", combates[y + 1], "-> Gana ", combates[y])
          pod_oculto_partic.pop(y + 1)
          combates.pop(y + 1)
        else:
          print(combates[y], "vs", combates[y + 1], "-> Gana ",
                combates[y + 1])
          pod_oculto_partic.pop(y)
          combates.pop(y)
      y = y + 1
      largo_budokai_tenkaichi = len(combates)
    y = 0
    z = z + 1
  z = 0
  y = 0
  u = u + 1

# SALIDA:

print("Y el campeon y poseedor del título del mas fuerte bajo el cielo es: " +
      str(combates[0]) + " !!!!!")
