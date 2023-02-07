import os
from tkinter import *
import tkinter as tk
from tkcalendar import Calendar
import CreateNote


os.system("cls")


def DeleteNote():
    selection = NoteBox.curselection()
    NoteBox.delete(selection[0])
    listNote.pop(selection[0])

    with open("note.csv", "w") as file:
        file.writelines(listNote)


def Bat():
    global window
    window = tk.Tk()
    window.title("Заметки")

    # add calendar and button "Select day"
    cal = Calendar(window, selectmode='day', year=2023, month=2, day=1)
    cal.grid(row=0, column=0, padx=20, pady=20, sticky=NW, rowspan=2)

    def grad_date():
        date.config(text="Выбрана дата: " + cal.get_date())

    Button(window, text="Выбрать дату", command=grad_date).grid(
        row=2, column=0, padx=20, pady=5, sticky=N)
    date = Label(window, text="")
    date.grid(row=3, column=0, padx=20, pady=20, sticky=N)

    # add button
    Button(text="Создать заметку", width=25, height=3, command=CreateNote.CreateNote).grid(row=0, column=1, padx=20, pady=20,
                                                                                           sticky=N)
    Button(text="Изменить заметку", width=25,
           height=3).grid(row=0, column=2, padx=20, pady=20, sticky=N)
    Button(text="Удалить заметку", width=25,
           height=3, command=DeleteNote).grid(row=0, column=3, padx=20, pady=20, sticky=N)

    for i in range(3):
        window.columnconfigure(i, weight=1, minsize=75)
        window.rowconfigure(i, weight=1, minsize=50)

    with open("note.csv", "r") as file:
        global listNote
        listNote = file.readlines()
    global NoteBox
    NoteBox = Listbox(listvariable=Variable(value=listNote))
    NoteBox.grid(row=1, column=1, sticky="nsew", columnspan=3, padx=10)

    window.mainloop()
