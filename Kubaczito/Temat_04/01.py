def get_dict_from_string(string):
    return dict((x.strip(), y.strip()) for x,y in (i.split(":") for i in string.strip().split("\n")))


test = '''x: 1
y: 2
z: 3
'''

print(get_dict_from_string(test))
