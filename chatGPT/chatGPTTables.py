import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from tabulate import tabulate
dataformat = pd.read_csv('ChatGPTDATA.csv')


#dataformat.sort_values(["Age Group"],
 #              axis=0,
  #             ascending=[True],
   #            inplace=True)

maxl = 50
#dataformat
for columns in dataformat.columns:
    if dataformat[columns].dtype == 'object':
        dataformat[columns] = dataformat[columns].str.slice(0,maxl)

pd.set_option('display.max_colwidth', 20)

table = dataformat.values.tolist()

headers = dataformat.columns.tolist()

output = tabulate(table, headers, tablefmt='pretty')

print(output)

#print((dataformat['Age Group'] == 'Less than 18').sum())
