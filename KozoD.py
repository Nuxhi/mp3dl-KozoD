from pytube import YouTube
import os

def main():
    destination = "/home/balasundar/Downloads/"
    os.system("cls")
    print("\n\n")
    print("               ╔══════════════════════════════╗")
    print("               ║                              ║")
    print("               ║     1. Download Clip         ║")
    print("               ║                              ║")
    print("               ║     2. Download Audio        ║")
    print("               ║                              ║")
    print("               ║     3. play musique          ║")
    print("               ║                              ║")
    print("               ╚══════════════════════════════╝\n")

    choix = input("votre choix : ")

    if choix == '1':
        clip_dl()

    if choix == '2':
        audio_dl()




def clip_dl():
    lien = input('Lien : ')
    try:
        video = YouTube(lien)
        print('[ CLEAN ]  [ 1/3 ]\n')
        os.system("cls")

        print('Get information / [ 2/3 ] \n')
        print(' | chaine :', video.author, ' |')
        print(' | vue :', video.views, ' |')
        print(' | titre :', video.title, ' |')

        streams = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
        print(' [ CLEAN ]  [ 2/3 ]\n\n')

        print('Download in progress / [ 3/3 ]')
        streams[0].download()
        print('Download Completed!')
        main()

    except:
        print("Connection Error")
        main()






def audio_dl():
    lien = input('Lien : ')
    try:
        video = YouTube(lien)
        print('[ CLEAN ]  [ 1/3 ]\n')
        os.system("cls")

        print('Get information / [ 2/3 ] \n')
        print(' | chaine :', video.author, ' |')
        print(' | vue :', video.views, ' |')
        print(' | titre :', video.title, ' |')

        audio = video.streams.filter(only_audio=True, file_extension='mp4').first()
        print(' [ CLEAN ]  [ 2/3 ]\n\n')

        print('Download in progress / [ 3/3 ]')
        audio.download()
        print('Download Completed!')
        main()

    except:
        print("Connection Error")
        main()
    



if __name__ == "__main__":
    main()