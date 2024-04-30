class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        a=self.base*self.altura # implementación de la función con la formula de área de un rectángulo
        return a
    
rectangulo=Rectangulo(4,5)
print(f"El área del circulo es: {rectangulo.area()}")

import math
class Circulo:
    
    
    def __init__(self, radio):
        self.__radio = radio # inicialización de la variable radio

    def area(self):
        a=math.pi*self.__radio**2 # implementación de la función con la formula de área de un círculo
        return a
        

circulo=Circulo(3)
print(f"El área del circulo es: {circulo.area()}")
        