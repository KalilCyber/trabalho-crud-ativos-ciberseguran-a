import json
from enums import TipoAtivo, Severidade, Tratamento
from dados import inventario_ativos

# Configuração do arquivo json
ARQUIVO_DADOS = "dados_inventario.json"

# Funções Auxiliares de Arquivo
def salvar_dados():
    with open(ARQUIVO_DADOS, 'w') as f:
        json.dump(inventario_ativos, f, indent=4)

def carregar_dados():
    try:
        with open(ARQUIVO_DADOS, 'r') as f:
            # Carrega os dados do arquivo JSON
            dados_brutos = json.load(f)
            
            # Limpa o dicionário original que foi importado
            inventario_ativos.clear()
            
            # Preenche o MESMO dicionário com as chaves convertidas para inteiro
            for id_str, dados in dados_brutos.items():
                inventario_ativos[int(id_str)] = dados
                
    except FileNotFoundError:
        # Se o arquivo não existir, o dicionário simplesmente permanece vazio
        pass