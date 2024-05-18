import requests
import PyQt5
from PyQt5.QtWidgets import *
app = QApplication([])

window = QWidget()
window.resize(700,500)


qest_btn = QPushButton("Друкувати")
answer_text = QTextEdit()
answer_text1 = QTextEdit()
answer_text2 = QTextEdit()

mine_line = QHBoxLayout()

h1 = QVBoxLayout()
h1.addWidget(answer_text)
h1.addWidget(answer_text1)
h1.addWidget(answer_text2)
h1.addWidget(qest_btn)

mine_line.addLayout(h1)

window.setLayout(mine_line)

window.show()
app.exec()