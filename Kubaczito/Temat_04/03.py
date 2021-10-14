import collections
import sys

test = open(sys.argv[1]).read()

print(dict(collections.Counter(test.strip().split())))
