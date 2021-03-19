import datetime

print((lambda *data, **kw:
       {x: datetime.datetime(x[0], x[1], x[2]).strftime("%A") for x in list(data) + list(kw.values())})
      ((2021, 3, 12), (2021, 3, 13), (2021, 3, 14), data=(2021, 3, 15)))

