import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(724, 450)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 704, 329))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.labelImg = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelImg.setStyleSheet("background-color: rgb(47, 47, 47);")
        self.labelImg.setText("")
        self.labelImg.setObjectName("labelImg")
        self.gridLayout.addWidget(self.labelImg, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 5)
        self.inputAbrir = QtWidgets.QLineEdit(self.centralwidget)
        self.inputAbrir.setStyleSheet("background-color: rgb(18, 18, 18);\n"
"")
        self.inputAbrir.setObjectName("inputAbrir")
        self.gridLayout_2.addWidget(self.inputAbrir, 1, 0, 1, 4)
        self.btnEscolherArquivo = QtWidgets.QPushButton(self.centralwidget)
        self.btnEscolherArquivo.setStyleSheet("background-color: rgb(47, 47, 47);")
        self.btnEscolherArquivo.setObjectName("btnEscolherArquivo")
        self.gridLayout_2.addWidget(self.btnEscolherArquivo, 1, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.inputLargura = QtWidgets.QLineEdit(self.centralwidget)
        self.inputLargura.setStyleSheet("background-color: rgb(18, 18, 18);")
        self.inputLargura.setObjectName("inputLargura")
        self.gridLayout_2.addWidget(self.inputLargura, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 2, 1, 1)
        self.inputAltura = QtWidgets.QLineEdit(self.centralwidget)
        self.inputAltura.setStyleSheet("background-color: rgb(18, 18, 18);")
        self.inputAltura.setObjectName("inputAltura")
        self.gridLayout_2.addWidget(self.inputAltura, 2, 3, 1, 1)
        self.btnRedimensionar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRedimensionar.setStyleSheet("background-color: rgb(47, 47, 47);")
        self.btnRedimensionar.setObjectName("btnRedimensionar")
        self.gridLayout_2.addWidget(self.btnRedimensionar, 2, 4, 1, 1)
        self.btnSalvar = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalvar.setStyleSheet("background-color: rgb(47, 47, 47);")
        self.btnSalvar.setObjectName("btnSalvar")
        self.gridLayout_2.addWidget(self.btnSalvar, 3, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Redimensionar do EDU"))
        self.btnEscolherArquivo.setText(_translate("MainWindow", "Abrir Arquivo"))
        self.label.setText(_translate("MainWindow", "Largura:"))
        self.inputLargura.setToolTip(_translate("MainWindow", "<html><head/><body><p>fgfdgdf</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Altura:"))
        self.btnRedimensionar.setText(_translate("MainWindow", "Redimensionar"))
        self.btnSalvar.setText(_translate("MainWindow", "Salvar"))

class Janela(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnEscolherArquivo.clicked.connect(self.abrir_imagem)
        self.btnRedimensionar.clicked.connect(self.redimensionar)
        self.btnSalvar.clicked.connect(self.salvar)

    def abrir_imagem(self):
        img, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Imagem',
            '/home/duduka/Imagens')
        self.inputAbrir.setText(img)
        self.original_img = QPixmap(img)
        self.labelImg.setPixmap(self.original_img)
        self.inputLargura.setText(str(self.original_img.width()))
        self.inputAltura.setText(str(self.original_img.height()))

    def redimensionar(self):
        largura = int(self.inputLargura.text())
        self.nova_imagem = self.original_img.scaledToWidth(largura)
        self.labelImg.setPixmap(self.nova_imagem)
        self.inputLargura.setText(str(self.nova_imagem.width()))
        self.inputAltura.setText(str(self.nova_imagem.height()))

    def salvar(self):
        img, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar Imagem',
            '/home/duduka/Imagens')
        self.nova_imagem.save(img, 'PNG')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    janela = Janela()
    janela.show()
    qt.exec_()