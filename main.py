import json 
from enum import Enum

# Configuração de Arquivo

ARQUIVO_DADOS = "dados_inventario.json"

# Estruturas de Dados Iniciais (Enum)
class TipoAtivo(Enum):
    SERVIDOR = 1
    ROTEADOR = 2
    NOTEBOOK = 3
    APLICAÇÃO_WEB = 4

# Severidade das vulnerabilidades (Enum)
class Severidade(Enum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3
    CRITICA = 4 

# Tratamento das vulnerabilidades (Enum)
class Tratamento(Enum):
    ABERTO = 1
    EM_TRATAMENTO = 2
    CORRIGIDA = 3
    ACEITA = 4

# Dicionário principal

inventario_ativos = {}

# Funções Auxiliares de Arquivo

def salvar_dados():
    with open(ARQUIVO_DADOS, 'w') as f:
        json.dump(inventario_ativos, f, indent=4)

def carregar_dados():
    global inventario_ativos
    try:
        with open(ARQUIVO_DADOS, 'r') as f:
            # Carrega os dados do arquivo JSON para o dicionário
            inventario_ativos = json.load(f)
    except FileNotFoundError:
        inventario_ativos = {}

# Módulos de Funcionalidade

# Requisito 3: Cadastrar Ativo

def cadastrar_ativo():
    print("\n --- Novo Cadastro ---")
    try:
        id_ativo = int(input("Digite o ID único do ativo (apenas números):"))

        if id_ativo in inventario_ativos:
            print("Erro: ID já existe no sistema.")
            return
        
        nome = input("Nome/Hostname:")
        while True:
            responsavel = input("Responsável:").strip()
            if responsavel.replace(" ", "").isalpha():
                break
            else:
                print("Entrada inválida! Digite apenas letras (sem números ou símbolos). \n")

        print(f"Responsável cadastrado: {responsavel}")


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

        salvar_dados()
        print("Ativo cadastrado com sucesso!")

    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite números onde for solicitado.")

# Requisito 4: Consultar Ativo

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
            
# Requisito 5: Atualizar Ativo

def atualizar_ativo():
    print("\n--- Atualizar Ativo ---")
    try:
        id_ativo = int(input("Digite o ID do ativo que deseja atualizar:"))
        
        if id_ativo not in inventario_ativos:
            print("Erro: Ativo não encontrado no sistema.")
            return
    
    
        ativo = inventario_ativos[id_ativo]
        print("Dica: Dica: Deixe o campo em branco e aperte Enter se não quiser alterá-lo.")

        novo_nome = input(f"Nome atual ({ativo['nome']}):").strip()
        novo_responsavel = input(f"Responsavel atual ({ativo['responsavel']})").strip()
        novo_setor = input(f"Setor atual ({ativo['setor']}):").strip()
    
# Atualiza apenas se o usuário digitou algo
        if novo_nome: ativo["nome"] = novo_nome
        if novo_responsavel: ativo["responsavel"] = novo_responsavel
        if novo_setor: ativo["setor"] = novo_setor
    
        salvar_dados()
        print("Ativo atualizado com sucesso!")
    
    except ValueError:
        print("Erro: O ID deve ser um número inteiro.")

# Requisito 6: Remover Ativo

def remover_ativo():
    print("\n--- Remover Ativo ---")
    try:
        id_ativo = int(input("Digite o ID do ativo a ser removido:"))
           
        if id_ativo in inventario_ativos:  
            del inventario_ativos[id_ativo] # Remove do dicionário
            salvar_dados() # Atualiza o arquivo
            print("Ativo( e suas vulnerabilidades) removido com sucesso!")
        else:
            print("Erro: Ativo não encontrado.")
    except ValueError:
        print("Erro: O ID deve ser um número inteiro.")

# Requisito 7: Cadastrar Vulnerabilidades

def cadastrar_vulnerabilidade():
    print("\n--- Cadastrar Vulnerabilidade ---")
    
    id_ativo = int(input("Digite o ID do ativo para cadastrar a vulnerabilidade:"))
        
    if id_ativo not in inventario_ativos:
            print("Erro: Ativo não encontrado no sistema.")
            return
        
    descricao = input("Descrição da vulnerabilidade:")
    severidade = input("Severidade (Baixa, Média, Alta, Crítica):")
        
    try:
             # Usando o Enum para Severidade
        print("\nNíveis de Severidade:")
        for s in Severidade:
            print(f"{s.value} - {s.name}")
        cod_sev = int(input("Escolha o código da severidade: "))
        severidade = Severidade(cod_sev).name
        
        # Usando o Enum para Status de Tratamento
        print("\nStatus de Tratamento:")
        for t in Tratamento:
            print(f"{t.value} - {t.name}")
        cod_status = int(input("Escolha o código do status: "))
        status = Tratamento(cod_status).name
        
    except ValueError:
        print("Erro: Código inválido. Cadastro de vulnerabilidade cancelado.")
        return
    
    # Adiciona a vulnerabilidade à lista do ativo
    inventario_ativos[id_ativo]["vulnerabilidades"].append({
        "descricao": descricao,
        "severidade": severidade,
        "status": status
    })
    
    salvar_dados()
    print("Vulnerabilidade cadastrada com sucesso!")

# Requisito 8: Visualizar Vulnerabilidades de um Ativo

def listar_vulnerabilidades():
    print("\n--- Consultar Vulnerabilidades de um Ativo ---")
    try:
        id_ativo = int(input("Digite o ID do ativo para consultar suas vulnerabilidades:"))
        
        if id_ativo not in inventario_ativos:
            print("Erro: Ativo não encontrado no sistema.")
            return
        
        vulnerabilidades = inventario_ativos[id_ativo]["vulnerabilidades"]
        
        if not vulnerabilidades:
            print("Nenhuma vulnerabilidade cadastrada para este ativo.")
            return
        
        print(f"\nVulnerabilidades do Ativo [ID: {id_ativo}] - {inventario_ativos[id_ativo]['nome']}:")
        for idx, vuln in enumerate(vulnerabilidades, start=1):
            print(f"{idx}. Descrição: {vuln['descricao']} , Severidade: {vuln['severidade']} , Status de Tratamento: {vuln['status']}\n")
            
    
    except ValueError:
        print("Erro: O ID deve ser um número inteiro.")


# Criando o Menu Interativo

def menu():
    carregar_dados()  # Carrega os dados do arquivo ao iniciar o programa

while True:
    print("\n---Sistema de Inventário de TI e Vulnerabilidades---")
    print("1. Cadastrar Ativo")
    print("2. Consultar Ativo")
    print("3. Atualizar Ativo")
    print("4. Remover Ativo")
    print("5. Cadastrar Vulnerabilidade")
    print("6. Consultar Vulnerabilidades de um Ativo")
    print("0. Sair")

    try:
        opcao = int(input("Escolha uma opção:"))
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


if __name__ == "__main__":
    menu()