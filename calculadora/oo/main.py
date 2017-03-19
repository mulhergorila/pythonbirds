from calculadora.oo.framework import Calculadora, Operacao, CalculadoraInfixa


class CalculadoraPrefixa(Calculadora):
    def obter_inputs(self):
        sinal = input('Digite o sinal da operação (*, + ou -): ')
        p1 = input('Digite o primeiro número: ')
        p1 = float(p1)
        p2 = input('Digite o segundo número: ')
        p2 = float(p2)
        return sinal, p1, p2


class Divisao(Operacao):
    def calcular(self, p1, p2):
        return p1 / p2

    
class Multiplicacao(Operacao):
    def calcular(self, p1, p2):
        return p1 * p2


calculadora = CalculadoraInfixa()
calculadora.adicionar_operacao('/', Divisao())
calculadora.adicionar_operacao('*', Multiplicacao())

print(calculadora.efetuar_operacao())
