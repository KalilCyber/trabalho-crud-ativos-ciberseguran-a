# Estruturas de Dados Iniciais (Enums e Dicionários)
from enum import Enum

class TipoAtivo(Enum):
    SERVIDOR = 1
    ROTEADOR = 2
    NOTEBOOK = 3
    SISTEMA_INTERNO = 4

inventario_ativos = {}

# Criando o Menu Interativo

def exibir_menu():
    print("\n---Sistema de Inventário de TI e Vulnerabilidades---")
    print("1. Cadastrar Ativo")
    print("2. Consultar Ativo")
    print("3. Atualizar Ativo")
    print("4. Remover Ativo")
    print("5. Gerenciar Vulnerabilidades")
    print("0. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção:")

        try:
            opcao_int = int(opcao)
            if opcao_int == 1:
                print("Iniciando cadastro...")
            elif opcao_int == 0:
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida! Escolha um número do menu.")
        except ValueError:
            print("Erro: Digite apenas números inteiros válidos.")
            