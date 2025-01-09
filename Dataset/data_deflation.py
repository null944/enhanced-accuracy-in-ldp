import pandas as pd

dataset = 'GentH_1.csv'
df = pd.read_csv(dataset,header=None)
d = 5
x_max = d
x_min = 1
a = 2/(x_max-x_min)
b = 1-((2*x_max)/(x_max-x_min))
df[0] = a * df[0] + b
df.to_csv(dataset,header=False,index=False) 
