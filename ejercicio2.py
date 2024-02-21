class Ejercicio2:

    @staticmethod
    def filtrar_lista(lista):
        resultado = []
        for numero in lista:
            if numero > 1000:
                break
            if numero % 5 == 0 and numero <= 600:
                resultado.append(numero)
        return resultado
