"""
Iterando strings com while
"""

#   012345678910

nome = 'Luiza' # Iteráveis

# 111087654321


indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'❤️{letra}'
    indice += 1

novo_nome += '❤️'
print(novo_nome)
