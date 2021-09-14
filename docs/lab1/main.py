import numpy as np
import pandas as pd

a = np.arange(1, 16, 2)
print(a)

a = np.ones(9, dtype='float')
print(a)

a = np.zeros((2, 4), dtype='uint')
print(a)

a = np.linspace(0, 1, 5)
print(a)

a = np.random.random((4, 3))
print(a)

a = np.random.randint(0, 100, (3, 4))
print(a)

a = np.empty(5)
print(a)

print(a.shape)

print(a[1], a[-2])
# print(a[0, -1])
# print(a[0: 1])

a = np.ones(4)
a *= 3
print(a)

a = np.arange(0, 6)
print(np.add.reduce(a))
print(np.add.accumulate(a))

a = np.arange(1, 10)
print(np.multiply.outer(a, a))

data = pd.read_csv('../../data/iris.csv')
petal = np.array(data['petal_length'])
print(petal)
