from os import system
from time import sleep
from datetime import datetime


# variáveis do domínio
saldo = 0.0
lista_extrato = []
LIMITE_SAQUE = 500.0
qtd_saques = 0

# opções do menu
msg_menu = '''
    1) Realizar saque
    2) Realizar depósito
    3) Extrato da Conta
    4) Sair
    ____________________
'''

# controle da aplicação
loop = True

while loop:
    print(msg_menu)
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
            valor_do_saque = float(input('Informe o valor do saque: R$ ').strip())

            if qtd_saques > 3:
                print('Operação falhou! Número máximo de saques excedido.')
            elif valor_do_saque >= LIMITE_SAQUE:
                print("Operação falhou! O valor do saque excede o limite.")
            elif valor_do_saque > saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif valor_do_saque < 0:
                print('Operação falhou! O valor do saque precisa ser positivo.')
            else:

                saldo -= valor_do_saque

                saque_reg = {
                    'data': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                    'valor': valor_do_saque,
                    'operação': 'SAQUE'
                }

                qtd_saques += 1
                lista_extrato.append(saque_reg)
                
                print('Saque Realizado com Sucesso!')
            
            sleep(3)
                
    elif opcao == 2:
        valor_do_deposito = float(input('Informe o valor do depósito: R$ ').strip())

        if valor_do_deposito <= 0:
            print('Operação falhou! O valor do depósito precisa ser positivo.')
        else:
            deposito_reg = {
                'data': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                'valor': valor_do_deposito,
                'operação': 'DEPÓSITO'
            }

            saldo += valor_do_deposito
            lista_extrato.append(deposito_reg)
            
            print('Depósito Realizado com Sucesso!')
            sleep(3)
            
    elif opcao == 3:
        print("\n================ EXTRATO ================")

        if len(lista_extrato) == 0:
            print("Não foram realizadas movimentações.")
        else:
            for extrato in lista_extrato:
                
                data = extrato['data']
                valor = extrato['valor']
                operacao = extrato['operação']
                 
                print(f'DATA: {data} | Valor: R$ {valor:.2f} | Operação: {operacao}')

        
        while True:
            input('Pressione Enter para voltar')
            break
            
    elif opcao == 4:
        print('Saindo...')
        loop = False
    else:
        print('Opção Inválida!\n\n')
        
    system('cls')
