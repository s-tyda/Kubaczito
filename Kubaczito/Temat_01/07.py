print("".join([x if x == ' ' else (chr((ord(x) + 2 - 65) % 26 + 65) if x.isupper() else chr((ord(x) + 2 - 97) % 26 + 97))for x in list(input("Podaj słowo do zaszyfrowania.\n"))]))
