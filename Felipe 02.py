# Ecreva um programa que receba 2 números e imprima o que o usuário solicitar de acordo com as seguintes opções

n1 = int(input(f"Digite o primeiro número:"))
n2 = int(input(f"Digite o segundo número:"))
opcao = int(input(f"Escolha uma opção:"))

if opcao == 1:
    print("A Soma é:",n1 + n2)
elif opcao == 2:
    print("O Produto é:",n1 * n2)
elif opcao == 3:
    print("O resto da divisão é:",n1 % n2)
elif opcao == 4:
    print("A divisão é:",n1 / n2)
elif opcao == 5:
    print("A subtração é:",n1 - n2)
else:
    print("Opção invalida")
