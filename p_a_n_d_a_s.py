
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
'''df = pd.read_csv('data.csv')
print(df.to_string())
'''
'''
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)
print(pd.__version__)
print(np.__version__)
'''

'''a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
print(myvar[2])

import pandas as pd

a = ["RAM", "PRASAD", "AMARAPU"]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)


calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
'''

'''import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)
'''
'''import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data, index =["a", "b","c"] )

print(myvar)
print(myvar)
print(myvar.loc["a"])
print(myvar.loc[['b']])'''
import pandas as pd
# c_s_v = pd.read_csv("data1.csv")
# c_s_v_1 = pd.read_csv("data.csv")

# print(c_s_v_1)
# # print(c_s_v)
# # print(c_s_v.to_string())
# pd.options.display.max_rows = 2457609
# print(pd.options.display.max_rows)

'''df = pd.read_json("data.json")
print(df.to_string())
print(df.head(20))  # it will give you the startings rows overview
print(df.tail())    # it will give you the last rows overview
print(df.info())'''

'''import pandas as pd

df = pd.read_csv('data1.csv')

# new_df = df.dropna()
# df["Calories"].fillna(128, inplace = True)
x = df["Calories"].mode()[0]
# df.fillna(130,inplace = True)
print(df.to_string())'''

# df = pd.read_csv('data1.csv')

# df['Date'] = pd.to_datetime(df['Date'])
# df.loc[7, 'Calories'] = 45

# for x in df.index:
#   if df.loc[x, "Calories"] > 120:
#     df.loc[x, "Calories"] = 120

# print(df.to_string())
# print(df.duplicated())

df = pd.read_csv('data2.csv')
print(df.corr())
# df.plot(kind = "scatter", x= 'Calories', y= 'Duration' ) 
df.plot(kind = "hist", x= 'Calories', y= 'Duration' ) 
plt.show()