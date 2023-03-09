import pandas as pd
import numpy as np
import csv

dataformat = pd.read_csv('ChatGPTDATA.csv')

dataformat.sort_values(["Age Group"],
               axis=0,
               ascending=[True],
               inplace=True)


dataformat

#print((dataformat['Age Group'] == 'Less than 18').sum())
