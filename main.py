from PyQt5 import QtWidgets ,QtCore
from PyQt5.QtWidgets import QDialog, QSplashScreen, QApplication, QTextEdit, QMainWindow ,QLabel
from PyQt5.QtCore import Qt, QSize
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap, QIcon
from subprocess import Popen, PIPE
import sys
import webbrowser
import time

# Ana uygulama sınıfı
class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        # Arayüz tasarımını yükle
        loadUi("arayuzDosyalari/interface.ui", self)
        # Baslik Eklendi
        self.setWindowTitle("DUYGU DURUM ANALİZİ")
        information_text = "##################################\n"
        information_text += "#                 DUYGU DURUM ANALİZİ                             #\n"
           information_text += "#           AHMET MERT KARAKOÇOĞLU                          #\n"
        information_text += "#                              203312049                                    #\n"
        information_text += "##################################"
        self.consoleTxtEdit.setPlainText(information_text)
        # Arkaplan ayarlari
        background_image = QPixmap(r'qrc/40op.jpg')
        background_label = QLabel(self)
        background_label.setPixmap(background_image)
        background_label.setGeometry(0, 0, 1280, 720)

        # Resmi arka planda tut
        background_label.setStyleSheet("position: absolute; z-index: -1;")
        background_label.setAttribute(Qt.WA_TransparentForMouseEvents)

        # Butonlara işlevsellik ekle
        self.egitimBtn.clicked.connect(self.egitimFunction)
        self.egitimBtn.setIcon(QIcon(r'icons/book-open.svg'))
        self.egitimBtn.setIconSize(QtCore.QSize(50, 50))
        self.egitimBtn.setGeometry(QtCore.QRect(20,109,131,71))
        self.dgrlndrmeTestBtn.clicked.connect(self.analizFunction)
        self.dgrlndrmeTestBtn.setIcon(QIcon(r'icons/alert-triangle.svg'))
        self.dgrlndrmeTestBtn.setIconSize(QtCore.QSize(50, 50))
        self.dgrlndrmeTestBtn.setGeometry(QtCore.QRect(19, 190, 141, 80))
        self.calistirBtn.clicked.connect(self.calistirFunction)
        self.calistirBtn.setIcon(QIcon(r'icons/arrow-right-circle.svg'))
        self.calistirBtn.setIconSize(QtCore.QSize(50, 50))
        self.calistirBtn.setGeometry(QtCore.QRect(9, 279, 151, 121))
        self.linkdnBtn.clicked.connect(self.openLinkedInProfile)
        self.linkdnBtn.setIcon(QIcon(r'icons/linkedin.svg'))
        self.linkdnBtn.setIconSize(QtCore.QSize(50, 50))
        self.linkdnBtn.setGeometry(QtCore.QRect(10, 409, 150, 81))
        self.bilgiBtn.clicked.connect(self.displayInformation)
        self.bilgiBtn.setIcon(QIcon(r'icons/info.svg'))
        self.bilgiBtn.setIconSize(QtCore.QSize(50, 50))
        self.bilgiBtn.setGeometry(QtCore.QRect(10, 490, 151, 91))
        self.logoBtn.clicked.connect(self.openSelcukEdu)
        self.logoBtn.setGeometry(QtCore.QRect(10, 10, 131, 81))

    def openSelcukEdu(self):
        # LinkedIn profiline gitmek için yapılacak işlev
        selcuk_url = "https://tf.selcuk.edu.tr/index.php?lang=tr&birim=033004&page=main"
        webbrowser.open(selcuk_url)

    def egitimFunction(self):
        # Eğitim butonuna tıklanınca yapılacak işlev
        # Eğitim penceresini aç
        self.consoleTxtEdit.clear()
        # Eğitim dosyasını çalıştır
        process = Popen(["python", "kokDosyalar/egitim.py"], stdout=PIPE, stderr=PIPE, text=True)
        stdout, stderr = process.communicate()
        # Logları arayüze ekle
        log_text = stdout + "\n" + stderr
        self.consoleTxtEdit.setPlainText(log_text)

    def analizFunction(self):
        # Analiz butonuna tıklanınca yapılacak işlev
        # Logları temizle
        self.consoleTxtEdit.clear()
        # Analiz dosyasını çalıştır
        process = Popen(["python", "kokDosyalar/degerlendirmeAnaliz.py"], stdout=PIPE, stderr=PIPE, text=True)
        stdout, stderr = process.communicate()
        # Logları arayüze ekle
        log_text = stdout + "\n" + stderr
        self.consoleTxtEdit.setPlainText(log_text)

    def calistirFunction(self):
        # Çalıştır butonuna tıklanınca yapılacak işlev
        # Logları temizle
        self.consoleTxtEdit.clear()
        # Çalıştır dosyasını çalıştır
        process = Popen(["python", "kokDosyalar/calistir.py"], stdout=PIPE, stderr=PIPE, text=True)
        stdout, stderr = process.communicate()
        # Logları arayüze ekle
        log_text = stdout + "\n" + stderr
        self.consoleTxtEdit.setPlainText(log_text)

    def openLinkedInProfile(self):
        # LinkedIn profiline gitmek için yapılacak işlev
        linkedin_url = "https://www.linkedin.com/in/ahmedovic/"
        webbrowser.open(linkedin_url)

    def displayInformation(self):
        # Bilgi butonuna tıklanınca yapılacak işlev
        # Bilgi metnini oluştur ve arayüze ekle

        information_text = "#####################################################\n"
        information_text += "#                                                                                                                                        #\n"
        information_text += "#  1) Eğitim  -> Veri setini egitir bilgisayarın hızına bağlı olarak 2-4 saat arasında sürer   #\n"
        information_text += "#  2) Analiz -> Yapılan eğitim dosyalarını (h5 ve json) çalışması için düzeltir                     #\n"
        information_text += "#  3) Çalıştır -> Uygulamayı çalıştırır                                                                                 #\n"
        information_text += "#  4) Linkedln -> Linkedln hesabıma yönlendirir                                                                #\n"
        information_text += "#  5) Bilgi -> İşte buradasınız :))                                                                                      #\n"
        information_text += "#                                                                                                                                       #\n"
        information_text += "####################################################\n"
        self.consoleTxtEdit.setPlainText(information_text)


# Ana uygulama başlatma işlevi
def main():
    # Uygulamayı oluştur
    app = QApplication(sys.argv)
    # Splash ekranı
    splash_pix = QPixmap('kapak.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()
    # 3 saniye bekle
    time.sleep(3)
    # Ana pencereyi oluştur ve göster
    mainWindow = MyApp()
    mainWindow.show()
    # Ana pencere gösterilince splash screen'i kapan
    splash.finish(mainWindow)
    # Uygulamayı çalıştır
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
