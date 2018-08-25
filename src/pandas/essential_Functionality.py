# this section contain the basic function to deal with data which is available in
# series or DataFrames

import pandas as pd
import numpy as np

series_1 = pd.Series([4.5, 7.2, - 5.3, 3.6], index=['d', 'b', 'a', 'c'])
print(series_1)

series_1 = series_1.reindex(['a', 'b', 'c', 'd', 'e'])
print(series_1)

# Forward fill method: This will allow to fill NaN values
# so this method is forward fill it will not fill the backward or previous values
series_2 = pd.Series(['blue', 'yellow', 'green'], index=[1, 2, 3])
print(series_2)
series_2 = series_2.reindex(range(6), method='ffill')
print(series_2)

# reindexing with DataFrames
data_1 = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'b', 'c'], columns=['MH', 'TN', 'GOA'])
print(data_1)
data_1 = data_1.reindex(['b', 'c', 'a', 'xx', 'zz', 'yy'])
print(data_1)
states = ['AP', 'MH', 'GOA', 'TN', 'HYD', 'JK']
data_1 = data_1.reindex(columns=states)
print(data_1)
data_1 = data_1.loc[['yy', 'xx', 'zz', 'a', 'b', 'c'], states]
print(data_1)

# droping entries form and axis
series_3 = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print(series_3)

series_4 = series_3.drop('c')
print(series_4)

series_4 = series_3.drop(['b', 'c'])
print(series_4)
# droping values form dataframes

data_2 = pd.DataFrame(np.arange(9).reshape((3, 3)), index=[0, 1, 2], columns=['name', 'state', 'pop'])
print(data_2)
data_row = data_2.drop(1)
print(data_row)
data_col = data_2.drop('name', axis=1)
print(data_col)

# if you want to operate drop method in-place then just put in-place=True in drop method
data_2.drop('state', axis=1, inplace=True)
print(data_2)

# indexing selection and filtering
##indexing in series
series_5 = pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
print(series_5)
print(series_5['b'])
print(series_5[1:3])
print(series_5[['e', 'a', 'd']])
print(series_5[[1, 3, 0]])
print(series_5['b': 'c'])

##indexing into DataFrames
data_3 = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['MH', 'AP', 'JP', 'NY'],
                      columns=['one', 'two', 'three', 'four'])
print(data_3)
print(data_3['two'])
print(data_3[['two','one']])
#in data frame indexing we see bellow
print(data_3 >5)    # this will give the boolean array

#one more feture of pandas over NumPy
print(data_3)

data_3[data_3 > 5] = 1
print(data_3)

##Selecting through loc and iloc

#loc :- this will allow tho select row as well as column by index
print(data_3.loc['MH',['two', 'three']])

#iloc :- this will allow to select same thing by integers
print(data_3.iloc[2, [3, 0, 2]])
