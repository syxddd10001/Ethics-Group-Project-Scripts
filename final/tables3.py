import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
#this works properly

#reading the data file
dataformat = pd.read_csv('final_ChatGPTdata.csv')

#list columns that are redundant to our pie chart
coldrop = ['What purpose does ChatGPT serve you? Select all that apply.', 'How can academic institutions effectively use ChatGPT?', 'What are the main issues surrounding the use of ChatGPT in higher education?']

#drop the columns we don't need
df = dataformat.loc[:, ~dataformat.columns.isin(coldrop)]


#print relevant data
print(df.groupby(['Academic Discipline'])['Describe your ChatGPT usage'].value_counts())
print(" ")
print(df.groupby(['What post-secondary institution are you currently enrolled in? '])['Describe your ChatGPT usage'].value_counts())
print(" ")
print(df.groupby(['Employment Status / Extra Activities'])['Describe your ChatGPT usage'].value_counts())
print(" ")


plt.show()
