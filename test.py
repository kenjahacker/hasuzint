import socket
import webbrowser
import os 
import pyautogui as pg

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostbyname_ex(socket.gethostname())[-1][-1], 1234))

server.listen()

while True:
    user, adres = server.accept()

    while True:
        data = user.recv(1024).decode("utf-8").lower()
        print(data)

        if data == "youtube":
            webbrowser.open("https:www.youtube.com")
        elif data == "google":
            webbrowser.open("https:www.google.com")
        elif data == "yandex":
            webbrowser.open("https://yandex.uz/")
        elif data == "vk":
            webbrowser.open("https:www.vk.com")

        elif data == "foto":
            os.startfile("C:/Users/Hasan/Downloads/40618026-4e7a-4b44-a048-4e11500803d9.jpg")
        elif data == "music":
            os.startfile("D:/Hasan/Hasuzint/Life.mp3")

        elif data == "chrome":
            os.system("start chrome")
        elif data == "saytni yop":

        elif data == "programani kata qil":
            pg.getInfo()


        else:
            print("Kechirasiz xujayin. Xozircha funksiyalarim kam kelajakta siz bl\n birga mani funksiyalarimni kupaytiramiz!")
        