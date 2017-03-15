from calculadora.oo.framework import CalculadoraInfixa, Calculadora


class CalculadoraPrefixa(Calculadora):
    def obter_inputs(self):
        sinal = input('Digite o sinal da operação (*, + ou -): ')
        p1 = input('Digite o primeiro número: ')
        p1 = float(p1)
        p2 = input('Digite o segundo número: ')
        p2 = float(p2)
        return sinal, p1, p2


calculadora = CalculadoraPrefixa()

print(calculadora.efetuar_operacao())
