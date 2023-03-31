import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt


#reading the data file
dataformat = pd.read_csv('final_chatGPTdata.csv')

#list columns that are redundant to our pie chart
dropped  = ['What purpose does ChatGPT serve you? Select all that apply. ', 'How can academic institutions effectively use ChatGPT?', 'What are the main issues surrounding the use of ChatGPT in higher education?']

#drop the columns we don't need
df = dataformat.loc[:, ~dataformat.columns.isin(dropped)]


#iterating through our updated columns
for cat in df.columns:
        #get the data and appropriate labels 
        your_values = df[cat].value_counts() #data values of our pie chart
        label = df[cat].unique() #label of values
   
        fig = plt.subplots(figsize=(16,9)) #plot the pie chart   
        plt.title(cat, pad=10)#title of our pie chart
        plt.pie(your_values,autopct='%.2f%%') #format, show percentages values 
        plt.legend(label,loc='upper right') #legend of our pie chart
        
        


plt.show() #show the pie chart in a window
