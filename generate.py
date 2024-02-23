# Gerador de credenciais recomendado para uso pessoal em sites que não precisem que você dê seu nome verdadeiro.
# Não me responsabilizo por mau uso desse código, visto que ele foi pensado para profissionais de SegInfo e caçadores de bug bounty.
# Faça bom uso dele ;-)

from random import choice
import string

print('================================================')
print('Gerador de Credenciais')
print('By: FeyHan')
print('==============================================')

tamUser = int(input('Qual o tamanho do seu user?: '))
tamSenha = int(input('Qual o tamanho da sua senha?: '))

print('===============================================')
senha = ' '
user = ' '

elementsB = string.ascii_letters + string.ascii_uppercase + string.ascii_lowercase
elements = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase + string.octdigits + string.hexdigits

for i in range(tamSenha):
    senha += choice(elements)

print('A senha gerada foi: ', senha)
if tamSenha <= 8:
    print('Senha fraca, melhor não usá-la...')
    tamSenha = int(input('Qual o tamanho da sua senha?: '))
else:
    print('Senha forte, pode usá-la!')
for i in range(tamUser):
    user += choice(elementsB)
print('O username gerado foi: ', user)