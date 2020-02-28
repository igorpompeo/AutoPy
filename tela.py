# Desenvolvimento de telas em Python

# coding: UTF8

from tkinter import *
from tkinter import ttk
import calendar

# Criação da janela
main = Tk()

# Colcando um titulo
main.title('Aprendendo Criação de Tela com TKinter!')
# Trocando o icone da tela
main.iconbitmap(
    'C:/Users/IgorPompeoTavares/Desktop/Igor/AutoPy/starwars_darth_vader_icon_131815.ico'
    )

lbl = Label(
    main, text='Informe uma data para iniciar a busca: \n - modelo(YYYY/MM/DD)'
    ).pack()
# Criação de segunda tela
# top = Toplevel()


# Alteração do background da janela 
# main['bg'] = 'green'

# Impressão na janela de qualquer texto
# lbl = Label (main, text='Fala galera!')

# Quando usar o place como gerenciador de layout não pode usar o pack junto
# lbl.place(x=100, y=100)

# Criação de Botão
# bt1 = Button(main, width=20, text='Botão 1')
# bt1.place(x=100, y=100)
# bt2 = Button(main, width=20, text='Botão 2')
# bt2.place(x=100, y=130)

# Definição do tamanho da janela LxA+E+T

main.mainloop()
