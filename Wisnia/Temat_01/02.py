# print
print(lista := ["JP", 2, True])
# dodać 2 elementy na końcu
print(lista := lista + ["jeden", "dwa"])
# dodać element na pozycji 2
print(lista := lista[:1] + ["element"] + lista[1:])
# zduplikuj lista do lista2
print(lista2 := lista)
# dodać na koniec listy2 listę1
print(lista2 := lista2 + lista)
# print długość listy 2
print(len(lista2))
# ostatni element listy 2
print(lista2[-1])
# pozycja na której element ostatni pojawia się po raz pierwszy i usnięcie go
print(lista2.remove(lista2[-1]) or lista2)
# usuń ostatni element z listy
print(lista2 := lista2[:-1])
# lista 3 od 3 do 5 elementu włącznie z lista2
print(lista3 := lista2[3:6])
