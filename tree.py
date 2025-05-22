class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None   # white move
        self.right = None  # black move

class GameTree:
    def __init__(self):
        self.root = TreeNode("Partida")

    def build_tree(self, turns):
        current_parent = self.root
        for num, white, black in turns:
            white_node = TreeNode(f"{num}. {white}")
            black_node = TreeNode(f"{num}... {black}" if black else "")

            current_parent.left = white_node
            if black:
                current_parent.right = black_node
                current_parent = black_node
            else:
                current_parent = white_node

        return self.root