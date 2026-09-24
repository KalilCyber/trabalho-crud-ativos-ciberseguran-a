from dados import inventario_ativos
from enums import Severidade, Tratamento
from persistencia import salvar_dados, carregar_dados


# Requisito 7: Cadastrar Vulnerabilidades

def cadastrar_vulnerabilidade():
    print("\n--- Cadastrar Vulnerabilidade ---")
    
    id_ativo = int(input("Digite o ID do ativo para cadastrar a vulnerabilidade:"))
        
    if id_ativo not in inventario_ativos:
            print("Erro: Ativo não encontrado no sistema.")
            return
        
    descricao = input("Descrição da vulnerabilidade:")
    categoria = input("Digite o categoria/tipo da vulnerabilidade:")
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
        "categoria":  categoria, 
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
            print(f"{idx}. Descrição: {vuln['descricao']} , Categoria: {vuln['categoria']} , Severidade: {vuln['severidade']} , Status de Tratamento: {vuln['status']}\n")
            
    
    except ValueError:
        print("Erro: O ID deve ser um número inteiro.")

