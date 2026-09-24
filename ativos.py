from dados import inventario_ativos
from enums import TipoAtivo
from persistencia import salvar_dados

# Módulos de Funcionalidade

# Requisito 3: Cadastrar Ativo

def cadastrar_ativo():
    print("\n --- Novo Cadastro ---")
    try:
        id_ativo = int(input("\nDigite o ID único do ativo (apenas números):"))

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
        print("\nTipos disponiveis:")
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