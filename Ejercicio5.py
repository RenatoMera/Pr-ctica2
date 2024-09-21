# En este ejercicio, tendrán total libertad para elegir la problemática y la mejor solución. 
# Cada grupo podrá decidir su propio enfoque y desarrollar el software según sus criterios.
# El grupo que presente la mejor solución será el único en recibir los 60 puntos asignados a esta pregunta.

sabritacant=20
sabritacosto=30

galletacant=5
galletacosto=19

refrescant=10
refrescosto=12
  
def main():
    while True: 
        
        print("**********VENTAS**********")
        sabritas=int(input("¿Cuantas sabritas venderas?"))
        galletas=int(input("¿Cuantas galletas venderas?"))
        refrescos=int(input("¿Cuantas refrescos venderas?"))
        
        if sabritas>sabritacant:
            print("solo dispogo de",sabritacant,"sabritas")
            sabritas=int(input("ingresa una cantidad valida"))
            return
             
        elif galletas>galletacant:
            print("solo dispogo de",galletacant,"galletas")
            sabritas=int(input("ingresa una cantidad valida"))
            return
              
        elif refrescos>refrescant:
            print("solo dispogo de",refrescant,"refrescos")
            sabritas=int(input("ingresa una cantidad valida"))
            return
            
        else:
            sabritas=int(input("¿Cuantas sabritas venderas?"))
            galletas=int(input("¿Cuantas galletas venderas?"))
            refrescos=int(input("¿Cuantas refrescos venderas?"))
            ventasabritas=sabritas*sabritacosto
            ventagalletas=galletas*galletacosto
            ventarefrescos=refrescos*refrescosto
            costoproduc = ventasabritas + ventagalletas + ventarefrescos 
            print("la venta total es:",costoproduc)
            pagarcliente=int(input("¿con cuanto dinero pagara el cliente?"))
            cambio=pagarcliente-costoproduc
            print("tendrias que devolver al cliente de cambio:",cambio)
            return
main()

            
