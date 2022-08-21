import Service


def ServiceCondition(service):
    str = ""
    for i in service:
        str += Service.Service.getServiceName(i) + " : " + \
            Service.Service.getServiceCondition(i)+"\n"
    return str
