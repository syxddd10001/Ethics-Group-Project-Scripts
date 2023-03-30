import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from tabulate import tabulate
dataformat = pd.read_csv('copyChatGPTDATA.csv')

cols_to_drop = ['What purpose does ChatGPT serve you? Select all that apply.', 'How can academic institutions effectively use ChatGPT?', 'What are the main issues surrounding the use of ChatGPT in higher education?']

#dataformat.sort_values(["Age Group"],
 #              axis=0,
  #             ascending=[True],
   #            inplace=True)

df = dataformat.loc[:, ~dataformat.columns.isin(cols_to_drop)]


maxl = 50
#dataformat
for columns in dataformat.columns:
    if dataformat[columns].dtype == 'object':
        dataformat[columns] = dataformat[columns].str.slice(0,maxl)

pd.set_option('display.max_colwidth', 20)

table = dataformat.values.tolist()

headers = dataformat.columns.tolist()

output = tabulate(table, headers, tablefmt='pretty')

df
#print((dataformat['Age Group'] == 'Less than 18').sum())
