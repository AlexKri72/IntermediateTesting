import os
from tkinter import *
import tkinter as tk
from tkcalendar import Calendar
import CreateNote

os.system("cls")


def NewNote():
    CreateNote.Note("", "", -1)


def ReadFromFile(selectDate="NULL"):
    global listNote
    global NoteBox
    with open("note.csv", "r") as file:
        listNote = file.readlines()
    if selectDate != "NULL":
        listNote1 = []
        for i in range(len(listNote)):
            if listNote[i].split()[1] == selectDate:
                listNote1.append(listNote[i])
        NoteBox = Listbox(listvariable=Variable(value=listNote1))
        NoteBox.grid(row=1, column=1, sticky="nsew", columnspan=3, padx=10)
    else:
        NoteBox = Listbox(listvariable=Variable(value=listNote))
        NoteBox.grid(row=1, column=1, sticky="nsew", columnspan=3, padx=10)


def ChangeNote():
    selection = NoteBox.curselection()  # читаем позицию курсора на выбранной заметке
    with open("note.csv", "r") as file:
        listNote = file.readlines()
    if not selection:  # если заметка не выбрана курсором, выдаем предупреждение
        temp = -2
        CreateNote.Note("", "", temp)
    else:               # если заметка выбрана, вызываем функцию изменения
        temp = listNote[selection[0]].split()
        CreateNote.Note(
            " ".join(temp[temp.index("Theme:")+1:temp.index("Note:")]), " ".join(temp[temp.index("Note:")+1:]), int(temp[0]))


def DeleteNote():
    selection = NoteBox.curselection()
    # удаляем на экране
    NoteBox.delete(selection[0])
    # удаляем в файле
    listNote.pop(selection[0])
    # записываем новый вариант файла
    with open("note.csv", "w") as file:
        file.writelines(listNote)


def Bat():
    global window
    window = tk.Tk()
    window.title("Заметки")

    # добавляем календарь и кнопку выбора даты
    cal = Calendar(window, selectmode='day', year=2023, month=2, day=1)
    cal.grid(row=0, column=0, padx=20,
             pady=20, sticky=NW, rowspan=2)

    def grad_date():
        date.config(text="Выбрана дата: " + cal.get_date())
        dateSelect = cal.get_date().split(".")
        resultDate = dateSelect[2]+"-"+dateSelect[1]+"-"+dateSelect[0]
        ReadFromFile(resultDate)

    def deleteDate():
        ReadFromFile("NULL")

    Button(window, text="Выбрать дату", command=grad_date).grid(
        row=2, column=0, padx=20, pady=5, sticky=N)
    date = Label(window, text="")
    date.grid(row=4, column=0, padx=20, pady=20, sticky=N)

    Button(window, text="Сбросить дату", command=deleteDate).grid(
        row=3, column=0, padx=20, pady=5, sticky=N)

    # добавляем кнопки
    Button(text="Создать заметку", width=25, height=3, command=NewNote).grid(row=0, column=1, padx=20, pady=20,
                                                                             sticky=N)
    Button(text="Изменить заметку", width=25,
           height=3, command=ChangeNote).grid(row=0, column=2, padx=20, pady=20, sticky=N)
    Button(text="Удалить заметку", width=25,
           height=3, command=DeleteNote).grid(row=0, column=3, padx=20, pady=20, sticky=N)
    Button(text="Обновить список", width=75,
           height=3, command=ReadFromFile).grid(row=2, column=1, padx=5, pady=5, sticky=N, columnspan=3)

    for i in range(3):
        window.columnconfigure(i, weight=1, minsize=75)
        window.rowconfigure(i, weight=1, minsize=50)
    ReadFromFile()

    window.mainloop()
