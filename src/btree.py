"""
Módulo: btree
Implementa uma Árvore B de acordo com a definição usada em aula:

- Raiz: entre 1 e 2m registros
- Demais páginas: entre m e 2m registros e m+1 a 2m+1 descendentes
- Todas as folhas aparecem no mesmo nível

Autor: Pedro Henrique
Data: 2025-10
"""

from bisect import bisect_left

class BTreeNode:
    """Representa um nó (página) da Árvore B."""
    def __init__(self, m: int, leaf: bool = True):
        self.m = m  # ordem mínima
        self.keys: list[int] = []
        self.children: list[BTreeNode] = []
        self.leaf = leaf

    def is_full(self) -> bool:
        """Verifica se o nó atingiu o máximo (2m registros)."""
        return len(self.keys) >= 2 * self.m


class BTree:
    """Implementa uma Árvore B com a convenção brasileira (ordem m)."""

    def __init__(self, m: int = 2):
        if m < 1:
            raise ValueError("A ordem mínima de uma Árvore B deve ser pelo menos 1.")
        self.root = BTreeNode(m)
        self.m = m

    # =============================================================
    # Inserção
    # =============================================================
    def insert(self, key: int):
        """Insere uma chave na Árvore B seguindo a definição brasileira."""
        root = self.root

        # Caso a raiz esteja cheia (2m chaves), faz split antes de inserir
        if root.is_full():
            new_root = BTreeNode(self.m, leaf=False)
            new_root.children.append(root)
            self._split_child(new_root, 0)
            self.root = new_root
            self._insert_non_full(new_root, key)
        else:
            self._insert_non_full(root, key)

    def _insert_non_full(self, node: BTreeNode, key: int):
        """Insere uma chave num nó que ainda não está cheio."""
        if node.leaf:
            idx = bisect_left(node.keys, key)
            node.keys.insert(idx, key)
        else:
            # Localiza o filho correto
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1

            # Divide o filho se ele estiver cheio
            if node.children[i].is_full():
                self._split_child(node, i)
                # Decidir em qual lado inserir após o split
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def _split_child(self, parent: BTreeNode, index: int):
        """Divide um nó filho cheio (2m chaves) e promove o registro central."""
        m = self.m
        node = parent.children[index]

        # Índice central
        mid = m  # separa após m chaves
        mid_key = node.keys[mid]

        # Cria o novo nó à direita
        right_node = BTreeNode(m, leaf=node.leaf)
        right_node.keys = node.keys[mid + 1 :]
        node.keys = node.keys[:mid]

        # Reatribui filhos, se não for folha
        if not node.leaf:
            right_node.children = node.children[mid + 1 :]
            node.children = node.children[: mid + 1]

        # Insere a chave mediana no pai
        parent.keys.insert(index, mid_key)
        parent.children.insert(index + 1, right_node)

    # =============================================================
    # Busca
    # =============================================================
    def search(self, key: int) -> tuple[bool, int]:
        """Busca uma chave na Árvore B e retorna (encontrou, comparações)."""
        return self._search_recursive(self.root, key, 0)

    def _search_recursive(self, node: BTreeNode, key: int, comparisons: int) -> tuple[bool, int]:
        i = 0
        while i < len(node.keys):
            comparisons += 1
            if key == node.keys[i]:
                return True, comparisons
            elif key < node.keys[i]:
                break
            i += 1

        if node.leaf:
            return False, comparisons
        return self._search_recursive(node.children[i], key, comparisons)

    # =============================================================
    # Percurso (debug)
    # =============================================================
    def traverse(self):
        """Percorre e imprime as chaves em ordem."""
        self._traverse(self.root)
        print()

    def _traverse(self, node: BTreeNode):
        for i in range(len(node.keys)):
            if not node.leaf:
                self._traverse(node.children[i])
            print(node.keys[i], end=" ")
        if not node.leaf:
            self._traverse(node.children[-1])


# =============================================================
# Teste rápido
# =============================================================
if __name__ == "__main__":
    print(" Teste da Árvore B:")
    b = BTree(m=2)
    for k in range(1, 21):
        b.insert(k)
    b.traverse()
    print("\nBusca por 7:", b.search(7))
    print("Busca por 100001:", b.search(100001))
