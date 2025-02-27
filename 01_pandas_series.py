#%%
import pandas as pd
import numpy as np
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

import pandas as pd

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

import pandas as pd

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

import pandas as pd

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
# %%
# 8. Write a Pandas program to convert the first column of a DataFrame as a Series.

import pandas as pd  # Import the pandas library for data manipulation and analysis.

# Create a DataFrame named 'df' with three columns: 'col1', 'col2', and 'col3'.
df = pd.DataFrame({'col1': [1, 2, 3, 4, 7, 11],   # 'col1' contains six integers.
                   'col2': [4, 5, 6, 9, 5, 0],   # 'col2' contains six integers.
                   'col3': [7, 5, 8, 12, 1, 11]} # 'col3' contains six integers.
                  )

# Extract the first column ('col1') from the DataFrame using its index (0) 
# and convert it into a pandas Series object.
ds = pd.Series(df.iloc[:, 0])  # 'ds' now holds the values from 'col1' as a pandas Series.
ds

# %%
#9. Write a Pandas program to convert a given Series to an array.
import pandas as pd
import numpy as np

# Create a pandas Series object named 'ds' with mixed data types (integer, string, and float).
ds = pd.Series([100, 200, 'python', 300.12, 400])

# Convert the pandas Series 'ds' into a numpy array and store it in the variable 'array'.
array = np.array(ds)

# Display the contents of the numpy array.
array

# Print the type of the 'array' variable to confirm it's a numpy array.
print(type(array))
# %%
# 10. Write a Pandas program to convert Series of lists to one Series.
import pandas as pd


place_holder = []
ds = pd.Series([['Red', 'Green', 'White'], ['Red', 'Black'], ['Yellow']])
for i, item in enumerate(ds):
    for word in item:
     place_holder.append(word)
ds = pd.Series(place_holder)
ds


# %%
# 10.1 Write a Pandas program to convert Series of lists to one Series.
import pandas as pd

# Create a pandas Series where each element is a list of colors
ds = pd.Series([['Red', 'Green', 'White'], ['Red', 'Black'], ['Yellow']])

# Apply 'pd.Series' to each element of the Series to split the lists into separate columns.
# Then, 'stack()' combines these columns into a single series, stacking non-null values vertically.
ds = ds.apply(pd.Series).stack().reset_index(drop=True)

# Reset the index of the resulting series to provide a clean, sequential index
# 'drop=True' ensures the old index is discarded.

print(ds)
# %%
#11. Write a Pandas program to sort a given Series.
import pandas as pd

# Step 1: Create a pandas Series with mixed types of data as strings
ds = pd.Series(['100', '200', 'python', '300.12', '400'])

# Step 2: Sort the values in the Series
# Since the data is stored as strings, the sorting will be lexicographical (alphabetical order),
# not numerical. This means numbers will be sorted as text (e.g., "100" comes before "300.12").
ds = pd.Series(ds).sort_values()
print(ds)
# %%
# 12. Write a Pandas program to add some data to an existing Series.
import pandas as pd

# Step 1: Create a pandas Series with mixed data types as strings
ds = pd.Series(['100', '200', 'python', '300.12', '400'])

# Step 2: Concatenate the original Series with a new Series containing additional values ('500' and 'php')
# - 'pd.concat' is used to combine two Series objects into one.
# - 'ignore_index=True' ensures that the index is reset for the resulting Series.
ds = pd.concat([ds, pd.Series(['500', 'php'])], ignore_index=True)
ds
# %%
# 13. Write a Pandas program to create a subset of a given series based on value and condition.

# Sample Output:
# Original Data Series:
# 0      0
# 1      1
# 2      2
#.........
# 10    10
import pandas as pd

# Step 1: Create a pandas Series with numeric values from 1 to 10
ds = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Step 2: Define the threshold value 'n' for filtering
n = 4

# Step 3: Create a subset of the Series
# - 'ds < n' generates a boolean mask (True for values less than 'n', False otherwise).
# - Using this mask, the Series is filtered to only include values less than 'n'.
ds = ds[ds < n]
ds
# %%
# 14. Write a Pandas program to change the order of index of a given series.
import pandas as pd

# Step 1: Create a pandas Series with numeric values from 1 to 10
ds = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Step 2: Sort the Series by its index in descending order
# - 'sort_index()' reorders the Series based on its index.
# - 'ascending=False' specifies that the sorting should be done in descending order.
ds = ds.sort_index(ascending=False)

# The Series is now sorted so that the last index (9) is first, and the first index (0) is last.
ds

# %%
# 15. Write a Pandas program to create the mean and standard deviation of the data of a given Series.
import pandas as pd

# Step 1: Create a pandas Series with numeric values from 1 to 10
ds = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Step 2: Calculate and print the mean and standard deviation
# - 'ds.mean()' computes the mean (average) of the Series.
# - 'ds.std()' computes the standard deviation of the Series.
# - ':.5f' formats the standard deviation to 5 decimal places.
print(f'Mean value {ds.mean()}, Standard deviation {ds.std():.5f}')

# %%
# 16. Write a Pandas program to get the items of a given series not present in another given series.
import pandas as pd

ds1 = pd.Series([1, 2, 3, 4, 5])
ds2 = pd.Series([2, 4, 6, 8, 10])

# Get items in ds1 that are not in ds2
# This is done by applying a boolean mask to the original Series object using the .isin() method to check which elements in 'ds1' are present in 'ds2',
# and then negating the boolean mask using the tilde (~) operator.
ds_new = ds1[~ds1.isin(ds2)]
ds_new

# %%
# 17. Write a Pandas program to get the items which are not common of two given series.
import pandas as pd
import numpy as np

ds1 = pd.Series([1, 2, 3, 4, 5])
ds2 = pd.Series([2, 4, 6, 8, 10])
# Get the items which are not common between series1 and series2
# '[ds1[~ds1.isin(ds2)]' items that are in series 1 and not in 2
# 'ds2[~ds2.isin(ds1)]]' items that are in series 2 and not in 1
result = pd.concat([ds1[~ds1.isin(ds2)], ds2[~ds2.isin(ds1)]])
result
# %%
# 18. Write a Pandas program to compute the minimum, 25th percentile, median, 75th, and maximum of a given series.
import pandas as pd
import numpy as np

# Create a random number generator with a fixed seed (100)
num_state = np.random.RandomState(100)

# Generate a series of 20 random numbers from a normal distribution (mean=10, std=4)
num_series = pd.Series(num_state.normal(10, 4, 20))

# Calculate the percentiles: minimum (0%), 25th percentile, median (50%), 75th percentile, and maximum (100%)
result = np.percentile(num_series, q=[0, 25, 50, 75, 100])

# Print the results
print('Minimum, 25th percentile, median, 75th, and maximum of a given series:')
print(result)

# %%

# 19. Write a Pandas program to calculate the frequency counts of each unique value of a given series.
import pandas as pd
import numpy as np

# Generate a series of random digits as strings
num_series = pd.Series(np.take(list('0123456789'), np.random.randint(10, size=20)))

# Get the counts of unique values in the series
result = num_series.value_counts()

print(num_series)
print(result)


# %%
# 20. Write a Pandas program to display most frequent value in a given series and replace everything else as 'Other' in the series.
import pandas as pd
import numpy as np

# Create a pandas Series with 10 random integers between 1 and 4 (inclusive)
num_series = pd.Series(np.random.randint(1, 5, [10]))

# Identify the most frequent value in the series and replace all other values with 'Other'
# - num_series.value_counts() counts how many times each value appears and sorts them in descending order.
# - num_series.value_counts().index[:1] extracts the most frequent value (the first element of the index).
# - num_series.isin(...) creates a boolean mask that is True where the series values are in the list of the most frequent value.
# - The ~ operator negates the boolean mask, so it becomes True for values that are NOT the most frequent.
# - The assignment replaces all values that are not the most frequent with the string 'Other'.
num_series[~num_series.isin(num_series.value_counts().index[:1])] = 'Other'

# Print the updated series
print(num_series)

# %%
#21. Write a Pandas program to find the positions of numbers that are multiples of 5 of a given series.

import pandas as pd
import numpy as np

# Create a pandas Series with 9 random integers between 1 and 9 (inclusive)
num_series = pd.Series(np.random.randint(1, 10, 9))
# Print the original Series to see the random numbers generated
print(num_series)

# Create a boolean mask where each element is True if it is a multiple of 5, and False otherwise.
# The condition (num_series % 5 == 0) checks if a number leaves a remainder of 0 when divided by 5.
# np.where returns the indices where this condition is True.
result = np.where(num_series % 5 == 0)

# Print the indices of the Series where the numbers are multiples of 5
print(result)

# %%
#22. Write a Pandas program to extract items at given positions of a given series.
import pandas as pd

# Create a pandas Series by converting the string into a list of characters.
num_series = pd.Series(list('2390238923902390239023'))

# Define a list of integer positions for the elements we want to extract.
element_pos = [0, 2, 6, 11, 21]

# Use .iloc for positional indexing to extract elements at the specified positions.
result = num_series.iloc[element_pos]

# Print the extracted elements.
print(result)
# %%
#23. Write a Pandas program to get the positions of items of a given series in another given series.
import pandas as pd
import numpy as np

# Create the first Series with values 1 through 10.
series1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Create the second Series with a subset of numbers that we want to locate in series1.
series2 = pd.Series([1, 3, 5, 7, 10])

# Convert series1 into an Index object and for each element in series2, find its position in series1.
# pd.Index(series1) creates an Index object from series1.
# .get_loc(i) returns the integer location of the element i in the index.
# The list comprehension loops over each element i in series2 and collects the positions.
result = [pd.Index(series1).get_loc(i) for i in series2]

# Print the list of positions corresponding to each element of series2 in series1.
print(result)
# %%
#24. Write a  Pandas program convert the first and last character of each word to upper case in each word of a given series.
import pandas as pd
import numpy as np


# Define a function that takes a string and returns the modified string
def transform_string(x):
    # Capitalize the first character, keep the middle part unchanged,
    # and capitalize the last character.
    return x[0].upper() + x[1:-1] + x[-1].upper()

# Create the pandas Series
series1 = pd.Series(['php', 'python', 'java', 'c#'])

# #the map() function applies a given function (in this case, the transform_string) to every element in the Series.

result = series1.map(transform_string)

# Print the result
print(result)
# %%
#25. Write a Pandas program to calculate the number of characters in each word in a given series.
import pandas as pd

# Create a pandas Series containing several strings.
series1 = pd.Series(['php', 'python', 'java', 'c#'])

# Use the .map() method to apply a function to each element of the Series.
# The lambda function takes each string 'x' and returns its length using len(x).
result = series1.map(lambda x: len(x))

# Print the resulting Series, which contains the lengths of the strings from series1.
print(result)

# %%
#26. Write a Pandas program to compute difference of differences between consecutive numbers of a given series.
import pandas as pd

# Create a pandas Series with a list of numbers.
series1 = pd.Series([1, 3, 5, 8, 10, 11, 15])

# Calculate the first differences between consecutive elements.
# .diff() computes the difference between each element and its previous element.
# The first element will be NaN because there is no previous element.
first_diff = series1.diff()
print(first_diff.tolist())
# Output: [NaN, 2.0, 2.0, 3.0, 2.0, 1.0, 4.0]
# Explanation:
# 3 - 1 = 2, 5 - 3 = 2, 8 - 5 = 3, 10 - 8 = 2, 11 - 10 = 1, 15 - 11 = 4

# Calculate the second differences between consecutive first differences.
# .diff().diff() computes the differences of the first differences.
# Again, the first element will be NaN, and the next will be NaN as well since it compares with NaN.
second_diff = series1.diff().diff()
print(second_diff.tolist())
# Output: [NaN, NaN, 0.0, 1.0, -1.0, -1.0, 3.0]
# Explanation:
# The differences of the first differences: (2-2)=0, (3-2)=1, (2-3)=-1, (1-2)=-1, (4-1)=3.

# %%
