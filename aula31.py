"""
Flag (Bandeira) - Marcar um local
None = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

v1 = 'a'
print(id(v1))

condicao = False
passou_no_if = None

if condicao:
     passou_no_if = True
     print('faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')
