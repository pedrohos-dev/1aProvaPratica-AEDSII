"""
Módulo: analysis
Fase 5 – Geração de gráficos e análise dos resultados
Prova 01 – Árvores de Pesquisa (BST e B-tree)
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# =============================================================
# Funções de leitura e preparação
# =============================================================

def load_results(file_path: str) -> pd.DataFrame:
    """Lê o CSV e retorna um DataFrame pandas."""
    df = pd.read_csv(file_path)
    print(f"Arquivo carregado: {file_path} ({len(df)} linhas)")
    return df


def summarize_bst(df_bst: pd.DataFrame) -> pd.DataFrame:
    """Calcula média de comparações por n e tipo (ordenada/aleatória)."""
    summary = (
        df_bst.groupby(['type', 'n'])['comparisons']
        .mean()
        .reset_index()
        .sort_values('n')
    )
    return summary


def summarize_btree(df_btree: pd.DataFrame) -> pd.DataFrame:
    """Agrupa resultados da Árvore B por n e m (ordem)."""
    summary = (
        df_btree.groupby(['m', 'n'])['comparisons']
        .mean()
        .reset_index()
        .sort_values(['m', 'n'])
    )
    return summary


# =============================================================
# Gráficos
# =============================================================

def plot_bst(summary_bst: pd.DataFrame):
    """Gera o gráfico da BST (ordenada x aleatória)."""
    plt.figure(figsize=(8, 5))
    for tipo in summary_bst['type'].unique():
        df_tipo = summary_bst[summary_bst['type'] == tipo]
        plt.plot(df_tipo['n'], df_tipo['comparisons'], marker='o', label=f'BST {tipo}')
    plt.title("Número de comparações na BST")
    plt.xlabel("n (número de elementos)")
    plt.ylabel("Comparações médias")
    plt.legend()
    plt.grid(True)
    Path("results").mkdir(exist_ok=True)
    plt.savefig("results/grafico_bst.png", dpi=300)
    plt.show()


def plot_btree(summary_btree: pd.DataFrame):
    """Gera o gráfico da Árvore B (m = 2, 4, 6)."""
    plt.figure(figsize=(8, 5))
    for m in sorted(summary_btree['m'].unique()):
        df_m = summary_btree[summary_btree['m'] == m]
        plt.plot(df_m['n'], df_m['comparisons'], marker='o', label=f'Árvore B (m={m})')
    plt.title("Número de comparações na Árvore B")
    plt.xlabel("n (número de elementos)")
    plt.ylabel("Comparações médias")
    plt.legend()
    plt.grid(True)
    Path("results").mkdir(exist_ok=True)
    plt.savefig("results/grafico_btree.png", dpi=300)
    plt.show()


# =============================================================
# Execução principal
# =============================================================

def main():
    """Lê os resultados, resume e gera os gráficos da prova."""
    # === Ler arquivos ===
    df_bst = load_results("results/results_bst.csv")
    df_btree = load_results("results/results_btree.csv")

    # === Resumir dados ===
    summary_bst = summarize_bst(df_bst)
    summary_btree = summarize_btree(df_btree)

    # === Exibir tabelas resumidas ===
    print("\nResumo BST:")
    print(summary_bst.head(10))

    print("\nResumo B-tree:")
    print(summary_btree.head(10))

    # === Gerar gráficos ===
    plot_bst(summary_bst)
    plot_btree(summary_btree)


if __name__ == "__main__":
    main()
