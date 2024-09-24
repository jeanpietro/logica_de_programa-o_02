import os, time


estoque = {}
nomes = {}
quantidades = {}
precos = {}

while True:
    os.system('cls')
    print()
    print(f'{'-'*25}Simulador de inventário de loja{'-'*25}')
    print(f'Opções disponíveis:')
    print(f'1. Adicionar novo produto')
    print(f'2. Atualizar a quantidade de um produto')
    print(f'3. Listar produtos disponíveis')
    print(f'4. Valor total do estoque')
    print(f'5. Sair')
    print('-'*81)
    opcao = input('Escolha sua opção: ')
    if opcao == '1':
        n = int(input('Digite quantos produtos você quer adicionar: '))
        for _ in range(n):
            print()
            nome = input('Insira o nome do produto: ')
            nomes.append(nome)
            quantidade = int(input('Insira a quantidade do produto: '))
            quantidades.append(quantidade)
            preco_unitario = float(input('Insira o preço unitário do produto: '))
            precos.append(preco_unitario)
            print('Produto adicionado com sucesso!')
        estoque.append(nomes)
        estoque.append(quantidades)
        estoque.append(precos)
        time.sleep(3)
    elif opcao == '2':
        nome = input('Insira qual produto você quer alterar a quantidade: ')
        encontrado = False
        for i in nomes:
            if i == nome:
                encontrado = True
                quantidade_antiga = quantidades[nomes.index(i)]
                quantidade_nova = int(input('Insira a nova quantidade do produto: '))
                quantidades.insert(nomes.index(i),quantidade_nova)
                quantidades.remove(quantidade_antiga)
                print('Quantidade alterada com sucesso!')
                time.sleep(2)
                break
        if not encontrado:
            print('Produto não encontrado.')
    elif opcao == '3':
        print('Produtos disponíveis: ')
        for nome in nomes:
            print(f'Nome: {nome}, Quantidade: {quantidades[nomes.index(nome)]}, Preço unitário: R${precos[nomes.index(nome)]:.2f}')
        time.sleep(3)
    elif opcao == '4':
        total = 0
        for nome in nomes:
            valor = quantidades[nomes.index(nome)] * precos[nomes.index(nome)]
            total += valor
        print(f'O valor total dos produtos é: R${total:.2f}')
        time.sleep(3)

    elif opcao == '5':
        print('Programa finalizado.')
        break
    else:
        print('Insira uma opção válida')
        time.sleep(2)
