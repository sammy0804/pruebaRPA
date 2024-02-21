class Ejercicio1:
    @staticmethod
    def suma_serie(number, terminos):
        suma = 0
        numero_str = str(number)
        for i in range(1, terminos + 1):
            suma += int(numero_str * i)
        return suma

