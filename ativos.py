import json
import tkinter as tk
from tkinter import messagebox, simpledialog
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
            # Carrega os dados do arquivo JSON
            dados_brutos = json.load(f)
            # Converte todas a chaves (IDS) de string de volta para inteiros
            inventario_ativos = {int(id_str): dados for id_str, dados in dados_brutos.items()}
    
    except FileNotFoundError:
        inventario_ativos = {}


# Módulos de Funcionalidade

# Requisito 3: Cadastrar Ativo

def cadastrar_ativo():
    id_ativo = simpledialog.askinteger("Novo Cadastro", "Digite o ID único do ativo (apenas números):")
    if id_ativo is None: return # O usuário cancelou
    
    if id_ativo in inventario_ativos:
        messagebox.showerror("Erro", "ID já existe no sistema.")
        return
    
    nome = simpledialog.askstring("Novo Cadastro", "Nome/Hostname:")
    if not nome: return
    
    responsavel = ""
    while True:
        resp = simpledialog.askstring("Novo Cadastro", "Responsável:")
        if not resp: return
        
        if resp.strip().replace(" ", "").isalpha():
            responsavel = resp.strip()
            break
        else:
            messagebox.showwarning("Aviso", "Entrada inválida! Digite apenas letras.")
            
    setor = simpledialog.askstring("Novo Cadastro", "Setor:")
    if not setor: return          
       
       

# Exibindo as opções do Enum
    opcoes_tipo = "Tipos disponíveis:\n"
    for tipo in TipoAtivo:
        opcoes_tipo += f"{tipo.value} - {tipo.name}\n"
    
    codigo_tipo = simpledialog.askinteger("Novo Cadastro", f"{opcoes_tipo}\nEscolha o código do tipo de ativo:")
    if codigo_tipo is None: return
    
    try:
        tipo_selecionado = TipoAtivo(codigo_tipo).name
    except ValueError:
        messagebox.showerror("Erro", "Código de tipo inválido.")
        return
# Salvando no dicionário com a lista de vulns inicial
        
    inventario_ativos[id_ativo] = {
        "nome": nome,
        "responsavel": responsavel,
        "setor": setor,
        "tipo": tipo_selecionado,
        "vulnerabilidades": []
        }

    salvar_dados()
    messagebox.showinfo("Sucesso", "Ativo cadastrado com sucesso!")

# Requisito 4: Consultar Ativo

def consultar_ativo():
    termo = simpledialog.askstring("Consultar Ativo", "Digite o ID ou o Nome do ativo para buscar:")
    if not termo: return
    termo = termo.strip().lower()

# Percorre todo o dicionário procurando correspondência

    resultados = ""
    for id_ativo, dados in inventario_ativos.items():
        if termo == str(id_ativo) or termo in dados["nome"].lower():
            resultados += f"ID: {id_ativo}\n"
            resultados += f"Nome/Hostname: {dados['nome']}\n"
            resultados += f"Responsável: {dados['responsavel']}\n"
            resultados += f"Setor: {dados['setor']}\n"
            resultados += f"Tipo: {dados['tipo']}\n"
            resultados += f"Qtd Vulnerabilidades: {len(dados['vulnerabilidades'])}\n"
            resultados += "-" * 20 + "\n"
            
    if resultados:
        messagebox.showinfo("Resultados da Busca", resultados)
    else:
        messagebox.showwarning("Aviso", "Nenhum ativo foi encontrado com esse termo.")
            
# Requisito 5: Atualizar Ativo

def atualizar_ativo():
    id_ativo = simpledialog.askinteger("Atualizar Ativo", "Digite o ID do ativo que deseja atualizar:")
    if id_ativo is None: return
    
    if id_ativo not in inventario_ativos:
        messagebox.showerror("Erro", "Ativo não encontrado no sistema.")
        return
    
    
    ativo = inventario_ativos[id_ativo]
    
    novo_nome = simpledialog.askstring("Atualizar Ativo", f"Nome atual ({ativo['nome']}):\n(Cancele ou deixe em branco para manter)")
    if novo_nome: ativo["nome"] = novo_nome.strip()
    
    novo_responsavel = simpledialog.askstring("Atualizar Ativo", f"Responsável atual ({ativo['responsavel']}):")
    if novo_responsavel: ativo["responsavel"] = novo_responsavel.strip()
    
    novo_setor = simpledialog.askstring("Atualizar Ativo", f"Setor atual ({ativo['setor']}):")
    if novo_setor: ativo["setor"] = novo_setor.strip()

    salvar_dados()
    messagebox.showinfo("Sucesso", "Ativo atualizado com sucesso!") 

# Requisito 6: Remover Ativo


def remover_ativo():
    id_ativo = simpledialog.askinteger("Remover Ativo", "Digite o ID do ativo a ser removido:")
    if id_ativo is None: return
    
    if id_ativo in inventario_ativos:
        # Pede confirmação antes de apagar
        resposta = messagebox.askyesno("Confirmar", f"Tem certeza que deseja remover o ativo {id_ativo}?")
        if resposta:
            del inventario_ativos[id_ativo]
            salvar_dados()
            messagebox.showinfo("Sucesso", "Ativo removido com sucesso!")
    else:
        messagebox.showerror("Erro", "Ativo não encontrado.")

# Requisito 7: Cadastrar vulnerabilidades

def cadastrar_vulnerabilidade():
    id_ativo = simpledialog.askinteger("Cadastrar Vulnerabilidade", "Digite o ID do ativo:")
    if id_ativo is None: return
    
    if id_ativo not in inventario_ativos:
        messagebox.showerror("Erro", "Ativo não encontrado no sistema.")
        return
        
    descricao = simpledialog.askstring("Vulnerabilidade", "Descrição da vulnerabilidade:")
    if not descricao: return
    
    severidade = simpledialog.askstring("Vulnerabilidade", "Severidade (Baixa, Média, Alta, Crítica):")
    if not severidade: return

# Exibindo as opções do Enum Tratamento
    
    opcoes_status = "Status disponíveis:\n"
    for status in Tratamento:
        opcoes_status += f"{status.value} - {status.name}\n"
    

    codigo_status = simpledialog.askinteger("Vulnerabilidade", f"{opcoes_status}\nEscolha o código do status:")
    if codigo_status is None: return

    try:
        status_selecionado = Tratamento(codigo_status).name
    except ValueError:
        messagebox.showerror("Erro", "Código de status inválido.")
        return
    
# Salvando no dicionário com o novo campo "status"
    
    inventario_ativos[id_ativo]["vulnerabilidades"].append({
        "descricao": descricao,
        "severidade": severidade,
        "status": status_selecionado
    })
    
    salvar_dados()
    messagebox.showinfo("Sucesso", "Vulnerabilidade cadastrada com sucesso!")

# Requisito 8: Visualizar Vulnerabilidades de um Ativo

def listar_vulnerabilidades():
    id_ativo = simpledialog.askinteger("Listar Vulnerabilidades", "Digite o ID do ativo:")
    if id_ativo is None: return
    
    if id_ativo not in inventario_ativos:
        messagebox.showerror("Erro", "Ativo não encontrado no sistema.")
        return
        
    vulnerabilidades = inventario_ativos[id_ativo]["vulnerabilidades"]
    
    if not vulnerabilidades:
        messagebox.showinfo("Vulnerabilidades", "Nenhuma vulnerabilidade cadastrada para este ativo.")
        return
        
    resultado = f"Vulnerabilidades do Ativo [ID: {id_ativo}] - {inventario_ativos[id_ativo]['nome']}:\n\n"
    for idx, vuln in enumerate(vulnerabilidades, start=1):
        # Usa .get() para evitar erro com dados antigos do JSON
        status_atual = vuln.get('status', 'NÃO INFORMADO')
        resultado += f"{idx}. Descrição: {vuln['descricao']}\n   Severidade: {vuln['severidade']}\n\n Status: {status_atual}\n\n"
        
    messagebox.showinfo("Vulnerabilidades", resultado)


# Interface Gráfica Principal (Menu)

def iniciar_gui():
    carregar_dados()  # Carrega os dados antes de abrir a janela
    
    janela = tk.Tk()
    janela.title("Sistema de Inventário de TI")
    janela.geometry("450x450")
    
    # Título
    titulo = tk.Label(janela, text="Inventário de TI e Vulnerabilidades", font=("Arial", 14, "bold"))
    titulo.pack(pady=20)
    
    # Botões do Menu
    estilo_botao = {"width": 35, "pady": 5, "bg": "#f0f0f0"}
    
    tk.Button(janela, text="1. Cadastrar Ativo", command=cadastrar_ativo, **estilo_botao).pack(pady=5)
    tk.Button(janela, text="2. Consultar Ativo", command=consultar_ativo, **estilo_botao).pack(pady=5)
    tk.Button(janela, text="3. Atualizar Ativo", command=atualizar_ativo, **estilo_botao).pack(pady=5)
    tk.Button(janela, text="4. Remover Ativo", command=remover_ativo, **estilo_botao).pack(pady=5)
    tk.Button(janela, text="5. Cadastrar Vulnerabilidade", command=cadastrar_vulnerabilidade, **estilo_botao).pack(pady=5)
    tk.Button(janela, text="6. Consultar Vulnerabilidades de um Ativo", command=listar_vulnerabilidades, **estilo_botao).pack(pady=5)
    
    # Botão de sair
    tk.Button(janela, text="0. Sair", command=janela.quit, width=20, bg="#ffcccc").pack(pady=30)
    
    janela.mainloop()

if __name__ == "__main__":
    iniciar_gui()