from mensageiro import Mensageiro

spam = Mensageiro()

spam.adicionar_destinatario('Tiago')
spam.adicionar_meio('Slack')

pega_mensagem = input('Digite a mensagem: ')

print(spam.enviar(pega_mensagem))

print(spam.enviar('Minha mensagem'))
# deve ser impresso
# ['Enviando por Email: Minha Mensagem', Enviando por SMS: Minha Mesagem]

print(spam.enviar('Outra mensagem'))
# deve ser impresso
# ['Enviando por Email: Outra Mensagem', Enviando por SMS: Outra Mesagem]