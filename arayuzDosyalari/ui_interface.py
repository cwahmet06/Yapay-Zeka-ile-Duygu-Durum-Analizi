import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QFrame

class DuyguAnaliziUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Duygu Analizi")
        self.setWindowIcon(QIcon("kapak.png"))
        self.setGeometry(100, 100, 1280, 720)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)

        left_frame = QFrame()
        left_frame.setFrameShape(QFrame.StyledPanel)
        left_frame.setFrameShadow(QFrame.Raised)
        left_layout = QVBoxLayout(left_frame)

        right_frame = QFrame()
        right_frame.setFrameShape(QFrame.StyledPanel)
        right_frame.setFrameShadow(QFrame.Raised)
        right_layout = QVBoxLayout(right_frame)

        main_layout.addWidget(left_frame)
        main_layout.addWidget(right_frame)

        ARKAPLAN = QLabel()
        ARKAPLAN.setStyleSheet("image: url(:/arkaplan/qrc/40op.png);")
        BASLIK = QLabel("GÖRÜNTÜ İLE DUYGU DURUM ANALİZİ")
        BASLIK.setFont(QtGui.QFont('Arial', 20))
        LOGO = QLabel()
        LOGO.setStyleSheet("image: url(:/arkaplan/qrc/suLOGO.jpg);")
        calistirBtn = QPushButton("Çalıştır")
        bilgiBtn = QPushButton("Bilgi")
        linkdnBtn = QPushButton("LinkedIn")
        egitimBtn = QPushButton("Eğitim")
        dgrlndrmeTestBtn = QPushButton("Analiz (TEST)")
        consoleTxtEdit = QTextEdit()

        left_layout.addWidget(ARKAPLAN)
        left_layout.addWidget(BASLIK)
        left_layout.addWidget(LOGO)
        left_layout.addWidget(calistirBtn)
        left_layout.addWidget(bilgiBtn)
        left_layout.addWidget(linkdnBtn)
        left_layout.addWidget(egitimBtn)
        left_layout.addWidget(dgrlndrmeTestBtn)

        right_layout.addWidget(consoleTxtEdit)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DuyguAnaliziUI()
    window.show()
    sys.exit(app.exec_())
