# pruebaRPA
Prueba técnica en Python, consta de 4 ejercicios básicos

# Proyecto de Programación Básica
Este proyecto incluye soluciones a una serie de ejercicios de programación en Python, diseñados para demostrar habilidades en operaciones matemáticas, manipulación de listas, y manejo básico de inventario. Cada solución se implementa en un módulo separado y se proporcionan ejemplos de uso.

## Ejercicio 1: Suma de Serie de Números Repetidos
Este módulo calcula la suma de una serie de un número X repetido hasta el n-ésimo término.
### Uso
Para utilizar este ejercicio, asegúrate de tener el script ejercicio1.py con la clase Ejercicio1 definida. Luego, puedes ejecutar el siguiente código:
```python
from ejercicio1 import Ejercicio1

serie = Ejercicio1()
print(f"Serie: {serie.suma_serie(3, 5)}")
```
Esto imprimirá la suma de la serie del número 3 repetido hasta el 5º término.

## Ejercicio 2: Filtrado de Lista
Este módulo filtra una lista de números basándose en criterios específicos: ser divisible por cinco, ser menor a 600, y detener el proceso si encuentra un número mayor a 1000.

### Uso:
Asegúrate de tener el script ejercicio2.py con la clase Ejercicio2. Ejemplo de uso:
```python
from ejercicio2 import Ejercicio2

filtrar = Ejercicio2()
lista = [24, 150, 300, 660, 295, 1050, 50]
print(f"Lista filtrada: {filtrar.filtrar_lista(lista)}")
```

## Ejercicio 3: Agrupación de Elementos en Matrices
Agrupa elementos similares de una lista en sub-listas.

### Uso:
Con el script ejercicio3.py y la clase Ejercicio3, puedes agrupar elementos:
```python
from ejercicio3 import Ejercicio3

agrupar = Ejercicio3()
lista2 = [12, 25, 1, 1, 7, 25]
print(f"Elementos agrupados: {agrupar.agrupar_elementos(lista2)}")
```

## Ejercicio 4: Sistema de Inventario
Gestiona un inventario permitiendo agregar o actualizar productos y visualizar el inventario actual.

### Uso:
Para este ejercicio, el script ejercicio4.py contiene la clase Inventario. Para interactuar con el menú del inventario:
```python
from ejercicio4 import Inventario

inventario = Inventario()
inventario.mostrar_menu()
```
Sigue las instrucciones en pantalla para agregar productos, actualizar existencias, o mostrar el inventario.
![image](https://github.com/sammy0804/pruebaRPA/assets/51298297/997581e2-81dc-4977-9a14-e2192e2d5111)

![image](https://github.com/sammy0804/pruebaRPA/assets/51298297/088068ee-a133-412e-abaf-7c415cc4a44e)

## Instalación
No se requieren instalaciones adicionales más allá de Python 3.x, ya que todos los scripts utilizan la biblioteca estándar.

## Contribución
Este proyecto es parte de una prueba técnica y no está abierto a contribuciones.
