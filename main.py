from os import system
from time import sleep
from datetime import datetime

# Constantes e listas globais
LIMITE_SAQUE = 500.0
LIMITE_QTD_SAQUES = 3
AGENCIA = "0001"

usuarios = []
contas = []

# Funções do sistema bancário

def sacar(*, saldo, valor, extrato, qtd_saques):
    if qtd_saques >= LIMITE_QTD_SAQUES:
        print('Operação falhou! Número máximo de saques excedido.')
    elif valor > LIMITE_SAQUE:
        print("Operação falhou! O valor do saque excede o limite.")
    elif valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor <= 0:
        print('Operação falhou! O valor do saque precisa ser positivo.')
    else:
        saldo -= valor
        extrato.append({
            'data': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            'valor': valor,
            'operação': 'SAQUE'
        })
        qtd_saques += 1
        print('Saque Realizado com Sucesso!')
    return saldo, extrato, qtd_saques

def depositar(saldo, valor, extrato):
    if valor <= 0:
        print('Operação falhou! O valor do depósito precisa ser positivo.')
    else:
        saldo += valor
        extrato.append({
            'data': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            'valor': valor,
            'operação': 'DEPÓSITO'
        })
        print('Depósito Realizado com Sucesso!')
    return saldo, extrato

def visualizar_extrato(extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for item in extrato:
            print(f"DATA: {item['data']} | Valor: R$ {item['valor']:.2f} | Operação: {item['operação']}")
    input('\nPressione Enter para voltar')

def criar_usuario():
    cpf = input("Informe o CPF (somente números): ").strip()
    if any(u['cpf'] == cpf for u in usuarios):
        print("Já existe um usuário com esse CPF!")
        return
    nome = input("Informe o nome completo: ").strip()
    nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
    endereco = input("Informe o endereço (logradouro, número, bairro, cidade/sigla estado): ").strip()
    
    usuarios.append({
        'nome': nome,
        'nascimento': nascimento,
        'cpf': cpf,
        'endereco': endereco
    })
    print("Usuário criado com sucesso!")

def criar_conta():
    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    
    if usuario:
        numero_conta = len(contas) + 1
        contas.append({
            'agencia': AGENCIA,
            'numero_conta': numero_conta,
            'usuario': usuario
        })
        print(f"Conta criada com sucesso! Agência: {AGENCIA}, Número da Conta: {numero_conta}")
    else:
        print("Usuário não encontrado. Cadastre o usuário primeiro.")

# Função principal
def main():
    saldo = 0.0
    extrato = []
    qtd_saques = 0

    msg_menu = '''
    1) Realizar saque
    2) Realizar depósito
    3) Extrato da Conta
    4) Criar Usuário
    5) Criar Conta Corrente
    6) Sair
    ____________________
    '''

    while True:
        print(msg_menu)
        try:
            opcao = int(input('Escolha uma opção: '))
        except ValueError:
            print('Opção inválida. Digite um número.')
            continue

        system('cls')

        if opcao == 1:
            valor = float(input('Informe o valor do saque: R$ ').strip())
            saldo, extrato, qtd_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, qtd_saques=qtd_saques)
            sleep(2)

        elif opcao == 2:
            valor = float(input('Informe o valor do depósito: R$ ').strip())
            saldo, extrato = depositar(saldo, valor, extrato)
            sleep(2)

        elif opcao == 3:
            visualizar_extrato(extrato)

        elif opcao == 4:
            criar_usuario()
            sleep(2)

        elif opcao == 5:
            criar_conta()
            sleep(2)

        elif opcao == 6:
            print("Saindo...")
            break

        else:
            print("Opção Inválida!")
            sleep(2)
        
        system('cls')

if __name__ == "__main__":
    main()
