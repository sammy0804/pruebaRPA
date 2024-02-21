from collections import defaultdict

class Ejercicio3:

    @staticmethod
    def agrupar_elementos(lista):
        agrupaciones = defaultdict(list)
        for elemento in lista:
            agrupaciones[elemento].append(elemento)
        return list(agrupaciones.values())
