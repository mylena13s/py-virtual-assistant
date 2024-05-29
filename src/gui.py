from PySide6.QtWidgets import QWidget, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

def setup_gui(callback):
    window = QWidget()
    window.setWindowTitle("Virtual Assistant: Wikipedia Voice Search")
    window.setGeometry(100, 100, 820, 600)
    
    layout = QVBoxLayout()
    layout.setContentsMargins(20, 20, 20, 20)
    layout.setSpacing(20)

    title_label = QLabel("Virtual Assistant")
    title_label.setAlignment(Qt.AlignCenter)
    title_label.setFont(QFont("Arial", 24, QFont.Bold))
    title_label.setStyleSheet("color: #007BFF;")
    layout.addWidget(title_label)

    response_text = QTextEdit()
    response_text.setReadOnly(True)
    response_text.setFont(QFont("Arial", 14))
    response_text.setStyleSheet("color: #333333; background-color: #f5f5f5; border: 1px solid #dddddd; border-radius: 10px; padding: 10px;")
    layout.addWidget(response_text, stretch=1)
    
    button_layout = QHBoxLayout()
    button_layout.setAlignment(Qt.AlignCenter)

    listen_button = QPushButton("Listen")
    listen_button.setFixedHeight(50)
    listen_button.setFixedWidth(200)
    listen_button.setFont(QFont("Arial", 16, QFont.Bold))
    listen_button.setStyleSheet("color: #ffffff; background-color: #007BFF; border: none; border-radius: 25px; padding: 10px;")
    listen_button.clicked.connect(lambda: callback(response_text))
    button_layout.addWidget(listen_button)

    layout.addLayout(button_layout)
    
    window.setLayout(layout)
    window.show()
    
    return window, response_text
