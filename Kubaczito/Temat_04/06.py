import sys
import textwrap


def center_wrap(text, cwidth, **kw):
    lines = textwrap.wrap(text, **kw)
    return "\n".join(line.center(cwidth) for line in lines)


with open(sys.argv[1]) as f:
    file = f.read()

width = int(sys.argv[2])

print(center_wrap(file, cwidth=width + 30, width=width))
