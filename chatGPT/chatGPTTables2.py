import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from tabulate import tabulate
#dataformat = pd.read_csv('copyChatGPTDATA.csv')


# Use list comprehension to remove the unwanted column in **usecol**
df= pd.read_csv('copyChatGPTDATA.csv')

cols_to_drop = ['What purpose does ChatGPT serve you? Select all that apply.', 'How can academic institutions effectively use ChatGPT?', 'What are the main issues surrounding the use of ChatGPT in higher education?']

# Use the loc method to drop the columns
df = df.loc[:, ~df.columns.isin(cols_to_drop)]


maxl = 50
#dataformat

for columns in df.columns:
    if df[columns].dtype == 'object':
        df[columns] = df[columns].str.slice(0,maxl)

pd.set_option('display.max_colwidth', 20)


table = df.values.tolist()

headers = df.columns.tolist()

output = tabulate(table, headers, tablefmt='pretty')

print(output)

#print((dataformat['Age Group'] == 'Less than 18').sum())
