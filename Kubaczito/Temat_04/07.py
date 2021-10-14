import sys
import re

regex = r"(?<![^\s])(?:(?:[1-9]\d?|1\d{2}|2[0-4]\d|25[0-5])\.){3}(?:[1-9]\d?|1\d{2}|2[0-4]\d|25[0-5])(?![^\s])"

with open(sys.argv[1]) as f:
    file = f.read()

print(re.findall(regex, file))
