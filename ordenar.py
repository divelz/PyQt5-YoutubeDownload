import os

def func2():
    nameArch = os.listdir()
    n = ''

    for ruta_video in nameArch:
        try:
            part3 = ruta_video.split('-')
            part1_2 = part3[0].split('.')

            if part3[1][0] != ' ': n = part3[1][0]
            else: n = ''
            
            newName = f'{part1_2[0]}{n}. Pr{part1_2[1].strip()} -{part3[1].replace(n, "", 1)}'

            os.rename( ruta_video, newName)

        except: pass

func2()