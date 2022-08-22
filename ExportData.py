import sqlite3
from datetime import datetime
from Service import *

# запись данных в базу


def ExportData(service):
    nameService = service.getServiceName()
    condition = Service.getServiceCondition(service)
    checkTime = datetime.now()

    base = sqlite3.connect("dataBase.db")
    cur = base.cursor()

    base.execute(
        'CREATE TABLE IF NOT EXISTS My_table (dateTime timestamp,nameService TEXT,Condition TEXT); ')
    base.commit()
    cur.execute(
        "INSERT INTO My_table  VALUES(?,?,?);", (checkTime, nameService, condition))
    base.commit()
