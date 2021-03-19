import os


def gen(directory):
    for file in os.listdir(directory):
        if file.endswith('.py'):
            yield file


print(list(gen("../..")))
