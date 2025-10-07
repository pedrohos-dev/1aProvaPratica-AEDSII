"""
Módulo: bst
Implementa uma Árvore Binária de Pesquisa (Binary Search Tree)
usando inserção e busca iterativas para suportar grandes valores de n.

Autor: Pedro Henrique
Data: 2025-10
"""

class Node:
    """Representa um nó da árvore binária."""
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Implementa uma Árvore Binária de Pesquisa (BST).
    - Inserção e busca são iterativas (para evitar recursão profunda).
    - A busca retorna também o número de comparações realizadas.
    """

    def __init__(self):
        self.root = None

    def insert(self, key: int):
        """Insere um novo valor na árvore de forma iterativa."""
        new_node = Node(key)

        # Caso 1: árvore vazia
        if self.root is None:
            self.root = new_node
            return

        # Caso 2: procurar o local correto para inserir
        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, key: int) -> tuple[bool, int]:
        """
        Busca um valor na árvore e retorna (encontrado, comparações).
        Cada comparação entre 'key' e 'node.key' é contabilizada.
        """
        comparisons = 0
        current = self.root

        while current is not None:
            comparisons += 1  # Comparação com o nó atual
            if key == current.key:
                return True, comparisons
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        # Se chegar aqui, o elemento não existe
        return False, comparisons

    def inorder(self) -> list[int]:
        """Retorna uma lista com os valores em ordem crescente."""
        result = []
        stack = []
        current = self.root

        # Percurso in-order iterativo
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                result.append(current.key)
                current = current.right

        return result


if __name__ == "__main__":
    # Pequeno teste local (executar: python src/bst.py)
    bst = BinarySearchTree()
    for key in [5, 2, 8, 1, 3]:
        bst.insert(key)

    print("Árvore (in-order):", bst.inorder())
    print("Busca por 3:", bst.search(3))
    print("Busca por 100001:", bst.search(100001))
