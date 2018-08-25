import pandas as pd
from pandas import Series, DataFrame

# series : 1darray of simillar type of data

obj = pd.Series([1, 2, 3, 4])
print(" this is a series : {}".format(obj))

print("get value without index : {}".format(obj.values))
print("get index with out the values : {}".format(obj.index))

# creating series with its index associalted with the elements

obj2 = pd.Series([1, 2, 3, 4], ['a', 'c', 'b', 'd'])
print("the user defined series with an index  : {}".format(obj2))
print("the value of the index a {}".format(obj2['a']))

# creating the series form the dict

dict_1 = {1: 'a', 2: 'b', 3: 'c'}
obj_3 = pd.Series(dict_1)
print("The series form the dict : {}".format(obj_3))
print(obj2.isnull())
print(obj_3 + obj2)
obj.index = ['a', 'b', 'c', 'd']
print(obj + obj2)

# DataFrames
##creating Dataframe

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

datFrame = pd.DataFrame(data, columns=['year', 'pop', 'state', 'test'])
print(datFrame.index)
import numpy as np

# modifying column
datFrame['test'] = np.arange(6.)
print(datFrame)
datFrame['may'] = '15'
print("the creation of column: {}".format(datFrame))

## Nested dicts :
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
nes_df = pd.DataFrame(pop)
print("[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]][][][]")
#setting name attribute to the column and rows
datFrame.index.name = 'states'
datFrame.columns.name = 'states'
print(datFrame)
lables = datFrame.index
print(lables)
test_1 = pd.Series(range(6),index=['bar', 'bar', 'foo', 'foo', 'bar', 'tar'])
print(test_1)