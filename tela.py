# Desenvolvimento de telas em Python

# coding: UTF8

from tkinter import *

# criação da janela
janela = Tk()

# alteração de titúlo
janela.title("Janela Principal")

# alteração do background da janela
janela["bg"] = "green"

# definição do tamanho da janela LxA+E+T
janela.geometry("300x300+100+100")

lbl = Label (janela, text="Fala galera!").pack()

janela.mainloop()
