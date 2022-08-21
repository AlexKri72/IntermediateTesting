import sqlite3
import GeneratorOfCondition


def GetServiceHistory(name):
    base = sqlite3.connect("dataBase.db")
    cur = base.cursor()
    noWorkedTime = cur.execute(
        "SELECT dateTime,Condition FROM My_table WHERE nameService=? AND Condition=?;", (name, GeneratorOfCondition.condition[1])).fetchall()
    isWorkedTime = cur.execute(
        "SELECT dateTime,Condition FROM My_table WHERE nameService=? AND Condition=?;", (name, GeneratorOfCondition.condition[0])).fetchall()
    nonStableWorkedTime = cur.execute(
        "SELECT dateTime,Condition FROM My_table WHERE nameService=? AND Condition=?;", (name, GeneratorOfCondition.condition[2])).fetchall()
    allTime = cur.execute(
        "SELECT dateTime,Condition FROM My_table WHERE nameService=?;", (name,)).fetchall()
    with open("log.csv", "w") as file:
        file.writelines(name+"\n")
        file.writelines("Total tracking time: \t" +
                        str(len(allTime)*2) + " seconds, of which:\n")
        file.writelines("Didn't work: \t\t\t" + str(len(noWorkedTime)*2) + " second, " +
                        str("%.3f" % (len(noWorkedTime)/len(allTime) * 100)) +
                        "% of the total time\n")
        file.writelines("Worked unstable: \t\t" + str(len(nonStableWorkedTime)*2)+" second, " +
                        str("%.3f" % (len(nonStableWorkedTime)/len(allTime)*100)) +
                        "% of the total time\n")
        file.writelines("Worked properly: \t\t" + str(len(isWorkedTime)*2)+" second, " +
                        str("%.3f" % (len(isWorkedTime)/len(allTime)*100)) + "% of the total time\n")
        file.writelines("Details: \n")
        file.writelines("{\n")
        for i in allTime:
            file.writelines('\t"'+str(i[0])+'" : "'+str(i[1]).strip()+'",\n')
        file.writelines("}")
