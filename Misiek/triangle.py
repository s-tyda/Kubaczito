import random
import numpy as np
import matplotlib.pyplot as plt


# def zrobciag(n):
#     return ''.join(['*' if random.randint(0, 1) else '' for x in range(n)])


rule = '01011010'
l1 = ['***',  '**_', '*_*', '*__', '_**',  '_*_',  '__*',  '___']
reguly = dict(zip(l1, ['*' if int(i) else '_' for i in list(rule)]))
# ciag = zrobciag(100)
ciag = '________________________________________________________________________________________________________________________________________*________________________________________________________________________________________________________________________________________'
print(ciag)
print(reguly)
for i in range(400):
    result = ''
    for j in range(len(ciag)):
        substring = ciag[j:j+3]
        if len(substring) < 3:
            substring += ciag[0:3-len(substring)]
        result += reguly[substring]
    ciag = result[-1] + result[:-1]
    print(ciag)
