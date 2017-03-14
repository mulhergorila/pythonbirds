class Poligono:
    dimensao = '2D'
    _protegido = False

    def __init__(self, cor=None):
        self.cor = cor
        self._Poligono__privado = True

    def calcular_area(self):
        print(id(self))
        return 8


if __name__ == '__main__':
    Poligono._protegido = True
    print(Poligono._protegido)
    p1 = Poligono('Azul')
    print(p1.__dict__)
    p2 = Poligono()
    print(id(p1))
    print(p1.calcular_area())
    print(id(p2))
    print(p2.calcular_area())
    p2.cor = 'Red'
    print(p1.cor)
    print(id(p1.cor))
    print(p2.cor)
    print(id(p2.cor))

    p1.dimensao = '3D'
    Poligono.dimensao = '4D'
    print(Poligono.dimensao)  # 4D
    print(id(Poligono.dimensao))
    print(p1.dimensao)  # 3D
    print(id(p1.dimensao))
    p1.lkhg = 1
    print(p1.__dict__)
    del p1.dimensao
    print(p1.__dict__)
    print(p1.dimensao)
    print(p2.dimensao)  # 4D
    print(id(p2.dimensao))
    print(p2.__dict__)
    print(Poligono.__dict__)
    del Poligono.dimensao
    print(Poligono.__dict__)

    for nome_propriedade in dir(p1):
        valor_propriedade = getattr(p1, nome_propriedade)
        if not callable(valor_propriedade) and not nome_propriedade.startswith('_'):
            print(nome_propriedade, valor_propriedade)

