from PyQt5.QtWidgets import (QWidget, QTextEdit, QPushButton, QVBoxLayout,
                             QLabel, QGraphicsScene, QGraphicsView, QGraphicsTextItem)
from PyQt5.QtGui import QFont
from parser import SANParser
from tree import GameTree

class ChessApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chess SAN Parser")
        self.setGeometry(200, 200, 900, 700)

        self.parser = SANParser()
        self.tree_builder = GameTree()

        self.editor = QTextEdit()
        self.button = QPushButton("Parse and Show Tree")
        self.result = QLabel()
        self.result.setFont(QFont("Arial", 6))
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)

        layout = QVBoxLayout()
        layout.addWidget(self.editor)
        layout.addWidget(self.button)
        layout.addWidget(self.result)
        layout.addWidget(self.view)
        self.setLayout(layout)

        self.button.clicked.connect(self.on_parse_click)

    def on_parse_click(self):
        self.scene.clear()
        text = self.editor.toPlainText()
        try:
            turns = self.parser.parse_game(text)
            root = self.tree_builder.build_tree(turns)
            self.result.setText("Game is valid. Displaying tree...")
            self.draw_tree(root, 400, 20, 200)
        except ValueError as e:
            self.result.setText(str(e))

    def draw_tree(self, node, x, y, offset):
        if not node or node.value == "":
            return
        item = QGraphicsTextItem(node.value)
        item.setPos(x, y)
        self.scene.addItem(item)

        if node.left:
            self.scene.addLine(x + 30, y + 20, x - offset + 30, y + 70)
            self.draw_tree(node.left, x - offset, y + 80, offset / 1)

        if node.right:
            self.scene.addLine(x + 30, y + 20, x + offset + 30, y + 70)
            self.draw_tree(node.right, x + offset, y + 80, offset / 1)