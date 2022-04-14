from collections import Counter

dias_semana = {
    '2': 'Segunda-Feira',
    '3': 'Terça-Feira',
    '4': 'Quarta-Feira',
    '5': 'Quinta-Feira',
    '6': 'Sexta-Feira'
}

d_live = Counter()
while True:
    live = input('Digite o número correspondente ao dia da semana (ou "fim" para encerrar): ')
    if live == 'fim':
        break # sai do while True
    if live in dias_semana: # se é um dos números de candidato válido
        d_live.update([live])
    else:
        print(f'Número inválido: {live}')

print('Resultado:')
for numero, d_live in live.most_common():
    print(f'{dias_semana[numero]} teve {d_live} votos')