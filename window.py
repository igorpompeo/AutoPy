# Seeing course from CODEMY.com
# coding UTF8

import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

def btnAction():
    root.destroy()

def calendar():
    def print_sel():
        print(cal.selection_get())

    top = tk.Toplevel(root)

    cal = Calendar(top,
        font='Arial 14',
        selectmode='day',
        cursor='hand1',
        year=2019,
        month=2,
        day=5
        )
    cal.pack(fill='both',expand=True)
    ttk.Button(top,text='ok',command=print_sel).pack()

def calendar2():
    top = tk.Toplevel(root)

    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)

    cal = DateEntry(top, width=12, bg='darkblue', fg='white', bw=2)

    cal.pack(padx=10, pady=10)

root = tk.Tk()
s = ttk.Style(root)
root.title(
    'Initialize Know How to Use TKinter'
    )
root.iconbitmap(
    'C:/Users/IgorPompeoTavares/Desktop/Igor/AutoPy/starwars_darth_vader_icon_131815.ico'
)
s.theme_use('clam')
# lbl = Label(
#     root, 
#     text='Hello World'
#     ).grid(
#         row=0, column=0
#         )
# btn = Button(
#     root, 
#     width=10, 
#     text='Close',
#     fg='blue', 
#     command=btnAction
#     ).grid(row=0, column=1)


ttk.Button(root, text='Calendar', command=calendar).pack(padx=10, pady=10)
ttk.Button(root, text='DateEntry', command=calendar2).pack(padx=10, pady=10)

root.mainloop()
