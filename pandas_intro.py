"""
pandas_intro.py

tutorial material from several sources including
https://github.com/fonnesbeck/statistical-analysis-python-tutorial

"""
import pandas as pd
import numpy as np


""" 
PANDAS DATA STRUCTURES
Series:
    A series is a single vector of data with an index
"""

cnt = pd.Series([632, 1638, 569, 115])
cnt
cnt.values
cnt.index

# you can assign labels to the index
bact = pd.Series([632, 1638, 569, 115],
                 index=['firm', 'prote', 'actino', 'bactero'])
bact
# you can refer to the values by the index
bact['prote']
[name.endswith('o') for name in bact.index]
# also can use positional indexing
bact[0:2]

# can give the array values and index labels
bact.name = 'counts'
bact.index.name = 'phylum'
bact

# can apply numpy math functions and other operations to series and keep structure
np.log(bact)

# filter according to values in the series
bact[bact > 1000]


# A Series can be thought of as a key: value store. in fact they can be created from a dictionary
bac_dict = {'firm': 632, 'proteo': 1632, 'actinobac': 569, 'bactero': 115}
pd.Series(bac_dict)
# note, the series is created in key-sort order...

# if we pass a custom index to Series, it will select the corresponding values from the dict and treat indices
# without corresponding values a s missing - Pandas uses NaN for missing values
bac2 = pd.Series(bac_dict, index=['cyano', 'firm', 'proteo', 'actinobac'])
bac2
bac2.isnull()

# critically the labels are used to align data when used in operations with other series
bact + bac2


""" 
PANDAS DATA STRUCTURES
DataFrame:
    a tabular data structure, similar to a spreadsheet, multiple series in columns with a row index
"""
data = pd.DataFrame({'value': [632, 1638, 569, 115, 433, 1130, 754, 555],
                     'patient': [1, 1, 1, 1, 2, 2, 2, 2],
                     'phylum': ['firmicutes', 'proteobacteria', 'actinobacteria', 'bacteroidetes', 'firmicutes',
                                'proteobacteria', 'actinobacteria', 'bacteroidetes']})
data
# note the DataFrame is sorted by column name - but you can easily change the order
data[['phylum', 'value', 'patient']]

# a dataframe has a second index to represent the columns
data.columns

# to access a column either use dict-like indexing or by attribute
data['value']
data.value
type(data.value)
type(data[['value']])
# notice, this is different than with Series, where dict-like indexing retrived a particular element (row).
# to access a row in a dataframe we index its iloc or loc attribute
data.iloc[3]

# alternatively you can create a DataFrame by a dict of dicts...
data = pd.DataFrame({0: {'patient': 1, 'phylum': 'Firmicutes', 'value': 632},
                    1: {'patient': 1, 'phylum': 'Proteobacteria', 'value': 1638},
                    2: {'patient': 1, 'phylum': 'Actinobacteria', 'value': 569},
                    3: {'patient': 1, 'phylum': 'Bacteroidetes', 'value': 115},
                    4: {'patient': 2, 'phylum': 'Firmicutes', 'value': 433},
                    5: {'patient': 2, 'phylum': 'Proteobacteria', 'value': 1130},
                    6: {'patient': 2, 'phylum': 'Actinobacteria', 'value': 754},
                    7: {'patient': 2, 'phylum': 'Bacteroidetes', 'value': 555}})
data

# probably need it transposed
data = data.T
data

# it is key to note that the Series returned when a DF is indexed is merely a 'view' on the DF and not a copy
# CAREFUL
vals = data.value
vals
vals[5] = 0
vals
data
# hmmm the above actually did adjust the underlying data...

# create/modify columns by assignment
data.value[3] = 14
data

data['year'] = 2013
data

# note, you can not use attribute indexing to add a new column
data.treatment = 1
data

data.treatment


# Specifying a Series as a new column cause its values to be added according to the DF index
treatment = pd.Series([0] * 4 + [1] * 2)
treatment

data['treatment'] = treatment
data

# Other python data structures (without an index) need to be the same size as the DF
month = ['jan', 'feb', 'mar', 'apr']
data['month'] = month
# above fails
data['month'] = ['jan'] * len(data)
data

# we can use 'del' to remove columns - just like dicts
del data['month']
data


# we can extract the underlying data as a simple ndarray by accessing the 'values' attribute
data.values
# because of the mix of types, the dtype of the array is object

df = pd.DataFrame({'foo': [1, 2, 3], 'bar': [0.4, -1.0, 4.5]})
df.values

# Pandas uses a custom data structure to represent the indices of Series and DataFrames
data.index
# index objects are immutable!
data.index[0] = 15
# this is so index objects can be shared between data structures
bac2.index = bact.index
bac2


""" 
PANDAS IMPORTING DATA

    importing data into pandas is quite easy
"""
mb = pd.read_csv("data/microbiome.csv")
mb.head()
mb.shape

# 'read_csv' automatically considers the first row as a header row - many things can be overridden
pd.read_csv("data/microbiome.csv", header=None).head()

# 'read_csv' is just a convenience function of 'read_table' - more generic
mb = pd.read_table("data/microbiome.csv", sep=',')
""" the 'sep' argument can be customized as needed to accommodate other separators including regular expressions
that way you could include extra whitespace in the separator such as
sep='\s+
"""

# also you can specify a more useful index such as
mb = pd.read_csv("data/microbiome.csv", index_col=['Taxon', 'Patient'])
mb.head()
# referred to as a hierarchical index











