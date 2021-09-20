import numpy as np
import pandas as pd

from string import Template

np.set_printoptions(suppress=True)

template = Template('#' * 10 + ' $string ' + '#' * 10)

# Generating section starts #

print(template.substitute(string='Generate array from 3 to 25 with step 2'))
array = np.arange(3, 25, 2)
print(array)

print(template.substitute(string='Generate array of 13 elements, filled with ones'))
array = np.ones(13, dtype='float')
print(array)

print(template.substitute(string='Generate matrix 3x7x3, filled with zeros'))
array = np.zeros((3, 7, 3), dtype='uint')
print(array)

print(template.substitute(string='Generate evenly spaced numbers from 3 to 8 over a specified interval'))
array = np.linspace(3, 8, 5)
print(array)

print(template.substitute(string='Generate random floats in the half-open interval [0.0, 1.0)'))
array = np.random.random((2, 2, 2))
print(array)

print(template.substitute(string='Generate random integers from low (inclusive) to high (exclusive).'))
array = np.random.randint(23.1, 50, (5, 5))
print(array)

print(template.substitute(string='Generate a new array of given shape and type, without initializing entries.'))
array = np.empty(10)
print(array)

# Generating section ends #
# Indexing section starts #

array = np.arange(12)
array.shape = (3, 4)

print(template.substitute(string='Generate the ndarray'))
print(array)

print(template.substitute(string='Indexing the last row'))
print(array[2])
print(array[-1])

print(template.substitute(string='Indexing the third row'))
print(array[:, 2])

print(template.substitute(string='Indexing the element'))
print(array[2, 2])
print(array[-1, -2])

print(template.substitute(string='Create the sub-array'))
print(array[0][0:3:2])

# Indexing section ends #
# Arithmetic operations section starts #

array = np.arange(1, 9, dtype='float')
array_1 = np.arange(1, 9, dtype='int')
print(template.substitute(string='Generate the ndarray'))
print(array)

print(template.substitute(string='Adding'))
print(array + 3.1)
print(np.add(array, array_1 + np.ones(8)))

print(template.substitute(string='Subtracting'))
print(array - 3)
print(np.subtract(array, array_1 + np.ones(8)))

print(template.substitute(string='Multiplying'))
print(array * 2.5)
print(np.multiply(array, array_1 + np.ones(8)))

print(template.substitute(string='Dividing'))
print(array / .5)
print(np.divide(array, array_1))

print(template.substitute(string='Powering'))
print(array ** 2)
print(np.power(array, np.ones(8)))
print(np.power(np.array([10, 100, 1000]), np.array([3, 2, 1])))

print(template.substitute(string='Remainder of division'))
print(array % 2)
print(np.mod(array, array_1))

print(template.substitute(string='Convert to negative values'))
print(-array)
print(np.negative(array - 3))

print(template.substitute(string='Complex operations'))
print(((4 * array + 2) ** 1.5))

print(template.substitute(string='Reduce'))
print(np.add.reduce(array))
print(np.subtract.reduce(array))
print(np.multiply.reduce(array))
print(np.divide.reduce(array))
print(np.power.reduce(array))

print(template.substitute(string='Accumulate'))
print(np.add.accumulate(array))
print(np.subtract.accumulate(array))
print(np.multiply.accumulate(array))
print(np.divide.accumulate(array))
print(np.power.accumulate(array))

print(template.substitute(string='Outer'))
array = np.arange(1, 10)
print(np.multiply.outer(array, array))

# Arithmetic operations section ends #
# Operations with data section starts #

data = pd.read_csv('../../data/iris.csv')
petal = np.array(data['petal_width'])

print(template.substitute(string='Dataframe from pandas'))
print(petal)

print(template.substitute(string='Minimum and maximum from dataframe'))
print(petal.min(), petal.max())

print(template.substitute(string='Arithmetic mean'))
print(petal.mean())

print(template.substitute(string='Median'))
print(np.median(petal))

print(template.substitute(string='Standard deviation'))
print(np.std(petal))

print(template.substitute(string='Dispersion'))
print(np.var(petal))

print(template.substitute(string='Percentiles'))
print(np.percentile(petal, 25))
print(np.percentile(petal, 75))
# Operations with data section ends #
