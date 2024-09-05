lista = []

nome1 = input('Digite um nome: ')
lista.append(nome1)

nome2 = input('Digite um nome: ')

if nome2 in lista:
    print(f'Sim, o {nome2} na lista')
else:
     print(f'Não o {nome2} não está na lista')