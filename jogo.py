import random
import os

#recebe um numero aleatorio entre 0 e 100
num_premiado = random.randint(0,100)
num_tentados = []
num_tentativas = 10

os.system("cls")
while True:
    ent_usuario = int(input("Digite um numero: "))
    if ent_usuario == num_premiado:
        print("Voçe ganhou")
        break
    elif num_tentativas == 0:
        print(f"Voçe perdeu, o numero premiado era {num_premiado}")
        break
    else:
        print("Voçe nao acertou o numero")

        #recebe um numero tentado na lista
        num_tentados.append(ent_usuario)

        #Verifica se o numero digitado e maior ou menor
        if ent_usuario > num_premiado:
            print("digite um numero menor!")
        else:
            print("digite um numero maior!")

print("fim de jogo")
print(f"voce tentou os numeros: `{num_tentados}")
print(f"Voce precisa de: {(len(num_tentados))} tentativas")


