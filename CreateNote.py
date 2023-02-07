import datetime
import tkinter as tk


def CreateNote():

    # Создается новое окно с заголовком
    global window1
    window1 = tk.Toplevel()
    window1.title("Новая заметка")

    # Создает ярлык и текстовое поле для ввода названия темы.
    lblNoteTheme = tk.Label(window1, text="Тема заметки:")
    global entNoteTheme
    global entNoteText
    entNoteTheme = tk.Entry(window1, width=100)
    lblNoteTheme.grid(row=0, column=0, sticky="w", padx=10, pady=20)
    entNoteTheme.grid(row=0, column=1, sticky="w", padx=10, pady=20)

    # Создает ярлык и текстовое поле для ввода текста заметки.
    lblNoteText = tk.Label(window1, text="Текст :")
    entNoteText = tk.Text(window1, width=80, height=10)
    lblNoteText.grid(row=1, column=0, sticky="w", padx=10, pady=20)
    entNoteText.grid(row=1, column=1, sticky="w", padx=10, pady=20)

    # Создает кнопку "Сохранить"
    tk.Button(window1, text="Сохранить", width=40, height=2, command=SaveToFile).grid(
        row=2, column=1, padx=10, pady=20)
    for i in range(3):
        window1.columnconfigure(i, weight=1, minsize=120)
        window1.rowconfigure(i, weight=1, minsize=100)


def SaveToFile():
    with open("note.csv", "r+") as file:
        array = file.readlines()
        file.write(str(len(array)+1)+" ")
        file.write(str(datetime.datetime.now())[:-7]+" ")
        file.write(str(entNoteTheme.get())+" ")
        file.write(str(entNoteText.get("1.0", tk.END)))
    window1.destroy()
