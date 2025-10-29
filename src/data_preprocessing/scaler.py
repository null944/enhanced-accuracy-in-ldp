import pandas as pd

dataset = 'adult_salary'
df = pd.read_csv('./data/processed/'+ dataset+'.csv', header=None)
d = 2
x_max = df[0].max()
x_min = df[0].min()
a = 2/(x_max-x_min)
b = 1-((2*x_max)/(x_max-x_min))
df[0] = a * df[0] + b
df.to_csv('./data/processed/' + dataset + '_1.csv', header=False, index=False)