from PyQt5 import QtCore, QtGui, QtWidgets

class subVent(object):

    def __style__(self): 
        with open('./styles/style-subVent.css') as f: txt = f.read()
        return txt
    
    def setupUi(self, Form, geo=[817, 210, 564, 362], text='Hola Mundo!'):
        #* Ubicar Izquierda o Derecha
        if geo[0] >= 390: x = (geo[0] - (geo[2] - 150))
        else: x = geo[0] + geo[2]

        if geo[1] <= 36: #* Ubicar Abajo
            y = geo[1] + geo[3]
            x = ( (geo[2] // 2) - 210) + geo[0]
        
        elif geo[1] >= 350: #* Ubicar Arriba
            y =  (100 + geo[1]) - geo[3]
            x = ( (geo[2] // 2) - 210) + geo[0]
        
        #* Ubicar a nivel
        else: y = ((geo[3]//2)-140) + geo[1]

        Form.setGeometry(QtCore.QRect(x, y, 420, 280))
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        Form.setStyleSheet(self.__style__())

        self.fr_fondo = QtWidgets.QFrame(Form)
        self.fr_fondo.setGeometry(QtCore.QRect(20, 10, 381, 251))
        self.fr_fondo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_fondo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_fondo.setObjectName("fr_fondo")

        self.btn_cerrar = QtWidgets.QPushButton(self.fr_fondo)
        self.btn_cerrar.setGeometry(QtCore.QRect(340, 20, 21, 23))
        self.btn_cerrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cerrar.setText("")
        self.btn_cerrar.setObjectName("btn_cerrar")
        
        self.lbl_message = QtWidgets.QLabel(self.fr_fondo)
        self.lbl_message.setGeometry(QtCore.QRect(30, 40, 271, 141))
        self.lbl_message.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_message.setObjectName("lbl_message")

        self.btn_continuar = QtWidgets.QPushButton(self.fr_fondo)
        self.btn_continuar.setGeometry(QtCore.QRect(240, 200, 111, 31))
        self.btn_continuar.setObjectName("btn_continuar")

        self.retranslateUi(Form, text)

        self.btn_cerrar.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def retranslateUi(self, Form, txt):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Mensaje"))
        self.lbl_message.setText(_translate("Form", f"{txt}"))
        self.btn_continuar.setText(_translate("Form", "Continuar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    Form = QtWidgets.QWidget()
    ui = subVent()
    ui.setupUi(Form)
    Form.show()

    sys.exit(app.exec_())

#* De: Francisco Velez
