# En este ejercicio, tendrán total libertad para elegir la problemática y la mejor solución. 
# Cada grupo podrá decidir su propio enfoque y desarrollar el software según sus criterios.
# El grupo que presente la mejor solución será el único en recibir los 60 puntos asignados a 
# esta pregunta.
#Punto de Venta con 3 Productos 
#####

sabritacant=20
sabritacosto=30
galletacant=5
galletacosto=19
refrescant=10
refrescosto=12
#Defino main para utlizar el reorno si no se 
# cumple alguna condicion
# main:cuerpo de trabajo   
def main():
    
    print("**********VENTAS**********")
    sabritas=int(input("¿Cuantas sabritas venderas?"))
    galletas=int(input("¿Cuantas galletas venderas?"))
    refrescos=int(input("¿Cuantas refrescos venderas?"))
    #While; Mientras las condiciones se cumplan, imprimer las cantidades disponible 
    #al usuario y que ingrese cantidades validas y el while lo retorna la main  principal 
    # 
    while (sabritas>sabritacant)or(galletas>galletacant)or(refrescos>refrescant): 
        
        print("solo dispogo de",sabritacant,"sabritas")
        print("solo dispogo de",galletacant,"galletas")
        print("solo dispogo de",refrescant,"refrescos")
        print("ingresar una cantidad disponible")
        
        
        return main()

    
    # Cuando el if se cumple  y tienes las cnatidades diponibles se reliza las 
    #operaciones
    if sabritas<=sabritacant:
    #Calculo el valor en pesos de los productos 
       ventasabritas=sabritas*sabritacosto
       ventagalletas=galletas*galletacosto
       ventarefrescos=refrescos*refrescosto
    #Sumo el total de cantidades de cada producto 
       costoproduc = ventasabritas + ventagalletas + ventarefrescos 
    #Imprimo el total de la venta 
       print("la venta total es:",costoproduc)
    #Pregunto al usuario con cuanto dinero pagara
       pagarcliente=int(input("¿con cuanto dinero pagara el cliente?"))
    #Realizo una resta para saber el cambio que se le da la cliente 
       cambio=pagarcliente-costoproduc
    #Imprimo cambio que se dara al cliente
       print("tendrias que devolver al cliente de cambio:",cambio)
         
    elif galletas<=galletacant:
        
        ventasabritas=sabritas*sabritacosto
        ventagalletas=galletas*galletacosto
        ventarefrescos=refrescos*refrescosto
        costoproduc = ventasabritas + ventagalletas + ventarefrescos 
        print("la venta total es:",costoproduc)
        pagarcliente=int(input("¿con cuanto dinero pagara el cliente?"))
        cambio=pagarcliente-costoproduc
        print("tendrias que devolver al cliente de cambio:",cambio)  
        
    elif refrescos<=refrescant:
    
        ventasabritas=sabritas*sabritacosto
        ventagalletas=galletas*galletacosto
        ventarefrescos=refrescos*refrescosto
        costoproduc = ventasabritas + ventagalletas + ventarefrescos 
        print("la venta total es:",costoproduc)
        pagarcliente=int(input("¿con cuanto dinero pagara el cliente?"))
        cambio=pagarcliente-costoproduc
        print("tendrias que devolver al cliente de cambio:",cambio)
        
main()           
