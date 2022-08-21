import sqlite3
import threading
import GeneratorOfCondition
from Service import Service
from ServiceCondition import ServiceCondition
from time import sleep
from tkinter import *
import ImportData
import GetServiceHistory
import os

os.system("cls")

stopFlag = True


def Bat():
    global window
    window = Tk()
    window.title("Опрос состояния сервисов")
    window.geometry('450x550+700+300')

    # Кнопки
    emptyLbl = Label(window, text=" "*70+"\n"+" "*70+"\n"+" "*70 +
                     "\n"+" "*70+"\n"+" "*70, font=16)
    emptyLbl.grid(column=0, row=1)
    btnStart = Button(window, text="Start", background="lavender", foreground="#B22222",
                      width=15, height=2, font=18, command=lambda: threading.Thread(target=Run, daemon=True).start())
    btnStart.grid(column=1, row=0)
    btnStop = Button(window, text="Stop", background="lavender", foreground="#B22222",
                     width=15, height=2, font=18, command=Stop)
    btnStop.grid(column=1, row=1)
    btnCheckSLA = Button(window, text="Check SLA", background="lavender", foreground="#B22222",
                         width=15, height=2, font=18, command=lambda: threading.Thread(target=CheckSLA, daemon=True).start())
    btnCheckSLA.grid(column=1, row=2)
    btnCheckSLA = Button(window, text="Throw off log SLA", background="lavender", foreground="#B22222",
                         width=15, height=2, font=18, command=lambda: threading.Thread(target=ThrowLog, daemon=True).start())
    btnCheckSLA.grid(column=1, row=3)

    global choiceService
    choiceService = IntVar()
    choiceService.set(1)

    for i in GeneratorOfCondition.serviceName:
        rb = Radiobutton(text=i, value=int(
            i[-1]), variable=choiceService, padx=15, pady=10, font=18)
        rb.grid(row=2+int(i[-1]), column=0, sticky=W)

    btnHistory = Button(window, text="Save log to file ", background="lavender", foreground="#B22222",
                        width=15, height=2, font=18, command=lambda: threading.Thread(target=HistoryView, daemon=True).start())
    btnHistory.grid(column=1, row=5)

    window.mainloop()


def HistoryView():
    return GetServiceHistory.GetServiceHistory("Server "+str(choiceService.get()))


def ThrowLog():
    base = sqlite3.connect("dataBase.db")
    base.execute("DELETE FROM  My_table;")
    base.commit()


def CheckSLA():
    lbl = Label(window, text=ImportData.ImportData(), font=16, justify=LEFT)
    lbl.grid(column=0, row=1)


def Run():
    global stopFlag
    stopFlag = True
    Start()


def Start():
    while stopFlag:
        lbl = Label(window, text=ServiceCondition(
            GeneratorOfCondition.FillData()), font=16, justify=LEFT)
        lbl.grid(column=0, row=0)
        sleep(2)


def Stop():
    global stopFlag
    stopFlag = False
