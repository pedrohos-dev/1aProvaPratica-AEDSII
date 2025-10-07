#  Prova 01 – Árvores de Pesquisa (BST e Árvore B)
Disciplina: Algoritmos e Estruturas de Dados II
Instituição: CEFET-MG
Aluno: Pedro Henrique Oliveira Santos
Projeto: Prova 01 – Árvores de Pesquisa (BST e Árvore B)
Data: Outubro de 2025

Este projeto implementa e analisa experimentalmente o desempenho de duas estruturas clássicas de dados:
- **BST (Binary Search Tree)** — Árvore Binária de Pesquisa;
- **Árvore B** — Estrutura balanceada usada em bancos de dados.

O objetivo é comparar o número médio de comparações durante as operações de inserção, considerando diferentes volumes de dados e ordens da árvore B.

---

##  Estrutura do projeto

prova-01/
├── src/
│ ├── bst.py # Implementação da árvore binária de pesquisa
│ ├── btree.py # Implementação da árvore B
│ ├── experiments.py # Execução dos experimentos (fase 1–4)
│ ├── analysis.py # Geração dos gráficos e tabelas (fase 5)
│ └── utils/ # (opcional) funções auxiliares
│
├── results/
│ ├── results_bst.csv # Saída dos experimentos da BST
│ ├── results_btree.csv # Saída dos experimentos da Árvore B
│ ├── grafico_bst.png # Gráfico de comparações da BST
│ ├── grafico_btree.png # Gráfico de comparações da Árvore B
│ 
├── requirements.txt # Dependências do projeto
├── README.md # Este arquivo
└── run.sh # Script para executar o fluxo completo


##  Fases do projeto

| Fase | Descrição | Arquivo |
|------|------------|---------|
| 1 | Implementação da BST | `src/bst.py` |
| 2 | Implementação da Árvore B | `src/btree.py` |
| 3 | Criação dos experimentos comparativos | `src/experiments.py` |
| 4 | Execução e coleta dos resultados | `results/*.csv` |
| 5 | Geração de gráficos e análise | `src/analysis.py` |

---

##  Instalação

# Versão do Python
   Python 3.10+

```bash
# Clonar o repositório
git clone https://github.com/pedrohos-dev/1aProvaPratica-AEDSII.git

# Criar e ativar o ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Linux / Mac
# ou
.venv\Scripts\activate           # Windows

# Instalar as dependências
pip install -r requirements.txt