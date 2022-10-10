# url+url+url

#* Version cmd
import os, time
# from colorama import Fore

# https://www.youtube.com/watch?v=7O-YUh29XIE&ab_channel=Nauu08 descarga gratis

# curso piano
# https://www.youtube.com/watch?v=kAALQ4JEY6c&list=PL92TYERZtnkSqZpcT8xlygi_FfpnecThS

# git
# https://www.youtube.com/watch?v=4OXXLtbM8IE&list=PLDbrnXa6SAzUyitkL4zcnWO07HxG0BvmS

try:
    from pytube import Playlist, YouTube
    from art import * 

except ModuleNotFoundError:
    os.system('pip install pytube')
    os.system('pip install art')

class DownloadYoutubeVideoList:

    def __init__(self, run=False, leerArchivo=False, nombreArchivo='text.txt'):
        if leerArchivo: self.leerArchivo = [leerArchivo, nombreArchivo]
        else: self.leerArchivo = [leerArchivo]
        self.error = 0
        self.num = 0
        self.video = None  
        self.descarga = None
            
            
        if run:
            self.get_Url()
            self.download_video()
            self.print_info()

    def get_Url(self):
        tprint('YTDownload')
        print('Developed by Francisco J. Velez O.')
        print('----------------------------------')

        # Create a function to get urls form list of playlist
        def get_playlist(playlists):
            urls = []

            for playlist in playlists:
                playlist_urls = Playlist(playlist)

                for url in playlist_urls:
                    urls.append(url)

            return urls 

        # Code drive
        if self.leerArchivo[0]: infor = self.func_leer_arch()
        else: infor = input(' >>> Digite la url: ')

        if infor.strip() == '': return

        playlist = infor.split('+')
        pl_ursls = get_playlist(playlist)

        with open('plurls.txt', 'w') as f:
            for url in pl_ursls:
                f.write(f'{url}\n')

        print(f"\n [+] Urls successfully saved into {os.getcwd()}/plurls.txt")
    
    def func_leer_arch(self):
        return_ = ''
        print(self.leerArchivo)

        with open(self.leerArchivo[1], 'r') as f:
            list_info = f.readlines()

            for txt in list_info:
                txt2 = txt.strip()

                if list_info[-1] != txt and txt2 != '': return_ += f'{txt2}|'
                else: return_ += txt2

        print(return_.replace('\n', '').replace('||', '|'))
        return return_

    def download_video(self):
        with open('plurls.txt', 'r') as f: self.lines = f.readlines()
        self.num_leng = len(self.lines)
        self.iterador = 0

        for num, ruta in enumerate(self.lines):
            try:
                self.video = YouTube(ruta)  
                self.descarga = self.video.streams.get_highest_resolution()
                
                self.descarga.download(
                    './video1',filename=f'{num+1}. {self.descarga.default_filename}'
                )
                
                print(f'\n >>> {num+1}. {ruta}')
                self.iterador += 1
                time.sleep(0.02)

            except:
                if self.num == 0: 
                    self.num = self.iterador+1
                    self.error = ''

    def print_info(self):
        print('\n [+] Completed... ')

        print(f'\n[+] Total de Videos: {self.num_leng}')
        print(f'[+] Videos Descargados: {self.iterador}')
        print(f'[-] Videos Faltantes: {self.num_leng-self.iterador} \n')
        
        if self.num_leng-self.iterador == 0:
            print(f'\n[-] Error: al descargar archivo #{self.num}')
            print(f'Message:\n\t{self.error}')


___Run__ = DownloadYoutubeVideoList(
    leerArchivo=False, nombreArchivo='./UrlList.txt',
    run=True
)

# De: Francisco Velez
