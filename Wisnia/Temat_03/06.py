import datetime


def fun(data):
    return datetime.datetime(data[0], data[1], data[2]).strftime("%A")


print(fun((2021, 3, 12)))
