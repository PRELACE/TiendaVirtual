import os
class Utils:
    def __init__(self):
        pass

    
    def printList(self, lista):
        # Encabeados
        print("+----+------------------------------------+------------")
        print("| ID | Producto                           |   Precio  |")
        print("+----+------------------------------------+------------")

        
        for i, (nombre, precio) in enumerate(lista, start=1):
            print(f"| {i:2} | {nombre:33} | {precio:11} |")


        # Final de la tabla 
        print("+----+------------------------------------+------------")
    


    #Envia la lista de los productos disponibles hasta el momento
    def getListProducts(self):
        return [
            ["Teléfono inteligente", 2989],
            ["Laptop", 20000],
            ["Audífonos inalámbricos", 400],
            ["Reloj inteligente", 1590],
            ["Teclado mecánico", 4580],
            ["Silla ergonómica", 1500],
            ["Monitor 4K", 7099],
            ["Disco duro externo", 4500],
            ["Cafetera automática", 10700],
            ["Smart TV", 20599],
            ["Aspiradora robot", 15852],
            ["Cámara de seguridad WiFi", 10999],
            ["Tableta gráfica", 6700],
            ["Altavoz Bluetooth", 5645],
            ["Router de alta velocidad", 1300],
            ["Batería portátil", 4622],
            ["Consola de videojuegos", 11300],
            ["Licuadora de alto rendimiento", 7400],
            ["Termo de acero inoxidable", 1200],
            ["Mochila impermeable", 2460]
        ]

    def showCardInTime(sel, cardlist):
       sel.printList(cardlist)
       
       
    #Para mostrar el menu
    def getMenu(self):
        return [
            "Disponibilidad de produtos",
            "Agregar producto al carrito",
            "Ver mi carrito",
            "Aplicar un descuento",
            "Finalizar compra",
            "Cerrar programa"
        ]
        

    def calcDiscount(self):
        #En proceso
        pass
    
    def printMenuOptions(self, menu):
        print("+------------+----------------------------------------")
        print("| Opcion     | Descripción                           |")
        print("+------------+----------------------------------------")
        for i, opcion in enumerate(menu, start=1):
            print(f"| {i:2}         | {opcion:37} |")
        print("+------------+----------------------------------------")

    def addProductTOcard(self, car_list, products_list):
        while True:
            try:
                id_product = int(input("Id del producto (1 en adelante): ")) - 1  # Convertir a índice de lista
                
                if 0 <= id_product < len(products_list):  # Validar índice
                    car_list.append(products_list[id_product])
                    print("Producto agregado al carrito.")
                else:
                    print("Lo siento, producto no encontrado.")

            except ValueError:
                print("Por favor, ingresa un número válido.")

            is_continue = input("¿Continuar agregando? (y/n): ").strip().lower() == "y"
            if is_continue != False:
                return car_list  # Retorna la lista con los productos agregados
            
    