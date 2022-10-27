senhac = 1234
saldoc = 150
chavec = 321
print("Óla sejam bem-vindo ao nosso banco!!")
conta = int(input("Número da conta:"))
agencia = int(input("Sua angecia:"))
senha = int(input("Insira sua senha:"))
if senha == senhac:
    chave = int(input("Insira sua chave de segurança:"))
    if chave == chavec:
        while True:
            print('''
     Opções
            
    1 - Saldo
    2 - Deposita
    3 - Sacar
    4 - Sair''')
            opcao = int(input("Insira sua Opção:"))
            if opcao == 1:
                print(f"Seu saldo é de {saldoc} r$")
            elif opcao == 2:
                dp = int(input(f'''Qual quatidade que você quer deposita?
    R$ '''))
                saldoc = saldoc + dp
                print("Seu saldo foi depositado com sucesso!")
            elif opcao == 3:
                     sacar = int(input(f'''Qual quatidade que você quer sacar?
    R$ '''))
                     if saldoc >= sacar:
                         saldoc =saldoc-sacar
                         print("Seu saque foi realizado com sucesso!!")
                     else:
                         print("Sem Saldo!!")    
            elif opcao == 4:
                print("Obrigado pelo uso do nosso banco!!")
                break
            else:
                print("Opção Invalida")
                               
    else:
        print("Chave incorreta")
else:
    print("Senha incorreta")
