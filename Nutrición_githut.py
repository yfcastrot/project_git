#Saludo
datos = True
while datos == True:
    saludo = input("Hola, desea saber la recomendacion de alimentacion balanceada segun la nutriologa (S/N): ").upper()
    if saludo == "S":        
        while True:
            try:
                edad = int(input("Ingrese su edad: "))
            except:
                print("La edad debe ser un numero entero. Intenta de nuevo...")
            else:
                break
        while True:
            try:
                peso = float(input("Ingrese su peso actual: "))    
            except:
                print("El peso debe ser un valor numerico. Intenta de nuevo...")    
            else:
                break
    elif saludo == "N":
        print("En otra oportunidad sera. Hasta pronto.")
    else:
        print("Opcion no valida. Intentelo de nuevo.")
        input("Presione ENTER para continuar...")

    repetir = True
    while repetir == True:
        rta = input("Desea imprimir el resultado (S/N): ").upper()
        if rta == "S":
            repetir = False
            datos = False
        elif rta == "N":
            repetir = False
            datos = True   
        else:
            print("Opcion no valida. Intentelo de nuevo.")
            input("Presione ENTER para continuar...")
            break

    #Insertar nutrición estandar
    c = 60.1 / 1000
    p = 30.5 / 1000
    fv = -24.4 / 1000
    #Insertar porciones para completar dieta
    #A es la dieta para un niño desnutrido
    A = 2*c + p + 2*fv
    #B es la dieta para un niño con sobrepeso
    B = 0.6*c + p + 4*fv
    #C es la dieta para un niño saludable
    C = 0.5*c + 0.7*p + 2*fv
    #rango edades
    rangoA = range(5,11)
    rangoB = range(11,14)
    rangoC = range(14,18)
    dia = 0
#condiciones para edades entre [5 y 10]

if(edad in rangoA) and (peso < 16):
  estado = "A"
  peso_ideal = 22
  nutricion = A

  while (peso < peso_ideal):
    peso += nutricion
    dia += 1
elif (edad in rangoA) and (peso >28):
    estado = "B"
    peso_ideal = 24
    nutricion = B

    while (peso > peso_ideal):
      peso += nutricion
      dia += 1
elif(edad in rangoA)and (peso>=16 and peso <=28):
  estado = "C"
  nutricion = C
  peso_ideal = 28

  while (peso < peso_ideal):
    peso += nutricion
    dia += 1
#condiciones edad y peso para edades entre (10 y 13]

if(edad in rangoB) and (peso < 30):
  estado = "A"
  peso_ideal = 32
  nutricion = A

  while (peso < peso_ideal):
    peso += nutricion
    dia += 1

elif (edad in rangoB) and (peso > 50):
  estado = "B"
  peso_ideal = 43
  nutricion = B

  while (peso > peso_ideal):
    peso += nutricion
    dia += 1

elif (edad in rangoB) and (peso>=30 and peso <=50):
  estado = "C"
  nutricion = C
  peso_ideal = 50

  while (peso < peso_ideal):
    peso += nutricion
    dia += 1

#condiciones edad y peso para edades entre (13 y 17]

if(edad in rangoC) and (peso < 51):
  estado = "A"
  peso_ideal = 56
  nutricion = A

  while (peso < peso_ideal):
    peso += nutricion
    dia += 1

elif (edad in rangoC) and (peso > 63):
  estado = "B"
  peso_ideal = 58
  nutricion = B

  while (peso > peso_ideal):
    peso += nutricion
    dia += 1

elif (edad in rangoC) and (peso>=51 and peso<=63):
  estado = "C"
  nutricion = C
  peso_ideal = 63

  while (peso < peso_ideal):
    peso += nutricion
    dia += 1
   

#Imprimir datos
if estado == "A" or "B":
 fin_msm = "un peso saludable"
if(estado == "C"):
  fin_msm = "el peso maximo"

if (peso != peso_ideal) or peso == peso_ideal:
  print(f"El estado nutricional del paciente es {estado} y se requieren {dia} dias de dieta para que alcance {fin_msm}")

