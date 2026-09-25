# Sistema de Inventário de TI e Vulnerabilidades

Projeto desenvolvido em **Python** com o objetivo de criar um sistema simples de gerenciamento de ativos de Tecnologia da Informação e suas respectivas vulnerabilidades.

O sistema funciona através do terminal e permite cadastrar, consultar, atualizar e remover ativos, além de registrar e visualizar vulnerabilidades associadas a cada equipamento.

---

## Sobre o Projeto

O projeto consiste em um sistema de **Inventário de Ativos de TI**, permitindo armazenar informações sobre equipamentos e aplicações da organização.

Cada ativo possui informações como:

* ID único;
* Nome ou Hostname;
* Responsável;
* Setor;
* Tipo do ativo;
* Lista de vulnerabilidades.

Além do gerenciamento dos ativos, o sistema também possibilita o cadastro de vulnerabilidades, contendo:

* Descrição;
* Categoria;
* Severidade;
* Status de tratamento.

Os dados cadastrados são armazenados em um arquivo **JSON**, permitindo que as informações continuem disponíveis após o programa ser encerrado.

---

## Funcionalidades

O sistema possui as seguintes funcionalidades:

### 1. Cadastrar Ativo

Permite cadastrar um novo ativo no inventário.

Durante o cadastro são solicitadas informações como:

* ID único;
* Nome/Hostname;
* Responsável;
* Setor;
* Tipo do ativo.

O sistema verifica se o ID informado já existe antes de realizar o cadastro.

---

### 2. Consultar Ativo

Permite pesquisar um ativo utilizando:

* ID;
* Nome ou parte do nome.

Ao encontrar o ativo, o sistema apresenta:

* ID;
* Nome/Hostname;
* Responsável;
* Setor;
* Tipo;
* Quantidade de vulnerabilidades cadastradas.

---

### 3. Atualizar Ativo

Permite alterar informações de um ativo já cadastrado.

É possível atualizar:

* Nome;
* Responsável;
* Setor.

Caso o usuário não queira alterar determinado campo, basta pressionar **Enter** sem digitar um novo valor.

---

### 4. Remover Ativo

Permite excluir um ativo do inventário através do seu ID.

Ao remover um ativo, suas vulnerabilidades associadas também são removidas.

---

### 5. Cadastrar Vulnerabilidade

Permite cadastrar uma vulnerabilidade para um ativo existente.

São armazenadas as seguintes informações:

* Descrição;
* Categoria;
* Severidade;
* Status de tratamento.

---

### 6. Consultar Vulnerabilidades

Permite visualizar todas as vulnerabilidades cadastradas para um determinado ativo.

Para cada vulnerabilidade são exibidos:

* Descrição;
* Categoria;
* Severidade;
* Status de tratamento.

---

## Estrutura do Projeto

```text
projeto/
│
├── main.py
├── menu.py
├── ativos.py
├── vulnerabilidades.py
├── persistencia.py
├── dados.py
├── enums.py
└── dados_inventario.json
```

### `main.py`

Arquivo responsável por iniciar o programa.

Ele carrega os dados existentes e executa o menu principal da aplicação.

### `menu.py`

Contém o menu principal do sistema e direciona o usuário para cada funcionalidade.

As opções disponíveis são:

```text
1 - Cadastrar Ativo
2 - Consultar Ativo
3 - Atualizar Ativo
4 - Remover Ativo
5 - Cadastrar Vulnerabilidade
6 - Consultar Vulnerabilidades de um Ativo
0 - Sair
```

### `ativos.py`

Responsável pelas principais operações relacionadas aos ativos:

* Cadastro;
* Consulta;
* Atualização;
* Remoção.

### `vulnerabilidades.py`

Responsável pelo gerenciamento das vulnerabilidades dos ativos.

Possui funcionalidades para:

* Cadastrar vulnerabilidades;
* Consultar vulnerabilidades.

### `persistencia.py`

Responsável pela leitura e gravação das informações.

Os dados são armazenados no arquivo:

```text
dados_inventario.json
```

O módulo utiliza a biblioteca nativa `json` do Python.

### `dados.py`

Contém o dicionário principal utilizado durante a execução do sistema:

```python
inventario_ativos = {}
```

Esse dicionário armazena todos os ativos cadastrados.

### `enums.py`

Contém os `Enum` utilizados para padronizar determinadas informações do sistema.

#### Tipos de Ativo

```text
1 - SERVIDOR
2 - ROTEADOR
3 - NOTEBOOK
4 - APLICAÇÃO_WEB
```

#### Severidade da Vulnerabilidade

```text
1 - BAIXA
2 - MEDIA
3 - ALTA
4 - CRITICA
```

#### Status de Tratamento

```text
1 - ABERTO
2 - EM_TRATAMENTO
3 - CORRIGIDA
4 - ACEITA
```

---

## Persistência dos Dados

O projeto utiliza um arquivo JSON para salvar as informações cadastradas.

Arquivo utilizado:

```text
dados_inventario.json
```

Sempre que um ativo ou vulnerabilidade é cadastrado, atualizado ou removido, os dados são salvos novamente no arquivo.

Ao iniciar o programa, os dados existentes são carregados para o dicionário `inventario_ativos`.

Isso permite que os registros não sejam perdidos quando o programa for encerrado.

---

## Estrutura de um Ativo

Internamente, cada ativo segue uma estrutura semelhante a:

```python
{
    "nome": "Servidor Principal",
    "responsavel": "João",
    "setor": "TI",
    "tipo": "SERVIDOR",
    "vulnerabilidades": []
}
```

O ID do ativo é utilizado como chave no dicionário principal.

Exemplo:

```python
inventario_ativos[1] = {
    "nome": "Servidor Principal",
    "responsavel": "João",
    "setor": "TI",
    "tipo": "SERVIDOR",
    "vulnerabilidades": []
}
```

---

## Estrutura de uma Vulnerabilidade

Cada vulnerabilidade é adicionada à lista de vulnerabilidades do ativo.

Exemplo:

```python
{
    "descricao": "Sistema operacional desatualizado",
    "categoria": "Software",
    "severidade": "ALTA",
    "status": "ABERTO"
}
```

Dessa forma, um mesmo ativo pode possuir várias vulnerabilidades cadastradas.

---

## Como Executar

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

Depois entre na pasta:

```bash
cd NOME_DO_REPOSITORIO
```

### 2. Verifique se o Python está instalado

Execute:

```bash
python --version
```

ou:

```bash
python3 --version
```

### 3. Execute o programa

```bash
python main.py
```

Dependendo do sistema operacional:

```bash
python3 main.py
```

---

## Exemplo de Execução

Ao executar o projeto será apresentado o menu:

```text
--- Sistema de Inventário de TI e Vulnerabilidades ---

1. Cadastrar Ativo
2. Consultar Ativo
3. Atualizar Ativo
4. Remover Ativo
5. Cadastrar Vulnerabilidade
6. Consultar Vulnerabilidades de um Ativo
0. Sair
```

O usuário deve informar o número correspondente à operação desejada.

---

## Tecnologias Utilizadas

* Python
* JSON
* Enum
* Manipulação de arquivos
* Dicionários
* Listas
* Funções
* Tratamento de exceções
* Programação modular

O projeto utiliza apenas recursos da biblioteca padrão do Python, não sendo necessária a instalação de bibliotecas externas para as funcionalidades atuais.

---

## Conceitos Aplicados

Durante o desenvolvimento foram aplicados conceitos importantes da linguagem Python, como:

* Modularização do código;
* Funções;
* Estruturas condicionais;
* Estruturas de repetição;
* Dicionários;
* Listas;
* `Enum`;
* Manipulação de arquivos JSON;
* Tratamento de exceções com `try` e `except`;
* Validação de entrada de dados;
* Importação entre módulos.

---

## Fluxo da Aplicação

O funcionamento geral do sistema pode ser representado da seguinte forma:

```text
main.py
   │
   ├── Carrega os dados
   │
   ▼
menu.py
   │
   ├── Gerenciamento de Ativos
   │      ├── Cadastrar
   │      ├── Consultar
   │      ├── Atualizar
   │      └── Remover
   │
   ├── Gerenciamento de Vulnerabilidades
   │      ├── Cadastrar
   │      └── Consultar
   │
   ▼
persistencia.py
   │
   ▼
dados_inventario.json
```

---

## Objetivo Acadêmico

Este projeto foi desenvolvido como atividade acadêmica com o objetivo de aplicar, na prática, conceitos fundamentais de programação em Python.

Entre os principais objetivos estão:

* Desenvolver um sistema dividido em módulos;
* Trabalhar com estruturas de dados;
* Utilizar arquivos para persistência das informações;
* Implementar operações de cadastro, consulta, atualização e remoção;
* Realizar validações das entradas do usuário;
* Trabalhar com vulnerabilidades associadas aos ativos.

---

## Possíveis Melhorias Futuras

Algumas funcionalidades que podem ser adicionadas futuramente incluem:

* Validação mais completa dos campos;
* Alteração do tipo do ativo durante uma atualização;
* Atualização de vulnerabilidades;
* Remoção individual de vulnerabilidades;
* Filtros por severidade;
* Filtros por status;
* Relatórios de vulnerabilidades;
* Contagem de vulnerabilidades críticas;
* Interface gráfica;
* Banco de dados;
* Sistema de autenticação;
* Registro de datas de cadastro e atualização.

---

