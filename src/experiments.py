"""
Módulo: experiments
Executa os experimentos da Prova 01 com:
- Árvore Binária de Pesquisa (BST)
- Árvore B  (ordem m)

"""

import random
import csv
import time
from tqdm import tqdm
from bst import BinarySearchTree      
from btree import BTree

# =============================================================
# Funções utilitárias
# =============================================================

def save_results_csv(filename: str, results: list[dict]):
    """Salva resultados em um arquivo CSV."""
    if not results:
        print("Nenhum resultado para salvar.")
        return
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    print(f"Resultados salvos em: {filename}")


# =============================================================
# Experimentos com BST 
# =============================================================

def run_bst_experiments(ns: list[int], repeats: int = 10) -> list[dict]:
    """
    Executa experimentos da BST:
    - Inserção ordenada
    - Inserção aleatória
    Busca pelo elemento 100001 e registra o número de comparações.
    """
    results = []
    for n in tqdm(ns, desc="BST Experiments"):
        # Inserção ordenada
        ordered_data = list(range(1, n + 1))
        for run in range(repeats):
            bst = BinarySearchTree()
            for key in ordered_data:
                bst.insert(key)
            _, comps = bst.search(100001)
            results.append({
                'tree': 'bst',
                'type': 'ordered',
                'm': '-',
                'n': n,
                'run': run,
                'comparisons': comps
            })

        # Inserção aleatória
        for run in range(repeats):
            data = list(range(1, n + 1))
            random.shuffle(data)
            bst = BinarySearchTree()
            for key in data:
                bst.insert(key)
            _, comps = bst.search(100001)
            results.append({
                'tree': 'bst',
                'type': 'random',
                'm': '-',
                'n': n,
                'run': run,
                'comparisons': comps
            })
    return results


# =============================================================
# Experimentos com Árvore B 
# =============================================================

def run_btree_experiments(ns: list[int], m_values: list[int] = [2, 4, 6]) -> list[dict]:
    """
    Executa experimentos para Árvore B de ordens m = 2, 4, 6.
    Cada árvore é construída com inserções ordenadas (1..n)
    e medida a busca pelo elemento 100001.
    """
    results = []
    for m in m_values:
        for n in tqdm(ns, desc=f"BTree (m={m})"):
            btree = BTree(m=m)
            for key in range(1, n + 1):
                btree.insert(key)
            _, comps = btree.search(100001)
            results.append({
                'tree': 'btree',
                'type': 'ordered',
                'm': m,
                'n': n,
                'run': 0,
                'comparisons': comps
            })
    return results


# =============================================================
# Execução principal
# =============================================================

def main():
    """Executa apenas os experimentos da Árvore B e gera CSV."""
    ns = list(range(10000, 100001, 10000))  # 10k, 20k, ..., 100k

    print("\nIniciando experimentos da BST...")              
    start = time.perf_counter()                                 
    bst_results = run_bst_experiments(ns)                       
    save_results_csv("results/results_bst.csv", bst_results)    
    print(f"Tempo total BST: {time.perf_counter() - start:.2f}s\n")  

    print("\n Iniciando experimentos da Árvore B (definição brasileira)...")
    start = time.perf_counter()
    btree_results = run_btree_experiments(ns)
    save_results_csv("results/results_btree.csv", btree_results)
    print(f"Tempo total BTree: {time.perf_counter() - start:.2f}s\n")


if __name__ == "__main__":
    main()
