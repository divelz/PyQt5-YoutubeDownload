from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):

    def __init__(self): self.inicio = True

    def __style__(self):
        with open('./style.qss', 'r') as f: txt = f.read()
        return txt
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 410)

        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        Form.setStyleSheet(self.__style__())

        self.fondo = QtWidgets.QFrame(Form)
        self.fondo.setGeometry(QtCore.QRect(20, 10, 560, 380))
        self.fondo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fondo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fondo.setObjectName("fondo")

        self.btn_descargar = QtWidgets.QPushButton(self.fondo)
        self.btn_descargar.setGeometry(QtCore.QRect(365, 170, 130, 35))
        self.btn_descargar.setObjectName("btn_descargar")
        
        self.lbl_autor = QtWidgets.QLabel(self.fondo)
        self.lbl_autor.setGeometry(QtCore.QRect(0, 330, 230, 50))
        self.lbl_autor.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_autor.setObjectName("lbl_autor")
        
        self.lbl_titulo = QtWidgets.QLabel(self.fondo)
        self.lbl_titulo.setGeometry(QtCore.QRect(70, 0, 420, 60))
        self.lbl_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_titulo.setObjectName("lbl_titulo")

        self.btn_cerrar = QtWidgets.QPushButton(self.fondo)
        self.btn_cerrar.setGeometry(QtCore.QRect(520, 20, 21, 23))
        self.btn_cerrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cerrar.setText("")
        self.btn_cerrar.setObjectName("btn_cerrar")

        self.btn_minimizar = QtWidgets.QPushButton(self.fondo)
        self.btn_minimizar.setGeometry(QtCore.QRect(20, 20, 21, 23))
        self.btn_minimizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_minimizar.setText("")
        self.btn_minimizar.setObjectName("btn_minimizar")

        self.txte_link = QtWidgets.QLineEdit(self.fondo)
        self.txte_link.setGeometry(QtCore.QRect(65, 170, 300, 35))
        self.txte_link.setText("")
        self.txte_link.setObjectName("txte_link")

        self.rdb_textVideo1 = QtWidgets.QRadioButton(self.fondo)
        self.rdb_textVideo1.setGeometry(QtCore.QRect(80, 80, 181, 25))
        self.rdb_textVideo1.setChecked(False)
        self.rdb_textVideo1.setObjectName("rdb_textVideo1")
        self.rdb_textVideo1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        self.rdb_textVideo2 = QtWidgets.QRadioButton(self.fondo)
        self.rdb_textVideo2.setGeometry(QtCore.QRect(80, 120, 311, 25))
        self.rdb_textVideo2.setChecked(True)
        self.rdb_textVideo2.setObjectName("rdb_textVideo2")
        self.rdb_textVideo2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.fr_progressBar1 = QtWidgets.QFrame(self.fondo)
        self.fr_progressBar1.setGeometry(QtCore.QRect(65, 230, 430, 80))
        self.fr_progressBar1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_progressBar1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_progressBar1.setObjectName("fr_progressBar1")

        self.fr_progressBar2 = QtWidgets.QFrame(self.fr_progressBar1)
        self.fr_progressBar2.setGeometry(QtCore.QRect(20, 10, 30, 30))
        self.fr_progressBar2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_progressBar2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_progressBar2.setObjectName("fr_progressBar2")

        self.lbl_info = QtWidgets.QLabel(self.fr_progressBar1)
        self.lbl_info.setGeometry(QtCore.QRect(25, 10, 380, 30))
        self.lbl_info.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_info.setObjectName("lbl_info")

        self.cbb_lang = QtWidgets.QComboBox(self.fondo)
        self.cbb_lang.setGeometry(QtCore.QRect(430, 80, 85, 35))
        self.cbb_lang.setObjectName("cbb_lang")
        self.cbb_lang.addItem("")
        self.cbb_lang.addItem("")

        self.retranslateUi(Form)

        self.cbb_lang.activated.connect(lambda: self.retranslateUi(Form))
        self.btn_minimizar.clicked.connect(Form.showMinimized)
        self.btn_cerrar.clicked.connect(Form.close)
 
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate

        self.num = 0 if ( self.cbb_lang.currentText().lower() == 'español' ) or self.inicio else 1
        self.inicio = False

        self.txt = {
            'title'    : ['Descargar Videos de Youtube', 'Download Youtube Videos'],
            'cbb1'     : ['Descargar video', 'Download video'],
            'cbb2'     : ['Descargar lista de reproducción', 'Download playlist'],
            'btn_desc' : ['Descargar', 'Download'],
            'bie'      : ['Bienvenido', 'Welcome'],
            'aut'      : ['Autor', 'Author'] 
        }

        Form.setWindowTitle(_translate("Form", 'Youtube Download'))

        self.btn_descargar.setText(_translate("Form", self.txt["btn_desc"][self.num]))
        self.lbl_autor.setText(_translate("Form", f'{self.txt["aut"][self.num]}: Francisco Velez'))
        self.lbl_titulo.setText(_translate("Form", self.txt["title"][self.num]))

        self.lbl_info.setText(_translate("Form", self.txt["bie"][self.num]))

        self.cbb_lang.setItemText(0, _translate("Form", "Español"))
        self.cbb_lang.setItemText(1, _translate("Form", "English"))

        self.rdb_textVideo1.setText(_translate("Form", self.txt["cbb1"][self.num]))
        self.rdb_textVideo2.setText(_translate("Form", self.txt["cbb2"][self.num]))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
