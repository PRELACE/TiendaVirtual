class Utils:
    def __init__(self):
        pass

    
    def printList(self, lista):
        # Encabeados
        print("+----+------------------------------+")
        print("| ID | Producto                     |")
        print("+----+------------------------------+")

        
        for i, producto in enumerate(lista, start=1):
            print(f"| {i:2} | {producto:28} |")

        # Final de la tabla 
        print("+----+------------------------------+")
    


    #Envia la lista de los productos disponibles hasta el momento
    def getListProducts(self):
        return [
            "Teléfono inteligente"[200],
            "Laptop",
            "Audífonos inalámbricos",
            "Reloj inteligente",
            "Teclado mecánico",
            "Silla ergonómica",
            "Monitor 4K",
            "Disco duro externo",
            "Cafetera automática",
            "Smart TV",
            "Aspiradora robot",
            "Cámara de seguridad WiFi",
            "Tableta gráfica",
            "Altavoz Bluetooth",
            "Router de alta velocidad",
            "Batería portátil",
            "Consola de videojuegos",
            "Licuadora de alto rendimiento",
            "Termo de acero inoxidable",
            "Mochila impermeable"
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
            if not is_continue:
                return car_list  # Retorna la lista con los productos agregados
            
    