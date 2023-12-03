# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA/FUNDAMENTOS DE COMPUTACIÓN Y PROGRAMACIÓN
# SECCIÓN DEL CURSO: L-35
# PROFESOR DE TEORÍA: CARLOS VERA
# PROFESOR DE LABORATORIO: ANDRÉS MUÑOZ
#
# AUTOR
# NOMBRE: Alfonso Sebastian Palacios Vergara
# RUT: 21.775.623-5
# CARRERA: Ingeniería Civil Informática
# El programa presente encuentra en una larga cadena de texto
# con los datos deestudiantes de varias universidades y carreras
# (rut,nombre,apellido,edad,univerdidad, notas de 5 asignaturas
# y correo) aquellos estudiantes de la usach que tienen mas
# asignaturas aprobadas que reprobadas, y retorna sus correos.
#________________________________________________________________

# ENTRADAS
entrada_1 = input().split(";")
entrada_2 = input().lower()

# PROCESAMIENTO
j = 0
k = 0
aprobadas = 0
reprobadas = 0
while j < len(entrada_1):

  # Establecemos los datos del estudiante de la iteracion en una lista
  estudiante_iter = entrada_1[j]
  estudiante_iter = estudiante_iter.split(",")

  # Si el estudiante pertenece a la carrera indicada y a la usach
  if estudiante_iter[5].lower() == entrada_2 and estudiante_iter[4].lower(
  ) == "usach":

    # Recolectamos sus notas
    nota_1 = float(estudiante_iter[7])
    nota_2 = float(estudiante_iter[8])
    nota_3 = float(estudiante_iter[9])
    nota_4 = float(estudiante_iter[10])
    nota_5 = float(estudiante_iter[11])
    notas_iter = [nota_1] + [nota_2] + [nota_3] + [nota_4] + [nota_5]

    # Recorremos la lista con las notas viendo si aprobó o reprobó
    while k < len(notas_iter):

      # Si el/la estudiante aprobó
      if notas_iter[k] >= 4.0:
        aprobadas += 1

      # Si el/la estudiante reprobó
      else:
        reprobadas += 1
      k += 1
    k = 0

    # SALIDAS
    if aprobadas > reprobadas:
      print(estudiante_iter[6])
  j += 1
