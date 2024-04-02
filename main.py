import tkinter as Tk 
from tkinter import *
from tkinter import font
import pyautogui
import os
import time

root = Tk()
root.geometry("400x400")
root.title("App Desempenho")
root.maxsize(400, 400)
root.minsize(400, 400)
root.configure(background="black")
root.iconbitmap("desempenho.ico")
fonte = ("Hack", 18, "italic")

mensagem = "Se deseja limpar seu pc de arquivos inuteis \n e melhorar o desempenho, Clique no botão abaixo!"
aviso = "Aviso:\n Quando clicar no botão,\n por favor não mexa no computador,\n até procedimento acabar!"
credito = "by thurflecks \n version 1.0"


with open('temp.bat', 'r') as arquivo:
    conteudo = arquivo.read()
    
with open('servicos.bat', 'r') as arquivo:
    servicos = arquivo.read()

cmd = "cmd"
 
def ola():
    nome_usuario = os.getlogin()
    bemVindo.configure(text= f"Olá, {nome_usuario} seja Bem Vindo!")
    
def limpeza():
    pyautogui.PAUSE = 2
    time.sleep(2)
    pyautogui.hotkey("win", "r")
    pyautogui.write(cmd)
    pyautogui.press("enter")
    pyautogui.write(conteudo)
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.press("enter")
    pyautogui.hotkey("alt", "f4")
    
def desativar():
    pyautogui.PAUSE = 2
    time.sleep(2)
    pyautogui.hotkey("win", "r")
    pyautogui.write(cmd)
    pyautogui.press("enter")
    pyautogui.write(servicos)
    pyautogui.press("enter")
    time.sleep(6)
    pyautogui.press("enter")
    pyautogui.hotkey("alt", "f4")
      



bemVindo = Label(font = (fonte), bg = '#000', fg = 'white')
bemVindo.place(x=45, y=20)

mensagem = Label(text= (mensagem), bg = '#000', fg = 'white', font= "Hack 11 italic")
mensagem.place(x=30, y=80)

botao = Button(text = "Desempenho Máximo", bg = '#000', fg = 'white', width= 25, height=3, command=limpeza)
botao.place(x=10, y=145)

botao1 = Button(text = "Desativar Serviços", bg = '#000', fg = 'white', width= 25, height=3, command=desativar)
botao1.place(x=210, y=145)

aviso = Label(text= (aviso), bg = '#000', fg = 'red', font= "Hack 10")
aviso.place(x=95, y=230)

credito = Label(text= (credito), bg = '#000', fg = 'red', font= "Hack 8")
credito.place(x=165, y=350)

ola()
root.mainloop()


