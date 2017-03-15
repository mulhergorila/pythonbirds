import math

from geometria.base import Poligono


class Retangulo(Poligono):
    def __init__(self, cor=None, base=None, altura=None):
        super().__init__(cor)
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.base * self.altura


class Quadrado(Retangulo):
    def __init__(self, cor=None, lado=None):
        super().__init__(cor, lado, lado)
        self.lado = lado


class Circulo(Poligono):
    def __init__(self, cor=None, raio=None):
        super().__init__(cor)
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)


if __name__ == '__main__':
    retangulo_azul = Retangulo('Azul', 5, 6)
    print(retangulo_azul.calcular_area())
    print(retangulo_azul.dimensao)
    print(retangulo_azul.cor)
    quadrado_amarelo = Quadrado('Amarelo', 7)
    print('Área do quadrado: %s' % quadrado_amarelo.calcular_area())

    poligonos = [quadrado_amarelo, retangulo_azul, Circulo('Branco', 1)]

    for p in poligonos:
        print('Área de {} é: {}'.format(type(p).__name__, p.calcular_area()))
