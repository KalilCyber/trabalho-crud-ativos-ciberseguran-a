# Estruturas de Dados Iniciais (Enums e Dicionários).
from enum import Enum

class TipoAtivo(Enum):
    SERVIDOR = 1
    ROTEADOR = 2
    NOTEBOOK = 3
    APLICAÇÃO_WEB = 4

def salvar_dados():
    with open(ARQUIVO_DADOS, 'w') as f:
        json.dump(inventario_ativos, f, indent=4)

# Dicionário pronto para atuar como hashmap, permitindo indexar e buscar os ativos pelo ID.

inventario_ativos = {}
ARQUIVO_DADOS = "dados_inventario.txt"

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
    if opcao == 0:
        print("Programa encerrado.")
        break

    elif opcao == 1:
        print("Cadastro de ativo")

    elif opcao == 2:
        print("Consulta de ativo")

    elif opcao == 3:
        print("Atualização de ativo")

    elif opcao == 4:
        print("Remoção de ativo")

    elif opcao == 5:
        print("Cadastro de vulnerabilidade")

    elif opcao == 6:
        print("Consulta de vulnerabilidades")

    else:
        print("Opção inválida! Tente novamente.")

# Módulos de Funcionalidade

def salvar_dados():
    with open(ARQUIVO_DADOS, 'w') as f:
        json.dump(inventario_ativos, f, indent=4)
    
def cadastrar_ativo():
    print("\n --- Novo Cadastro ---")
    try:
        id_ativo = int(input("Digite o ID único do ativo (apenas números):"))

        if id_ativo in inventario_ativos:
            print("Erro: ID já existe no sistema.")
            return
        
        nome = input("Nome/Hostname:")
        responsavel = input("Responsável:")
        setor = input("Setor:")

# Exibindo as opções do Enum
        print("Tipos disponiveis:")
        for tipo in TipoAtivo:
            print(f"{tipo.value} - {tipo.name}")
        
        codigo_tipo = int(input("Escolha o código do tipo de ativo:"))
        tipo_selecionado = TipoAtivo(codigo_tipo).name

# Salvando no dicionário com a lista de vulns inicial
        
        inventario_ativos[id_ativo] = {
        "nome": nome,
        "responsavel": responsavel,
        "setor": setor,
        "tipo": tipo_selecionado,
        "vulnerabilidades": []
        }

# Gravando num arquivo de texto 
        
        with open(ARQUIVO_DADOS, 'w') as f:
            json.dump(inventario_ativos, f, indent=4)

        print("Ativo cadastrado com sucesso!")

    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite números onde for solicitado.")

def consultar_ativo():
        print("\n--- Consultar Ativo ---")
        termo = input("Digite o ID ou o Nome do ativo para buscar:").strip().lower()
        encontrou = False

# Percorre todo o dicionário procurando correspondência

        for id_ativo, dados in inventario_ativos.items():
            if termo == str(id_ativo) or termo in dados["nome"].lower():
                print(f"\n[ID: {id_ativo}]")
                print(f"Nome/Hostname: {dados['nome']}")
                print(f"Responsavel: {dados['responsavel']}")
                print(f"Setor/Localização: {dados['setor']}")
                print(f"Tipo: {dados['tipo']}")
                print(f"Quantidade de vulnerabilidades: {len(dados['vulnerabilidades'])}")
                encontrou = True
        
            if not encontrou:
                print("Nenhum ativo foi encontrado com esse termo.")




    
























# Gravando num arquivo de texto
    
        


        
   
        

            