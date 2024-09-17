# Escribir un programa que almacene la cadena de caracteres contraseña en una
# variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña 
# introducida por el usuario coincide con la guardada en la variable sin tener en cuenta
# mayúsculas y minúsculas. (10 p)

contrasena="Contraseña12345678" 
contrasena1 = input("Por favor, ingresa la contraseña: ")
if contrasena.lower()==contrasena1.lower():
  print("Contraseña correcta")
else:
  print("Contraseña incorrecta")   

