import pandas as pd
import numpy as np

df = pd.read_csv("Health form.csv")


df.sort_values(["What's your age group?"],
               axis=0,
               ascending=[True],
               inplace=True)

df.tail()


