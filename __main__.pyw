from Ui_download import Ui_Form, QtWidgets, QtCore
from pytube import Playlist, YouTube
from notifypy import Notify 
import sys, os, threading

class MainApp(QtWidgets.QMainWindow): 

    def __init__(self, parent=None, *args): 
        super(MainApp, self).__init__(parent=parent) 
        self.num, self.error, self.numVideo = 0, 0, 0
        self.NameApp = 'Youtube Download'
        
        self.progress = False
        self.notify = True
        self.bar_ = True

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        #? Mover ventana
        self.ui.fondo.mouseMoveEvent = self.mover_ventana
        self.ui.btn_descargar.clicked.connect(self.download)

    ##? mover ventana
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def mover_ventana(self, event):
        if self.isMaximized() == False: 
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
    
    def animation_txt(self): 
        self.ui.lbl_info.setGeometry(25, self.corY, 380, 30)
        self.corY += 1

        if self.corY >= 41 and not(self.progress): self.timer1.stop()

    def animation_barra(self): 
        self.ui.fr_progressBar2.setGeometry(self.porcent, 10, 30, 30)

        self.porcent += 1 if self.bar_ else -1

        if (self.porcent >= self.hasta and self.bar_): self.bar_ = False 

        if (self.porcent <= 21 and not(self.bar_) ): 

            if self.progress: 
                self.ui.lbl_info.setGeometry(QtCore.QRect(25, 10, 380, 30))
                self.ui.lbl_info.setText(self.ui.txt['bie'][self.ui.num])        
                self.timer2.stop()

            self.bar_ = True
    
    def runAnimationBarra(self, porcent=20, hasta=381, time=5):
        self.porcent = porcent
        self.hasta  = hasta
        self.timer2 = QtCore.QTimer()
        self.timer2.timeout.connect(self.animation_barra)
        self.timer2.start(time)

    def download(self):
        if self.ui.txte_link.text() == '': 
            self.notificacion('Error', 'Campo de texto Vacio', self.NameApp)
            return
        
        self.corY = 10
        self.timer1 = QtCore.QTimer()
        self.timer1.timeout.connect(self.animation_txt)
        self.timer1.start(10)
        
        try:
            self.runAnimationBarra()

            if not self.ui.rdb_textVideo1.isChecked(): # Lista de reproduccion 
                t1 = threading.Thread(name='hilo_1', target=self.descargarLista)
                t1.start()
                
                # self.timer_ = QtCore.QTimer()
                # self.timer_.timeout.connect(self.animation_barra)
                # self.timer_.start()

            else: # un solo video 
                t2 = threading.Thread(name='hilo_2', target=(lambda: self.descargarVideo(True)) )
                t2.start()

        except: self.notificacion('Error', 'Error al descargar la informacion.', self.NameApp)

    def descargarLista(self):
        self.ui.lbl_info.setText('<p style="color: rgb(165, 255, 249);">Descargando Urls...</p>')
        self.ui.lbl_info.setText( self.get_Url(self.ui.txte_link.text()) )

        self.downloadVideos()
        self.Obtener_info()
        self.progress = True
    
    def descargarVideo(self, timerActive=False):
        self.ui.lbl_info.setText('Descargando Video...')

        self.download_video( url=self.ui.txte_link.text() )
        self.ui.lbl_info.setText(self.name)
        
        self.notificacion('Informacion', f'Video Listo: {self.name}', self.NameApp)

        if timerActive: 
            self.progress = True
            self.ui.fr_progressBar2.setGeometry(self.porcent, 10, 30, 30)

    def _get_playlist(self, playlist):
        urls = []

        playlist_urls = Playlist(playlist)

        for url in playlist_urls:
            urls.append(url)

        return urls 

    def get_Url(self, playlist='', archivo='plurls.txt'):
        pl_ursls = self._get_playlist(playlist)

        with open(archivo, 'w') as f:
            for url in pl_ursls:
                f.write(f'{url}\n')
                self.numVideo += 1

        return f"\n [+] Urls saved {os.getcwd()}/{archivo}"

    def download_video(self, url='', cont=False, rutaGuardar='./videos'):        
        self.video = YouTube(url)  
        self.descarga = self.video.streams.get_highest_resolution()
        self.name = self.descarga.title
        
        filename = ''
        if cont != False: filename = f'{cont}. '
        filename += self.descarga.default_filename

        self.descarga.download( output_path=rutaGuardar, filename=filename )

    def downloadVideos(self, archivo='plurls.txt'):
        with open(archivo, 'r') as f: self.lines = f.readlines()
        self.num_leng = len(self.lines)
        self.iterador = 0

        for num, ruta in enumerate(self.lines):
            try:
                self.download_video(ruta, num+1)
                print(f'\n >>> {num+1}. {ruta}')
                self.iterador += 1

            except:
                if self.num == 0: 
                    self.num = self.iterador+1
                    self.error = ''

    def Obtener_info(self, archivo='info.txt'):
        info = f'\n[+] Total de Videos: {self.num_leng} \n'
        info += f'[+] Videos Descargados: {self.iterador} \n'
        info += f'[-] Videos Faltantes: {self.num_leng-self.iterador} \n'
        
        if self.num_leng-self.iterador == 0:
            info += f'\n[-] Error: al descargar archivo #{self.num} \n'
            info += f'Message:\n\t{self.error} \n'

        with open(archivo, 'w') as f: f.write(info)
    
    def notificacion(self, title='Titulo', message='Hola Mundo!', application_name='App1'):
        if self.notify:
            notification = Notify()
            notification.title = title
            notification.message = message
            notification.application_name = application_name
            notification.send()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) 
    window = MainApp() 
    window.show() 
    sys.exit(app.exec_())

#* De: Francisco Velez
