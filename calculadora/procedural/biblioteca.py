def calcular_iterativamente_forma_infixa():
    p1 = input('Digite o primeiro número: ')
    p1 = float(p1)
    sinal = input('Digite o sinal da operação (+ ou -): ')
    p2 = input('Digite o segundo número: ')
    p2 = float(p2)
    return _calcular(sinal, p1, p2)


def calcular_iterativamente_forma_prefixa():
    sinal = input('Digite o sinal da operação (*, + ou -): ')
    p1 = input('Digite o primeiro número: ')
    p1 = float(p1)
    p2 = input('Digite o segundo número: ')
    p2 = float(p2)
    return _calcular(sinal, p1, p2)


def _calcular(sinal, p1, p2):
    if sinal == '+':
        return p1 + p2
    elif sinal == '-':
        return p1 - p2
    raise Exception('Operação não suportada')
