# Estruturas de Dados Iniciais (Enums e Dicionários)
from enum import Enum

class TipoAtivo(Enum):
    SERVIDOR = 1
    ROTEADOR = 2
    NOTEBOOK = 3
    SISTEMA_INTERNO = 4

inventario_ativos = {}

# Criando o Menu Interativo

while True:
    print("\n---Sistema de Inventário de TI e Vulnerabilidades---")
    print("1. Cadastrar Ativo")
    print("2. Consultar Ativo")
    print("3. Atualizar Ativo")
    print("4. Remover Ativo")
    print("5. Gerenciar Vulnerabilidades")
    print("0. Sair")

    opcao = int(input("Escolha uma opção:"))
    if opcao == "0":
        print("Programa encerrado.")
        break

    elif opcao == "1":
        print("Cadastro de ativo")

    elif opcao == "2":
        print("Consulta de ativo")

    elif opcao == "3":
        print("Atualização de ativo")

    elif opcao == "4":
        print("Remoção de ativo")

    elif opcao == "5":
        print("Cadastro de vulnerabilidade")

    elif opcao == "6":
        print("Consulta de vulnerabilidades")

    else:
        print("Opção inválida.")

   
        

            