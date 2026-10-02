####___DATAFRAME___####

# 1.
import pandas as pd

data = {
    'calories':[420, 911, 99],
    'duration':[50, 60, 70]
}
myvar = pd.DataFrame(data)
print(myvar)


# 2. 

import pandas as pd
data = {
    'calories':[420, 911, 99],
    'duration':[50, 60, 70]
}
myvar = pd.DataFrame(data)
print(myvar.loc[0])


# 3.

import pandas as pd
data = {
    'calories':[420, 911, 99],
    'duration':[50, 60, 70]
}
myvar = pd.DataFrame(data)
print(myvar.loc[[0, 1]])


# 4. Indexing Data

import pandas as pd
data = {
    'calories':[420, 911, 99],
    'duration':[50, 60, 70]
}
myvar = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(myvar)


# 5. Data Cleaning

import pandas as pd
data = {
    'A': [420, 911, 99, 1, 118],
    'B': [50, 60, 70, 80, 90],
    'C': [1, None, None, 4, 5],
    'D': [100, 200, 300, None, 500]
}

myvar = pd.DataFrame(data)
print("Original Data:\n")
print (myvar)

myvarcleaned = myvar.dropna()
print("Cleaned Data:\n")
print(myvarcleaned)


#6. 
import pandas as pd

# define a dictionary with sample data which includes some missing values
data = {
    'A': [1, 2, 3, None, 5],
    'B': [None, 2, 3, 4, 5],
    'C': [1, 2, None, None, 5],
}

df = pd.DataFrame(data)
print("Original Data:\n", df)
print()

# use dropna() to remove rows with any missing values
df_cleaned = df.dropna()


# 7. To fill the missing values

import pandas as pd

#define a dictionary with sample data which includes some missing values
data = {
    'A': [1, 2, 3, None, 5],
    'B': [None, 2, 3, 4, 5],
    'C': [1, 2, None, None, 5],
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# Filling none values with 0
df.fillna (0, inplace=True)


# 8. Use aggregate Functions to Fill Missing values
import pandas as pd

# define a dictionary with sample data which includes some missing values
data = {
    'A': [1, 2, 3, None, 5],
    'B': [None, 2, 3, 4, 5],
    'C': [1, 2, None, None, 5],
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# Filling NaN values with mean of each column
df.fillna(df.mean(), inplace=True)



# 9. Handle Duplicate Values

import pandas as pd

#Sample Data
data = {
    'A': [1, 2, 2, 3, 3, 4],
    'B': [5, 6, 6, 7, 8, 8]
}

df = pd.DataFrame(data)
print ("Original Dataframe:\n", df.to_string(index=False))

# Detect Duplicates
print("Duplicate Rows:\n", df[df.duplicated()].to_string(index = False))

# remove duplicates based on column 'A'
df.drop_duplicates(subset=['A'], keep'first', inplace=True)
print("DataFrame after removing duplicates based on column 'A'\n", df.to_string(index = False))



# 10. Rename Column Names to Meaningful Names

import pandas as pd

#Sample Data
data = {
    'A': [25, 30, 35],
    'B': ['John', 'Doe', 'Smith'],
    'C': [5000, 6000, 7000]
}

df = pd.DataFrame(data)

# Rename Columns
df.rename(columns={'A', 'Age', 'B', 'Name', 'C', 'Salary'},
          inplace=True)
print(df.to_string(index=False))