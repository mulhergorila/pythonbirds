from mensageiro import Mensageiro

spam= Mensageiro()


print(spam.enviar('Minha mensagem'))
# deve ser impresso
#['Enviando por Email: Minha Mensagem', Enviando por SMS: Minha Mesagem

print(spam.enviar('Outra mensagem'))
# deve ser impresso
#['Enviando por Email: Outra Mensagem', Enviando por SMS: Outra Mesagem]