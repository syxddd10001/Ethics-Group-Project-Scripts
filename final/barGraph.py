import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

#reading the csv file using pandas
dataformat = pd.read_csv('final_chatGPTdata.csv')

# list of what we want to show on the bar graph
purpose  = ['What purpose does ChatGPT serve you? Select all that apply. ']
use  = ['How can academic institutions effectively use ChatGPT?']
issues  = ['What are the main issues surrounding the use of ChatGPT in higher education?']


# converting columns to data format 
dfp = dataformat[purpose]
dfu = dataformat[use]
dfi = dataformat[issues]

# dictionaries to hold labels and values of our data
purpose_dict = {}
use_dict = {}
issues_dict = {}

# iterating through purpose column to get the relevant data 
for d in dfp.columns:
        #get the data and appropriate labels 
        your_values = dfp[d].value_counts() #data values of our graph
        label = dfp[d] #label of values
        # counting the number of values for each label
        for x in label:
                # converting it to a list and adding it to our dictionary if the label doesnt exist
                for n in x.split(", "):
                        if n not in purpose_dict:
                                purpose_dict[n] = 1
                        else:
                                purpose_dict[n] +=1
                                # if the label exists, just add the count
        
  
# turning the data labels and values as lists for plotting 
purposeName = list(purpose_dict.keys())
purposeValue = list(purpose_dict.values())

# plotting the graph, setting figure size and setting title 
figp,axp = plt.subplots(figsize=(16,9))
axp.barh(purposeName,purposeValue,color='green')
axp.invert_yaxis()
axp.set_title('What Purpose Does ChatGPT Serve You',fontweight='bold')


# adding values beside the bars graphs so the graph is more readable
for i in axp.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5,
                str(round((i.get_width()), 2)),
                fontsize = 10, fontweight='bold',
                color='black')

# font size of the y axis
plt.yticks(fontsize=7.5)






# doing the same thing but for use column
for d in dfu.columns:
          
        your_values = dfu[d].value_counts() #data values of our graph
        label = dfu[d] #label of values       
        # counting the number of values for each label
        for x in label:
                for n in x.split(", "):
                        if n not in use_dict:
                                use_dict[n] = 1

                        else:
                                use_dict[n] +=1
        
# plotting graph
useName = list(use_dict.keys())
useValue = list(use_dict.values())
figu,axu = plt.subplots(figsize=(16,9))
axu.barh(useName,useValue,color='orange')
axu.invert_yaxis()

# values beside the bar graphs
for i in axu.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5,
                str(round((i.get_width()), 2)),
                fontsize = 10, fontweight='bold',
                color='black')

# setting title and y axis font
axu.set_title('How can academic institutions effectively use ChatGPT?',fontweight='bold')
plt.yticks(fontsize=6.5)



# same with issues column
for d in dfi.columns:
        #get the data and appropriate labels    
        your_values = dfi[d].value_counts() #data values of our graph
        label = dfi[d] #label of values       
        # counting how many values we have
        for x in label:
                for n in x.split(", "):
                        if n not in issues_dict:
                                issues_dict[n] = 1

                        else:
                                issues_dict[n] +=1
        
#plotting graph
issuesName = list(issues_dict.keys())
issuesValue = list(issues_dict.values())
figi,axi = plt.subplots(figsize=(16,9))
axi.barh(issuesName,issuesValue,color='purple')
axi.invert_yaxis()

# values beside the bar graph
for i in axi.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5,
                str(round((i.get_width()), 2)),
                fontsize = 10, fontweight='bold',
                color='black')

# setting title and changing font size of y axis
axi.set_title('What are the main issues surrounding the use of ChatGPT in higher education?',fontweight='bold')
plt.yticks(fontsize=6)

# making the graphs appear on the screen
plt.show()
