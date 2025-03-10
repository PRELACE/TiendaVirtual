from utils import Utils
import os

# Instancia de la clase de utilidades
utils = Utils()

# Obtener menú y carrito dinámico
menu = utils.getMenu()  # Lista de opciones
car_product = []

# Limpiar la terminal según el sistema operativo
os.system('cls' if os.name == 'nt' else 'clear')

print("\n==== ¡QUÉ BUENO TENERTE POR AQUÍ! ¿QUÉ DESEAS HACER? ====")

# Este es el formato del menu de opciones
'''
[
"Disponibilidad de produtos",====>1
"Agregar producto al carrito",=====>2
"Ver mi carrito",========>3
"Aplicar un descuento",========>4
"Finalizar compra",=========>5
"Cerrar programa",========>6
"Modificar mi carrtio"=========>7
'''

while True:
    # Mostrar opciones del menú
    utils.printMenuOptions(menu)

    # Capturar la opción del usuario (asegurarse de que sea un número)
    option = input("Mi opción es: ")

    # Verificar que la opción ingresada sea un número
    if not option.isdigit():
        print("Por favor, ingresa un número válido.")
        continue

    option = int(option)

    if option == 1:  
        # Mostrar disponibilidad de productos
        product_list = utils.getListProducts()
        utils.printList(product_list)

    elif option == 2:  
        # Agregar un producto al carrito
        car_product = utils.addProductTOcard(car_product, utils.getListProducts())

    elif option == 3:  
        # Mostrar el contenido del carrito
        if not car_product:
            print("Tu carrito está vacío.")
        else:
            print("\nMi Carrito:")
            utils.showMyCar(car_product)

    elif option == 4: 
        #! Esta funcion es ANGELO
        #TODO: Objetivo======> Aplicar descento sin finalizar compra
        # Validar si hay descuento y si no aplicarlo
        pass

    elif option == 5:
        #! Esta funcion es para ANGELO
        #TODO: Objetivo=====> FInalizar compra
        # Finalizar la compra
        # Se pregunta por el descuento si no se ha aplicado previamente
        # Al finalizar, se vacía el carrito
        pass

    elif option == 6:  
        # Cerrar el programa
        # Se rompe el ciclo para terminar la ejecución
        break
    
    elif option == 7:  
        #! Esta fncion es para CHRISTOFER GOMEZ E.
        # TODO: Obtjetivo===> Eliminar un producto del carrito
        # Ve al archvi utils y lee los comentarios en la funcion closeBuy 
        pass

    else:
        # Limpiar la pantalla y mostrar mensaje de opción inválida
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opción no válida, intenta nuevamente.")

print("======================= ¡Bye! ¡Vuelve pronto! =====================")
