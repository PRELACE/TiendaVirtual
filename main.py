from utils import Utils
import os
utils = Utils()
menu=utils.getMenu()#Lista de opciones
car_product=[]
os.system('cls' if os.name == 'nt' else 'clear')
print("\n====QUE BUENO TENERTE POR AQUI!,  QUE DESEAS HACER?====")
while True:
    utils.printMenuOptions(menu)
    #TODO: El menu solo tiene 5 opciones por defecto
    option = int(input("Mi opcion es :"))
    if option==1: #ver disponibilidad de productos
        product_list=utils.getListProducts()
        utils.printList(product_list)
    elif option==2: #? Agregar producto al carrito
        car_product=utils.addProductTOcard(car_product, utils.getListProducts())
    elif option==3: #? Ver mi carrito
        if not car_product:
            print("Tu carrito esta vacio")
        else:
            print(utils.printList(car_product))

    elif option==4: #? finalizar compra 
        pass
    elif option==5: #? Finalizar cmpra
        pass
    
    elif option==6: #? Cerrar programa    
        break
    else:
        if os.name=="nt":
            os.system("cls")
        else:
            os.system("clear")
        print("Lo siento, opcion no valida")

print("=======================Bay, Vuelve pronto!=====================")




