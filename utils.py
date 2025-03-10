import os
from collections import Counter
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
    


    '''Retorna la lista de los productos disponibles hasta el momento'''
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
       
       
    '''
    Retorna una lista que contiene todas las opciones del menu
    '''
    def getMenu(self):
        return [
            "Disponibilidad de produtos",
            "Agregar producto al carrito",
            "Ver mi carrito",
            "Aplicar un descuento",
            "Finalizar compra",
            "Cerrar programa",
            "Modificar mi carrtio"
        ]
        
    '''
    Calcula el descuento a la compra
    '''
    def calcDiscount(self):
        #En proceso
        pass
    
    '''
    Imprime el menu opciones en forma de tbla
    '''
    def printMenuOptions(self, menu):
        print("+------------+----------------------------------------")
        print("| Opcion     | Descripción                           |")
        print("+------------+----------------------------------------")
        for i, opcion in enumerate(menu, start=1):
            print(f"| {i:2}         | {opcion:37} |")
        print("+------------+----------------------------------------")
        
        
    '''
    Este pemetodo permite agregar productos al carrito
    '''
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
            
            '''Preguntamos si desea continuar agregando productos'''
            is_continue = input("¿Continuar agregando? (y/n): ").strip().lower() == "y"
            if not is_continue :
                '''
                    Retornamos la lista de los productos
                    agregados al carrito
                '''
                return car_list
    def showMyCar(self, carList):
        # Contar la cantidad de cada producto en la lista
        conteo_productos = Counter([producto[0] for producto in carList])

        print("+----+--------------------------------------+-----------+-----------------+-------------+")
        print("| ID | Producto                             | Cantidad  | Precio unitario | Subtotal    |")
        print("+----+--------------------------------------+-----------+-----------------+-------------+")

        total = 0
        for idx, (producto_nombre, cantidad) in enumerate(conteo_productos.items(), start=1):
            # Obtener el precio unitario del primer producto con ese nombre
            producto_info = next(p for p in carList if p[0] == producto_nombre)
            precio_unitario = producto_info[1]
            subtotal = cantidad * precio_unitario
            total += subtotal

            print(f"| {idx:<2} | {producto_nombre:<36} | {cantidad:^9} | {precio_unitario:^15,.2f} | {subtotal:^11,.2f} |")

        print("+----+--------------------------------------+-----------+-----------------+-------------+")
        print(f"Total actual: {total:,.2f}")
        
    def removeProductFromCar(self, car_list, id, quantity):
        """
        Método para remover un producto del carrito.

        Pasos a seguir:
        1. Verificar si el carrito tiene productos:
        - Si el carrito está vacío, mostrar un mensaje y salir de la función.
        
        2. Mostrar el contenido actual del carrito al usuario.
        
        3. Validar que el ID del producto sea válido:
        - No debe ser mayor que la cantidad total de productos en el carrito.
        
        4. Contar cuántas veces aparece el producto en el carrito:
        - La cantidad a remover no debe ser mayor a la cantidad total de ese producto en la lista.
        
        5. Si las validaciones son correctas:
        - Remover el producto tantas veces como indique `quantity`.
        
        6. Preguntar al usuario si está seguro de eliminar el producto antes de proceder.
        
        7. Retornar la lista `car_list` actualizada con los productos removidos.
        
        8. Asignar la nueva lista a la variable del carrito para reflejar los cambios.
        """

    def closeBuy(self, car_list):
        """
        Método para finalizar la compra.

        Pasos a seguir:
        1. Verificar si el carrito tiene productos:
        - Si el carrito está vacío, mostrar un mensaje y salir de la función.
        
        2. Preguntar al usuario si desea aplicar un descuento:
        - Si acepta, solicitar el porcentaje o cantidad a descontar y aplicarlo al total.
        
        3. Calcular los montos finales:
        - Subtotal (antes del descuento).
        - Descuento aplicado (si corresponde).
        - Total a pagar (subtotal - descuento).
        
        4. Mostrar al usuario el resumen de su compra con todos los detalles.
        
        5. Vaciar el carrito:
        - Asignar una lista vacía `[]` a la variable del carrito.
        
        6. Confirmar al usuario que la compra se ha completado con éxito.
        """

            