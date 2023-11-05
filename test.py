lista_principal = []
lista_armazenadora = []
lista_de_notas = []
while True:
    lista_armazenadora.append(str(input('Nome: ')))
    lista_armazenadora.append((float(input('Nota 1: '))))
    lista_armazenadora.append((float(input('Nota 2: '))))
    lista_de_notas.append(lista_armazenadora[1:3])
    lista_armazenadora.append((lista_armazenadora[1] + lista_armazenadora[2]) / 2)
    lista_principal.append(lista_armazenadora[:])
    lista_armazenadora.clear()
    while True:
        questao = str(input('Quer continuar? S/N: ')).strip().upper()[0]
        if questao == 'N':
            break
        elif questao != 'S':
            print('Tente novamente.')
        elif questao == 'S':
            break
    if questao == 'N':
        break
c = 0
for item in lista_principal:
    print(f'Nº: {c} Nome: {item[0]} Media: {item[3]}')
    c += 1
while True:
    questao2 = int(input('Quer ver as notas de qual aluno? (Dígite 999 para parar): '))
    if questao2 == 999:
        break
    else:
        print(lista_de_notas[questao2])
