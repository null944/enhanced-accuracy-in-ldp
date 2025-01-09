import numpy as np
import pandas as pd
import math
import random

epsilon=1.5

# generate missing dataset
dataset = 'GentH'
d = 5
mechanism = 'MNAR'
Dataset = pd.read_csv(dataset+'.csv', header=None)
num = len(Dataset)# the number of users
miss_list = np.loadtxt(dataset+'_1_miss_'+mechanism+'.csv', delimiter=",", skiprows=0)            
for row in miss_list:
    i, j = int(row[0]), int(row[1])
    Dataset.iloc[i, j] = int(0)

p = math.exp(epsilon)/(math.exp(epsilon)+d)
print('p',p)
q = 1/(math.exp(epsilon)+d)
column = Dataset.iloc[:,0].copy()
def UP (value):
    possible_values = list(range(d+1))
    coin = random.random()
    if coin < p:
        return value
    else:
        possible_values.remove(value)
        return random.choice(possible_values)
    
perturb_list = []
count = np.zeros(d+1).astype(int)
count_est = np.zeros(d+1).astype(int)
count_real = np.zeros(d+1).astype(int)
square_error = np.zeros(d+1)
ave_error = []
for i in range(num):
    value = int(column.iloc[i])
    count_real[value] = count_real[value]+1


for i in range(100):
    perturb_list = []
    square_error = np.zeros(d+1)
    count = np.zeros(d+1).astype(int)
    count_est = np.zeros(d+1).astype(int)
    print(i)
    for i in range(num) :
        value = column.iloc[i]
        value_updated = UP(value)
        perturb_list.append(value_updated)
        count[int(value_updated)] = count[int(value_updated)] + 1
    for i in range(d+1) :
        count_est[i] = round((count[i]-num *q)/(p-q))
        #square_error[i] = (count_est[i]/num-count_real[i]/num)*(count_est[i]/num-count_real[i]/num)
    sum1 = sum(count_est)
    for j in range(d+1):
        square_error[j] = (count_est[j]/sum1-count_real[j]/num)*(count_est[j]/sum1-count_real[j]/num)
    ave_error.append(np.mean(square_error))
print("MSE:",sum(ave_error)/len(ave_error))

