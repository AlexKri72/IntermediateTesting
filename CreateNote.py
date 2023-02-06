import tkinter as tk


def CreateNote():

    # Создается новое окно с заголовком
    window1 = tk.Toplevel()
    window1.title("Новая заметка")

    # Создает ярлык и текстовое поле для ввода названия темы.
    lblNoteTeme = tk.Label(window1, text="Тема заметки:")
    ent_NoteTeme = tk.Entry(window1, width=100)
    lblNoteTeme.grid(row=0, column=0, sticky="w", padx=10, pady=20)
    ent_NoteTeme.grid(row=0, column=1, sticky="w", padx=10, pady=20)

    # Создает ярлык и текстовое поле для ввода текста заметки.
    lblNoteText = tk.Label(window1, text="Текст :")
    entNoteText = tk.Text(window1, width=80, height=10)
    lblNoteText.grid(row=1, column=0, sticky="w", padx=10, pady=20)
    entNoteText.grid(row=1, column=1, sticky="w", padx=10, pady=20)

    # Создает кнопку "Сохранить"
    tk.Button(window1, text="Сохранить", width=40, height=2).grid(
        row=2, column=1, padx=10, pady=20)
