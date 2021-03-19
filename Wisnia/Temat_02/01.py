import sys

if len(sys.argv) != 2 or not sys.argv[1].isdecimal():
    print("Wypierdalaj")
else:
    print(not bool(int(sys.argv[1]) % 2))
