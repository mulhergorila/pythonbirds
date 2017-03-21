class Mensageiro:
    def __init__(self):
        self.meios = {}
        self.destinatarios = {}
        # self.adicionar_meio('Email')
        # self.adicionar_meio('SMS')

    def adicionar_destinatario(self, destinatario):
        self.destinatarios[destinatario] = destinatario

    def adicionar_meio(self, meio):
        self.meios[meio] = meio

    def enviar(self, mensagem):
        for destinatario in self.destinatarios:
            for meio in self.meios:
                print("Enviando mensagem: {} via {} para {}".format(mensagem, meio, destinatario))
            print('-'*80)

class CanalDeMensagem:
    def __init__(self, tipo):
        self.tipo = tipo


class Email(CanalDeMensagem):
    def __init__(self, tipo):
        super().__init__(tipo)


class SMS(CanalDeMensagem):
    def __init__(self):
        super().__init__('SMS')


if __name__ == '__main__':

    spam = Mensageiro()

    spam.adicionar_destinatario('Tiago')
    spam.adicionar_destinatario('Teste')
    spam.adicionar_meio('Slack')
    spam.adicionar_meio('SMS')
    spam.adicionar_meio('Email')

    # pega_mensagem = input('Digite a mensagem: ')

    # print(spam.enviar(pega_mensagem))

    print(spam.enviar("Mensagem padrão"))

    print(spam)