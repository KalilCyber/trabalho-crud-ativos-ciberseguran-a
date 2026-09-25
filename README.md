# trabalho-crud-ativos-ciberseguran-apyt

# Trabalho CRUD Ativos - Cibersegurança (UFU)

Sistema de inventário de ativos de TI e gestão de vulnerabilidades desenvolvido em Python para o curso de Cibersegurança da Universidade Federal de Uberlândia (UFU). O projeto aplica conceitos de modularização, manipulação de arquivos JSON e uso de Enums para estruturação segura de dados.

## Funcionalidades da Sprint 1

O sistema opera via interface de linha de comando (CLI)[cite: 6] e inclui as seguintes operações principais:

*   **Gestão de Ativos:**
    *   Cadastrar novo ativo com validação de ID único (Requisito 3)[cite: 1].
    *   Consultar ativo existente buscando por ID ou Nome/Hostname (Requisito 4)[cite: 1].
    *   Atualizar informações de um ativo, alterando nome, responsável e setor (Requisito 5)[cite: 1].
    *   Remover ativo do inventário e excluir permanentemente suas vulnerabilidades atreladas (Requisito 6)[cite: 1].
*   **Gestão de Vulnerabilidades:**
    *   Cadastrar vulnerabilidade em um ativo específico informando descrição, categoria, severidade e status de tratamento (Requisito 7)[cite: 9].
    *   Listar todas as vulnerabilidades cadastradas em um determinado ativo (Requisito 8)[cite: 9].
*   **Persistência e Estrutura:**
    *   Carregamento e salvamento automático dos registros no arquivo `dados_inventario.json`[cite: 3, 7].
    *   Padronização de categorias utilizando classes Enum para `TipoAtivo`, `Severidade` e `Tratamento`[cite: 4].
    *   Armazenamento em memória utilizando um dicionário central de ativos[cite: 2].

## Tecnologias Utilizadas

*   Python 3.14.7: Linguagem principal de desenvolvimento[cite: 1, 5].
*   Módulo `json`: Utilizado para a persistência de dados no disco local[cite: 7].
*   Módulo `enum`: Utilizado para definir estruturas de dados rígidas e evitar erros de digitação[cite: 4].

## Arquitetura do Projeto

O código foi modularizado para separar responsabilidades e facilitar futuras implementações e manutenções:

*   `main.py`: Ponto de entrada da aplicação, responsável por iniciar o carregamento de dados e invocar o menu[cite: 5].
*   `menu.py`: Gerencia a interface de texto, recebendo as entradas do usuário e direcionando o fluxo para as funções correspondentes[cite: 6].
*   `ativos.py`: Contém as regras de negócio para as operações CRUD dos ativos de TI[cite: 1].
*   `vulnerabilidades.py`: Contém as regras de negócio para gerenciar e atrelar as vulnerabilidades aos ativos existentes[cite: 9].
*   `persistencia.py`: Isola as operações de leitura e escrita (`salvar_dados` e `carregar_dados`) no arquivo JSON[cite: 7].
*   `dados.py`: Inicializa a estrutura de dados principal do sistema (`inventario_ativos`)[cite: 2].
*   `enums.py`: Centraliza as constantes do sistema, definindo os tipos e níveis aceitos[cite: 4].

## Como Executar

1. Clone o repositório em sua máquina local.
2. Navegue até a pasta do projeto utilizando o terminal do seu sistema ou o terminal integrado do VS Code.
3. Execute o arquivo principal da aplicação:
   ```bash
   python main.py