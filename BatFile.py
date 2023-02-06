import os
from tkinter import *
import tkinter as tk
from tkcalendar import Calendar
import CreateNote

os.system("cls")


def Bat():
    global window
    window = tk.Tk()
    window.title("Заметки")

    # add calendar and button "Select day"
    cal = Calendar(window, selectmode='day', year=2023, month=2, day=1)
    cal.grid(row=0, column=0, padx=20, pady=20, sticky=NW)

    def grad_date():
        date.config(text="Выбрана дата: " + cal.get_date())

    Button(window, text="Выбрать дату", command=grad_date).grid(
        row=1, column=0, padx=20, pady=5, sticky=N)
    date = Label(window, text="")
    date.grid(row=2, column=0, padx=20, pady=20, sticky=N)

    # add button
    Button(text="Создать заметку", width=25, height=3, command=CreateNote.CreateNote).grid(row=0, column=1, padx=20, pady=20,
                                                                                           sticky=N)
    Button(text="Изменить заметку", width=25,
           height=3).grid(row=0, column=2, padx=20, pady=20, sticky=N)
    Button(text="Удалить заметку", width=25,
           height=3).grid(row=0, column=3, padx=20, pady=20, sticky=N)

    for i in range(3):
        window.columnconfigure(i, weight=1, minsize=75)
        window.rowconfigure(i, weight=1, minsize=50)

    window.mainloop()


# функции, реагирующие на нажатие кнопок
