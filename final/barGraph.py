import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from tabulate import tabulate

dataformat = pd.read_csv('final_ChatGPTdata.csv')

purpose  = ['What purpose does ChatGPT serve you? Select all that apply. ']
use  = ['How can academic institutions effectively use ChatGPT?']
issues  = ['What are the main issues surrounding the use of ChatGPT in higher education?']



dfp = dataformat[purpose]
dfu = dataformat[use]
dfi = dataformat[issues]


purpose_dict = {}
use_dict = {}
issues_dict = {}

# purpose
for d in dfp.columns:
        #get the data and appropriate labels 
        
        your_values = dfp[d].value_counts() #data values of our pie chart
        label = dfp[d] #label of values       
        
        for x in label:
                for n in x.split(", "):
                        if n not in purpose_dict:
                                purpose_dict[n] = 1
                        else:
                                purpose_dict[n] +=1
        
        
  

purposeName = list(purpose_dict.keys())
purposeValue = list(purpose_dict.values())
figp,axp = plt.subplots(figsize=(16,9))
axp.barh(purposeName,purposeValue,color='green')
axp.invert_yaxis()
axp.set_title('What Purpose Does ChatGPT Serve You',fontweight='bold')



for i in axp.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5,
                str(round((i.get_width()), 2)),
                fontsize = 10, fontweight='bold',
                color='black')

plt.yticks(fontsize=6)






#use
for d in dfu.columns:
        #get the data and appropriate labels    
        your_values = dfu[d].value_counts() #data values of our pie chart
        label = dfu[d] #label of values       

        for x in label:
                for n in x.split(", "):
                        if n not in use_dict:
                                use_dict[n] = 1

                        else:
                                use_dict[n] +=1
        

useName = list(use_dict.keys())
useValue = list(use_dict.values())
figu,axu = plt.subplots(figsize=(16,9))
axu.barh(useName,useValue,color='orange')
axu.invert_yaxis()

for i in axu.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5,
                str(round((i.get_width()), 2)),
                fontsize = 10, fontweight='bold',
                color='black')


axu.set_title('How can academic institutions effectively use ChatGPT?',fontweight='bold')
plt.yticks(fontsize=6)



#issues
for d in dfi.columns:
        #get the data and appropriate labels    
        your_values = dfi[d].value_counts() #data values of our pie chart
        label = dfi[d] #label of values       

        for x in label:
                for n in x.split(", "):
                        if n not in issues_dict:
                                issues_dict[n] = 1

                        else:
                                issues_dict[n] +=1
        

issuesName = list(issues_dict.keys())
issuesValue = list(issues_dict.values())
figi,axi = plt.subplots(figsize=(16,9))
axi.barh(issuesName,issuesValue,color='purple')
axi.invert_yaxis()

for i in axi.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5,
                str(round((i.get_width()), 2)),
                fontsize = 10, fontweight='bold',
                color='black')


axi.set_title('What are the main issues surrounding the use of ChatGPT in higher education?',fontweight='bold')
plt.yticks(fontsize=4.4)



plt.show()