import os

generator = (lambda x: (file for file in os.listdir(input("Podaj ścieżkę katalogu\n")) if file.endswith(x)))(input("Podaj rozszerzenie np \".py\"\n"))
print([i for i in generator])
