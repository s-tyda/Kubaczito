import sys


def get_dict_from_string(string):
    return dict((x.strip(), y.strip()) for x,y in (i.split(":") for i in string.strip().split("\n")))


test = open(sys.argv[1]).read()

print(get_dict_from_string(test))
