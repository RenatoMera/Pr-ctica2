# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales.
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no. (10p)
Edad = int(input("Introduzca su Edad: "))
Ingresos = float(input("Introduzca el salario que percibe: "))
if Edad > 16 and Ingresos >=1000:
    print("debes pagar impuestos")
else:
    print("No debes pagar impuestos")    
