#%%
import pandas as pd
# %%
# 1. Write a Pandas program to create and display a one-dimensional 
# array-like object containing an array of data using Pandas module.

# Solution - create a list of a given number of values and
# pass it to the .series  class, as a result a instance of the
# pandas series class will be createed

array = [1, 2, 3, 4]
array_series = pd.Series(array)
print('array_series')



# %%
# 2. Write a Pandas program to convert a Panda module Series to Python
# list and it's type.

# Solution - create a pandas series passing a list of given number of values
# then convert it to a list using the 'list' class
# 

array_series = pd.Series([7, 2, 4, 7])
regular_list = list(array_series)
print(regular_list)
print(type(regular_list))
# %%
# 3. Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]

# ds = ds1 + ds2: This line adds the two Series objects element-wise, resulting in a new Series object 'ds' with the values [3, 7, 11, 15, 19].
# ds = ds1 - ds2: This line subtracts the second Series object from the first Series object element-wise, resulting in a new Series object 'ds' with the values [1, 1, 1, 1, 1].
# ds = ds1 * ds2: This line multiplies the two Series objects element-wise, resulting in a new Series object 'ds' with the values [2, 12, 30, 56, 90].
# ds = ds1 / ds2: This line divides the first Series object by the second Series object element-wise, resulting in a new Series object 'ds' with the values [2.0, 1.333, 1.2, 1.143, 1.111].

ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])
print(f'{ds1}, {ds2}')

ds = ds1 + ds2
print("Add two Series:")
print(ds)
ds = ds1 * ds2
print("Multiply two Series:")
print(ds)
ds = ds1 / ds2
print("Divide Series1 by Series2:")
print(ds)
ds = ds1 - ds2
print("Subtract two Series:")
print(ds)

# %%
# 4. Write a Pandas program to compare the elements of the two Pandas Series.
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]

# print(ds1 == ds2): This line compares the two Series objects using the '==' operator, resulting in a 
# new Series object with boolean values indicating whether the corresponding elements in ‘ds1’ and ‘ds2’ are equal or not.
# The output will be: [False, False, False, False, True]

# print(ds1 > ds2): This line compares the two Series objects using the '>' operator, resulting in a new Series object with
# boolean values indicating whether the corresponding elements in ‘ds1’ are greater than those in ‘ds2’ or not. The output will be:
# [True, True, True, True, False]

# print(ds1 < ds2): This line compares the two Series objects using the '<' operator, resulting in a new Series object with boolean
# values indicating whether the corresponding elements in ‘ds1’ are less than those in ‘ds2’ or not. The output will be:
# [False, False, False, False, False]

ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 10])
print("Series1:")
print(ds1)
print("Series2:")
print(ds2)
print("Compare the elements of the said Series:")
print("Equals:")
print(ds1 == ds2)
print("Greater than:")
print(ds1 > ds2)
print("Less than:")
print(ds1 < ds2)
# %%
# 5. Write a Pandas program to convert a dictionary to a Pandas series.

# pd.Series({'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}): This line creates a new Pandas Series object 'ds' from the given dictionary using the pd.Series() constructor.
# The resulting Series object will have the same keys as the dictionary and the corresponding values as its elements.

import pandas as pd

ds = pd.Series({'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800})
print(ds)

# %%
# 6. Write a Pandas program to convert a NumPy array to a Pandas series.

# ds = pd.Series(numpy): This line creates a new Pandas Series object 'ds' from the NumPy array using the pd.Series() constructor.
# The resulting Series object will have the same values as the NumPy array, and the default index will be assigned to each element starting from 0 and
# increasing by 1 for each subsequent element.

import numpy as np
import pandas as pd
numpy = np.array([10, 20, 30, 40, 50])
ds = pd.Series(numpy)
print(ds)
# %%
# 7. Write a Pandas program to change the data type of given a column or a Series.

# ds = ds = pd.to_numeric(ds, errors='coerce'): This line applies the pd.to_numeric() function to the Series object 'ds' with the 'errors' parameter set to 'coerce'.
# This function attempts to convert each value in the Series object to a numeric type (e.g., integer or float). If a value cannot be converted, it will be replaced with a NaN (not a number) value.
# value in the Series object to a numeric type (e.g., integer or float). If a value cannot be converted, it will be replaced with a NaN (not a number) value.

import pandas as pd

ds = pd.Series([100, 200, 'python', 300.12, 400])
ds = pd.to_numeric(ds, errors='coerce')
ds