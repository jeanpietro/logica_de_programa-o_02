import os

def soma_lista(n):
    lista = []
    for i in range(1,n+1,2):
       lista.append(i)
    return len(lista), sum(lista)

x=int(input('Digite até que o número deseja somar:'))
os.system('cls')

comp,soma = soma_lista(x)

print(f'Há {comp} números impares entre 1 e {x}')
print(f'A soma deles é igual á: {soma}')   