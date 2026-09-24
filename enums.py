from enum import Enum

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