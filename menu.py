from ativos import (
    cadastrar_ativo,
    consultar_ativo,
    atualizar_ativo,
    remover_ativo
)

from vulnerabilidades import (
    cadastrar_vulnerabilidade,
    listar_vulnerabilidades
)

from persistencia import (carregar_dados)

def menu():
    carregar_dados()  # Carrega os dados do arquivo ao iniciar o programa

    while True:
        print("\n--- Sistema de Inventário de TI e Vulnerabilidades ---")
        print("1. Cadastrar Ativo")
        print("2. Consultar Ativo")
        print("3. Atualizar Ativo")
        print("4. Remover Ativo")
        print("5. Cadastrar Vulnerabilidade")
        print("6. Consultar Vulnerabilidades de um Ativo")
        print("0. Sair")

        try:
            opcao = int(input("\nEscolha uma opção: "))
            if opcao == 0:
                print("Programa encerrado.")
                break

        
            elif opcao == 1:
                cadastrar_ativo()

            elif opcao == 2:
                consultar_ativo()

            elif opcao == 3:
                atualizar_ativo()

            elif opcao == 4:
                remover_ativo()

            elif opcao == 5:
                cadastrar_vulnerabilidade()

            elif opcao == 6:
                listar_vulnerabilidades()

            else:
                print("Opção inválida! Tente novamente.")

        except ValueError:
            print("Erro: Por favor, digite um número válido.")