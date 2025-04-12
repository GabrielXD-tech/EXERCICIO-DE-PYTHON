primeiro_valor = input('Digite um valor:')
segundo_valor = input('Digite outro valor:')

if primeiro_valor < segundo_valor:
    print(f'o primeiro valor ="{primeiro_valor}" é maior que o segundo valor')
elif segundo_valor > primeiro_valor:
    print(f'o segundo valor ="{segundo_valor}" é maior que o primeiro valor')
else:
    print(f'Não foi possível declarar qual o valor maior')
