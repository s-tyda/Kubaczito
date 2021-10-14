import sys


def cezar(string):
    return "".join([x if x == ' ' else (chr((ord(x) + 2 - 65) % 26 + 65) if x.isupper() else chr((ord(x) + 2 - 97) % 26 + 97))for x in list(string)])


file = open(sys.argv[1]).read().strip()
print(file)

path = sys.argv[2]
with open(path, 'w') as f:
    f.write(cezar(file))