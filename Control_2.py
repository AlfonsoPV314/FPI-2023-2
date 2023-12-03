# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA/FUNDAMENTOS DE COMPUTACIÓN Y PROGRAMACIÓN
# SECCIÓN DEL CURSO: 0-L-35
# PROFESOR DE TEORÍA: CARLOS VERA
# PROFESOR DE LABORATORIO: ANDRÉS MUÑOZ
#
# AUTOR
# NOMBRE: Alfonso Sebastian Palacios Vergara
# RUT: 23.345.432-2
# CARRERA: Ingeniería Civil Informática
#________________________________________________________________________________________________________


def operar_fracciones(nombre_archivo_entrada, nombre_archivo_salida):
  with open(nombre_archivo_entrada, "r") as archivo:
    texto=archivo.read()
    texto=texto.split(" ")
    fraccion1=texto[0]
    fraccion2=texto[-1]
    operacion=texto[1]
    num1=int(fraccion1.split("/")[0])
    den1=int(fraccion1.split("/")[-1])
    num2=int(fraccion2.split("/")[0])
    den2=int(fraccion2.split("/")[-1])
    den_final=" "
    if operacion=="+" or operacion=="-":
      if den1>den2:
        den_mayor=den1
        i=0
        while i<den_mayor:
          if i*den2==den_mayor:
            den_final=den_mayor
            aux=i
            num2=num2*aux
          i+=1
        if den_final==" ":
          den_final=den1*den2
          num1=num1*den2
          num2=num2*den1
      else:
        den_mayor=den2
        i=0
        while i<den_mayor:
          if i*den1==den_mayor:
            den_final=den_mayor
            aux=i
            num1=num1*aux
          i+=1
        if den_final==" ":
          den_final=den1*den2
          num1=num1*den2
          num2=num2*den1
      if operacion=="+":
        num_final=num1+num2
        if num_final>den_final:
          valor_mayor=num_final
          valor_menor=den_final
        else:
          valor_mayor=den_final
          valor_menor=num_final
        i=0
        while i<valor_menor:
          if i%valor_mayor==0 and i%valor_menor==0:
            valor_mayor=valor_mayor/i
            valor_menor=valor_menor/i
          i+=1
        fraccion_final=str(num_final)+"/"+str(den_final)
      else:
        num_final=num1-num2
        if num_final>den_final:
          valor_mayor=num_final
          valor_menor=den_final
        else:
          valor_mayor=den_final
          valor_menor=num_final
        i=1
        while i<valor_menor:
          if valor_mayor%i==0 and valor_menor%i==0:
            valor_mayor=valor_mayor/i
            valor_menor=valor_menor/i
          i+=1
        fraccion_final=str(num_final)+"/"+str(den_final)
      
    elif operacion=="*":
      num_final=num1*num2
      den_final=den1*den2
      if num_final>den_final:
        valor_mayor=num_final
        valor_menor=den_final
      else:
        valor_mayor=den_final
        valor_menor=num_final
      i=1
      while i<valor_menor:
        if valor_mayor%i==0 and valor_menor%i==0:
          valor_mayor=valor_mayor/i
          valor_menor=valor_menor/i
        i+=1
      fraccion_final=str(num_final)+"/"+str(den_final)
    elif operacion==":":
      num_final=num1*den2
      den_final=num2*den1
      if num_final>den_final:
        valor_mayor=num_final
        valor_menor=den_final
      else:
        valor_mayor=den_final
        valor_menor=num_final
      i=1
      while i<valor_menor:
        if valor_mayor%i==0 and valor_menor%i==0:
          valor_mayor=valor_mayor/i
          valor_menor=valor_menor/i
        i+=1
      fraccion_final=str(num_final)+"/"+str(den_final)
    else:
      fraccion_final=" "
    with open(nombre_archivo_salida,"w") as resultado:
      resultado.write("El resultado de la fracción es: "+str(fraccion_final))
      
    return True
    
## Tiene un problema: calcula las fracciones simplificadas con valores aux
## (valor_mayor y valor_menor), pero no actualiza los valores iniciales 
## (num_final y den_final), aquellos que considera para hacer la fracción del resultado.
## Por ende, retorna fracciones sin simplificar, aunque haga la simplificación.
