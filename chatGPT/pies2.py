import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

dataformat = pd.read_csv('copyChatGPTDATA.csv')

cols_to_drop = ['What purpose does ChatGPT serve you? Select all that apply.', 'How can academic institutions effectively use ChatGPT?', 'What are the main issues surrounding the use of ChatGPT in higher education?']

# Use the loc method to drop the columns
df = dataformat.loc[:, ~dataformat.columns.isin(cols_to_drop)]



for cat in df.columns:
        your_values = df[cat].value_counts()
        label = df[cat].unique()
        fig = plt.figure()
        
        plt.pie(your_values,autopct='%.2f%%')
        plt.title(cat, pad=10)
        plt.legend(label,loc='best')
        
        


plt.show()