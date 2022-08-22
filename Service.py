# основная сущность- сервис
class Service:

    def __init__(self, service, condition):
        self.serviceName = service
        self.serviceCondition = condition

    def getServiceName(self):
        return self.serviceName

    def getServiceCondition(self):
        return self.serviceCondition
