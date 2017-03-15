# Classes Abstratas

class Operacao:
    """Classe responsável por definir como calculo é feito"""

    def calcular(self, p1, p2):
        raise NotImplementedError('Precisa ser implementado')


class Calculadora:
    """Classe responsável por obter inputs e efetuar operação de acordo"""

    def __init__(self):
        self._operacoes = {}
        adicao = Adicao()
        self.adicionar_operacao('+', adicao)

    def obter_inputs(self):
        """Deve obter sinal, p1, e p2 retornando os valores nessa ordem"""
        raise NotImplementedError('Precisa ser implementado')

    def efetuar_operacao(self):
        sinal, p1, p2 = self.obter_inputs()
        try:
            operacao_escolhida = self._operacoes[sinal]
        except KeyError:
            raise Exception('Operação não suportada')
        else:
            return operacao_escolhida.calcular(p1, p2)

    def adicionar_operacao(self, sinal, operacao):
        self._operacoes[sinal] = operacao


# Classes concretas
class CalculadoraInfixa(Calculadora):
    def obter_inputs(self):
        p1 = input('Digite o primeiro número: ')
        p1 = float(p1)
        sinal = input('Digite o sinal da operação (*, + ou -): ')
        p2 = input('Digite o segundo número: ')
        p2 = float(p2)
        return sinal, p1, p2


class Adicao(Operacao):
    def calcular(self, p1, p2):
        return p1 + p2
