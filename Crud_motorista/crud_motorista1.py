import json
import os
from time import sleep

class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'

arquivo = os.path.join(os.path.dirname(__file__), 'motoristas.json')


if not os.path.isfile(arquivo):
    with open(arquivo, 'w') as f:
        json.dump([], f)

def ler_motoristas():
    with open(arquivo, 'r') as f:
        return json.load(f)

def mudar_motoristas(motoristas):
    with open(arquivo, 'w') as f:
        json.dump(motoristas, f, indent=4)

def adicionar_motorista(nome, idade, cpf, nascimento, telefone, endereco, email):
    motoristas = ler_motoristas()
    motoristas.append({'nome': nome, 'idade': idade, 'cpf': cpf, 'nascimento': nascimento, 'telefone': telefone, 'endereco': endereco, 'email': email})
    mudar_motoristas(motoristas)
    print("MOTORISTA ADICIONADO COM SUCESSO!")

def listar_motoristas():
    motoristas = ler_motoristas()
    if motoristas:
        print("=" * 50)
        print("LISTA DE MOTORISTAS:")
        print("-" * 50)
        for motorista in motoristas:
            print("*" * 50)
            print(f"NOME: {motorista['nome']}, IDADE: {motorista['idade']}, CPF: {motorista['cpf']}, NASCIMENTO: {motorista['nascimento']}, TELEFONE: {motorista['telefone']}, ENDEREÇO: {motorista['endereco']}, EMAIL: {motorista['email']}")
            print("*" * 50)
            print("=" * 50)
    else:
        print("NENHUM MOTORISTA CADASTRADO.")

def atualizar_motorista(cpf, novo_telefone, novo_endereco, novo_email):
    motoristas = ler_motoristas()
    for motorista in motoristas:
        if motorista['cpf'] == cpf:
            motorista['telefone'] = novo_telefone
            motorista['endereco'] = novo_endereco
            motorista['email'] = novo_email
            break
    mudar_motoristas(motoristas)
    print(" MOTORISTA ATUALIZADO COM SUCESSO!")

def excluir_motorista(cpf):
        motoristas = ler_motoristas()

        for motorista in motoristas:  
            if motorista['cpf'] == cpf:
                motoristas.remove(motorista)

        mudar_motoristas(motoristas)
        print("MOTORISTA EXCLUÍDO COM SUCESSO!")

def buscar_motorista(cpf):
    motoristas = ler_motoristas()
    encontrado = False
    for motorista in motoristas:
        if motorista['cpf'] == cpf:
            print(f"NOME: {motorista['nome']}, IDADE: {motorista['idade']}, CPF: {motorista['cpf']}, NASCIMENTO: {motorista['nascimento']}, TELEFONE: {motorista['telefone']}, ENDEREÇO: {motorista['endereco']}, EMAIL: {motorista['email']}")
            encontrado = True
    if not encontrado:
        print("NENHUM MOTORISTA ENCONTRADO.")

def linha_horizontal(cor):
    return cor + "=" * 50 + cor.RESET

def menu_inicial():
    print(cor.CIANO + "=" * 55 + cor.RESET)
    print(cor.VERMELHO + " ---->>> BEM VINDO AO SISTEMA JORNADA <<<---- ")
    print("          1 - MÓDULO MOTORISTA ")
    print("          3 - SAIR ")
    print(cor.CIANO + "=" * 55 + cor.RESET)

def exibir_menu():
    print("\nMENU:")
    print("1. ADICIONAR MOTORISTA")
    print("2. LISTAR MOTORISTAS")
    print("3. ATUALIZAR MOTORISTA")
    print("4. EXCLUIR MOTORISTA")
    print("5. BUSCAR MOTORISTA")
    print("6. VOLTAR AO MENU ANTERIOR")

def main():
    while True:
        menu_inicial()
        opcao_inicial = int(input("INFORME UMA OPÇÃO: "))

        match opcao_inicial:
            case 2:
                print("MÓDULO EM DESENVOLVIMENTO")

            case 1:
                while True:
                    exibir_menu()
                    opcao = input("ESCOLHA UMA OPÇÃO:\n>>> ")

                    if opcao == "1":
                        nome = input("DIGITE O NOME:\n>>> ")
                        idade = input("DIGITE A IDADE:\n>>> ")
                        cpf = input("DIGITE SEU CPF:\n>>> ")
                        nascimento = input("DIGITE O DIA DE SEU NASCIMENTO:\n>>> ")
                        telefone = input("DIGITE SEU NÚMERO DE TELEFONE:\n>>> ")
                        endereco = input("DIGITE SEU ENDEREÇO:\n>>> ")
                        email = input("DIGITE SEU EMAIL:\n>>> ")
                        adicionar_motorista(nome, idade, cpf, nascimento, telefone, endereco, email)
                    elif opcao == "2":
                        listar_motoristas()
                    elif opcao == "3":
                        cpf = input("DIGITE O CPF DO MOTORISTA A SER ATUALIZADO:\n>>> ")
                        novo_telefone = input("DIGITE O NOVO TELEFONE:\n>>> ")
                        novo_endereco = input("DIGITE A NOVA IDADE:\n>>> ")
                        novo_email = input("DIGITE O NOVO EMAIL\n>>>")
                        atualizar_motorista(cpf, novo_telefone, novo_endereco, novo_email)
                    elif opcao == "4":
                        cpf = input("DIGITE O CPF DO MOTORISTA A SER EXCLUÍDO:\n>>> ")
                        excluir_motorista(cpf)
                    elif opcao == "5":
                        nome = input("DIGITE O CPF DO MOTORISTA QUE VOCÊ DESEJA ENCONTRAR:\n>>> ")
                        buscar_motorista(nome)
                    elif opcao == "6":
                        print("VOLTAR AO MENU ANTERIOR...")
                        sleep(3)
                        break
                    else:
                        print(" OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
            case 3:
                print(" SAINDO...")
                sleep(3)
                break
            case __:
                print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

if __name__ == "__main__":
    main()
