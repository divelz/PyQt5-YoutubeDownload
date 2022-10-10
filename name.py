from pytube import YouTube
import time

def download_video():

    with open('plurls.txt', 'r') as f:
        lineas = f.readlines()
        num_leng = len(lineas)
        iterador = 0

    for num, ruta in enumerate(lineas):
        try:
            video = YouTube(ruta)  
            descarga = video.streams.get_highest_resolution()
            
            descarga.download(output_path='./video1', filename=f'{12+num+1}. {descarga.default_filename}')

            print(f'\n >>> {12+num+1}. {ruta}')
            iterador += 1
            time.sleep(0.02)

        except: pass

download_video()
