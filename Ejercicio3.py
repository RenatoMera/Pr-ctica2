# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
#    Renta	   	         Tipo impositivo
#Menos de 10000€	         5%
#Entre 10000€ y 20000€		15%
#Entre 20000€ y 35000€	    20%
#Entre 35000€ y 60000€	    30%
#Más de 60000€	            45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla 
# el tipo impositivo que le corresponde. (10p)

#Se soliciata al usuario que ingrese la renta mensual y se almacena en la variable renta
renta=float(input("Ingrese la renta mensual: "))
# Condicional para determinar el tipo impositivo dependiendo de la renta
if renta <= 10000:
    x = 5
    print("el porcentaje es ", x)
elif renta <= 20000:
    x= 15
    print("el porcentaje es ", x)
elif renta <= 35000:
    x=20
    print("el porcentaje es ", x)
elif renta <= 60000:
    x=30
    print("el porcentaje es ", x)
elif renta > 60000:
    x=45
    print("el porcentaje es ", x)




