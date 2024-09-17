# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde. (10p)
Renta = float(input("Cual es tu renta anual?: "))
if Renta <= 10000:
    TipoIm = 5
elif Renta <= 20000:
    TipoIm = 15
elif Renta <= 35000:
    TipoIm = 20
elif Renta <= 60000:
    TipoIm = 30
else:
    TipoIm = 45
print("Tienes que pagar: ", Renta * TipoIm / 100,)
