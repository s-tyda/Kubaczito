import sys


def diff(list1, list2):
    return "\n".join(list(set(list1) - set(list2)) + list(set(list2) - set(list1)))


with open(sys.argv[1]) as f1:
    f1_text = f1.read().strip().split("\n")

with open(sys.argv[2]) as f2:
    f2_text = f2.read().strip().split("\n")

with open(sys.argv[3], 'w') as f3:
    f3.write(diff(f1_text, f2_text))
