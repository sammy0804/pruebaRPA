from ejercicio1 import Ejercicio1
from ejercicio2 import Ejercicio2
from ejercicio3 import Ejercicio3
from ejercicio4 import Inventario



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #Ejemplo de uso ejercicio1
    serie = Ejercicio1()
    print(f"Serie: {serie.suma_serie(3, 5)}")
    print()

    # Ejemplo de uso ejercicio2
    filtrar = Ejercicio2()
    lista= [24, 150, 300, 660, 295, 1050, 50]
    print(f"Lista filtrada: {filtrar.filtrar_lista(lista)}")
    print()

    agrupar = Ejercicio3()
    lista2= [12, 25, 1, 1, 7, 25]
    print(f"Elementos agrupados: {agrupar.agrupar_elementos(lista2)}")
    print()


    # Ejemplo de uso ejercicio4
    inventario = Inventario()
    inventario.mostrar_menu()
