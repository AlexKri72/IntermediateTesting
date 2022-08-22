import random
import Service
import ExportData
# генератор состояния севисов
condition = ["is worked         ", "no worked         ", "non stable worked "]
quantityOfServices = 5

serviceName = ["Server "+str(i) for i in range(1, quantityOfServices+1)]


def FillData():
    service = [Service.Service(
        serviceName[i], random.choice(condition))for i in range(quantityOfServices)]
    for item in service:
        ExportData.ExportData(item)
    return service
