# Para tributar un determinado impuesto se debe ser mayor
# de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales.
# Escribir un programa que pregunte
# al usuario su edad y sus ingresos mensuales y muestre por
# pantalla si el usuario tiene que tributar o no. (10p)
#Preuba
#Se soliciata el usuario su edad y se almacena en la variable Edad
Edad= int(input("Ingrese su edad: "))
 #Se solicita al usuario sus ingresos y se almacena en la variable ingresos
ingresos= float(input("Ingrese su salario: "))
 #Utilizamos if para verificar la edad y el salario del usuario 
if Edad >16 and ingresos >= 100:
 #Si se cumple la condicion imprime el resultado positivo
   print(" Usted puede tributar. ")
elif Edad < 16 and ingresos < 100:
 #Si no se cumple la condicion imprime el resultado negativo
   print(" Usted no puede tributar. ")
else:
  #No cumple ninguna condicion
  print(" Usted definitivamente no tributa. ")


