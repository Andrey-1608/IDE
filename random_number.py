"""программа угадай число"""
import numpy as np

num_random = np.random.randint(1, 101)
chislo = 101
print(num_random)
while chislo != num_random:
    chislo = input()
    chislo = int(chislo)
    if chislo != num_random:
        print('Не угодал\n')
print('МОЛОДЕЦ')
