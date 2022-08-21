import sqlite3
from unittest import result
import GeneratorOfCondition


def ImportData():
    base = sqlite3.connect("dataBase.db")
    cur = base.cursor()
    result = ""
    for i in GeneratorOfCondition.serviceName:
        noWorkedTime = cur.execute(
            "SELECT nameService,Condition FROM My_table WHERE nameService=? AND Condition=?;", (i, GeneratorOfCondition.condition[1])).fetchall()
        allTime = cur.execute(
            "SELECT nameService,Condition FROM My_table WHERE nameService=?;", (i,)).fetchall()
        #print(i+" "+str("%.3f" % ((1 - len(noWorkedTime)/len(allTime))*100))+"%")
        result += i + " " + \
            str("%.3f" % ((1 - len(noWorkedTime)/len(allTime))*100))+"%\n"
    return result
