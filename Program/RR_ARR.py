import math
import random
import pandas as pd
import numpy as np

epsilon =1.5
d = 2
dataset = 'CDC_COST'
Dataset = pd.read_csv(dataset+'.csv', header=None)
column = Dataset.iloc[:,0]
num = len(column)
#alpha = 0.312477478953057#adult_salary
#beta = 0.113576046274242#adult_salary
beta = 0.0695299320658368#cdc_cost
alpha = 0.368768623661109#cdc_cost
#p = math.exp(epsilon)/(math.exp(epsilon)-1+d)

p = min(((1-alpha)-(1-beta)*math.exp(epsilon))/((1-d*alpha)-(1-d*beta)*math.exp(epsilon)),1)
print(p)
def ARR(value):
    coin = random.random()
    if coin < p :
        return int(value)
    else :
        
        return int(1-value)




perturb_list = []
count = np.zeros(d).astype(int)
count_est = np.zeros(d).astype(int)
count_real = np.zeros(d).astype(int)
square_error = np.zeros(d)
ave_error = []
for i in range(num):
    value = int(column.iloc[i])
    count_real[value] = count_real[value]+1

q = 1-p
print('q',q)
for i in range(100):
    print(i)
    perturb_list = []
    square_error = np.zeros(d)
    count = np.zeros(d).astype(int)
    count_est = np.zeros(d).astype(int)
    for i in range(num) :
        value = column.iloc[i]
        value_updated = ARR(value)
        perturb_list.append(value_updated)
        count[int(value_updated)] = count[int(value_updated)] + 1
    for i in range(d) :
        count_est[i] = round((count[i]-num *q)/(p-q))
        square_error[i] = (count_est[i]/num-count_real[i]/num)*(count_est[i]/num-count_real[i]/num)
    ave_error.append(np.mean(square_error))

print("MSE:",sum(ave_error)/len(ave_error))
