import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import subprocess

class GameSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chọn trò chơi")
        self.resize(300, 100)
        
        main_layout = QVBoxLayout()
        #main_layout.setAlignment(Qt.AlignCenter)
        
        logo_layout = QVBoxLayout()
        logo_layout.setAlignment(Qt.AlignCenter)
        
        logo_label = QLabel(self)
        assets_dir = os.path.join(os.getcwd(), 'Assets')
        pixmap = QPixmap(os.path.join(assets_dir, 'logo.png'))
        pixmap = pixmap.scaled(120, 120) 
        logo_label.setPixmap(pixmap)
        logo_layout.addWidget(logo_label)
        
        main_layout.addLayout(logo_layout) 

        btn_human_vs_human = QPushButton("Chơi người với người")
        btn_human_vs_human.clicked.connect(self.nguoivsnguoi)
        main_layout.addWidget(btn_human_vs_human)
        
        btn_human_vs_computer = QPushButton("Chơi người vs máy")
        btn_human_vs_computer.clicked.connect(self.nguoivsmay)
        main_layout.addWidget(btn_human_vs_computer)
        
        self.setLayout(main_layout)
    
    def nguoivsnguoi(self):
        game_file = os.path.join(os.getcwd(), 'game2.py')
        if os.path.exists(game_file):
            try:
                subprocess.Popen(['python', game_file])
                print("[Người dùng chọn]: Người vs Người")
            except FileNotFoundError:
                QMessageBox.critical(self, "Lỗi", "Không thể tìm thấy tệp game2.py")
        else:
            QMessageBox.critical(self, "Lỗi", "Không thể tìm thấy tệp game2.py")
    
    def nguoivsmay(self):
        game_file = os.path.join(os.getcwd(), 'game.py')
        if os.path.exists(game_file):
            try:
                subprocess.Popen(['python', game_file])
                print("[Người dùng chọn]: Người vs Máy")
            except FileNotFoundError:
                QMessageBox.critical(self, "Lỗi", "Không thể tìm thấy tệp game.py")
        else:
            QMessageBox.critical(self, "Lỗi", "Không thể tìm thấy tệp game.py")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game_selector = GameSelector()
    game_selector.show()
    sys.exit(app.exec_())
