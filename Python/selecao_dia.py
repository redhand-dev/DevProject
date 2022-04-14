def votacao(dia_live):  # fução para votação com a variavel dia da semana como argumento
    global dia_segunda_feira, dia_terca_feira, dia_quarta_feira, dia_quinta_feira, dia_sexta_feira
 
    if dia_live.isalpha():  # checa se o dia da semana contém apenas letras
        if dia_live == 'Fim' or dia_live == 'fim' or dia_live == 'FIM':
            print('FIM DA VOTAÇÃO')
            print_resultados()

    elif dia_live.isnumeric():  # checa se o dia da semana e um caracter numérico
        if dia_live == '2' or dia_live == '3' or dia_live == '4' or dia_live == '5' or dia_live =='6':
            if dia_live == '2':
                dia_segunda_feira += 1
            elif dia_live == '3':
                 dia_terca_feira += 1
            elif dia_live == '4':
                 dia_quarta_feira += 1
            elif dia_live == '5':
                 dia_quinta_feira += 1
            elif dia_live == '6':
                 dia_sexta_feira += 1
        else:  # se o valor digitado não for válido, há entrada de novo dia da semana e a função repete
            dia_live= str(input('Digite um número válido para o dia da live: '))
            votacao(dia_live)


def print_resultados():  #printa resultados e encerra programa
    global dia_segunda_feira, dia_terca_feira, dia_quarta_feira, dia_quinta_feira, dia_sexta_feira

    print('QUANTIDADE DE VOTOS:\n')
    print('Live na Segunda-Feira - TOTAL DE ' + str(dia_segunda_feira))
    print('Live na Terça-Feira - TOTAL DE ' + str(dia_terca_feira))
    print('Live na Quarta-Feira - TOTAL DE ' + str(dia_quarta_feira))
    print('Live na Quinta-Feira - TOTAL DE ' + str(dia_quinta_feira))
    print('Live na Sexta-Feira - TOTAL DE ' + str(dia_sexta_feira))

    exit()  # encerra prog


if __name__ == '_main_':  # funcao main 
    dia_segunda_feira = 0
    dia_terca_feira = 0
    dia_quarta_feira = 0
    dia_quinta_feira = 0
    dia_sexta_feira = 0


    while True:  #laço ocorre indefinidamente até que ocorra o 'Fim'
        dia_live = str(input('PROGRAMAÇÃO LIVE \n Digite o dia de sua preferência: '))
        votacao(dia_live)