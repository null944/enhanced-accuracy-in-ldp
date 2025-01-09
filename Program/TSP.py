import math
import pandas as pd
import numpy as np
import random

epsilon = 1.5
dataset='GentH'
d = 5
mechanism = 'MNAR' 
Dataset = pd.read_csv(dataset+'.csv', header=None)
num = len(Dataset)
column = Dataset.iloc[:,0].copy()
count1 = np.zeros(d).astype(int)
count2 = np.zeros(d).astype(int)
for i in range(num):
    value = int(column.iloc[i])
    count1[value-1] = count1[value-1]+1
miss_list = np.loadtxt(dataset+'_1_miss_'+mechanism+'.csv', delimiter=",", skiprows=0)               
for row in miss_list:
    i, j = int(row[0]), int(row[1])
    value = int(column.iloc[i])
    Dataset.iloc[i, j] = 0
    
    count2[value-1] = count2[value-1]+1

column = Dataset.iloc[:,0].copy()

missing_rate = np.zeros(d)
for i in range(d):
    if count1[i] != 0:
        missing_rate[i] = count2[i] / count1[i]
    else:
        missing_rate[i] = np.nan

b = np.nanmin(missing_rate)
a = np.nanmax(missing_rate)
if a/b < (1-b)/(1-a):
    alpha = 1 - b
    beta = 1 - a
else:
    alpha = a
    beta = b
print('alpha:',alpha)
print('beta:',beta)
if alpha/beta <= math.exp(epsilon):
    p1 = 1
else:
    p1 = min(((1-alpha)-(1-beta)*math.exp(epsilon))/((1-(d+1)*alpha)-(1-(d+1)*beta)*math.exp(epsilon)),1)

print('p1:',p1)
q1 = (1-p1)/d
print('q1:',q1)

A = np.matrix([[p1-q1,math.exp(epsilon)*(q1-p1)],[1,d-1]])

B = np.matrix([[-q1+math.exp(epsilon)*q1],[1]])
A_inv = np.linalg.inv(A)
C = np.dot(A_inv,B)
p2 = C[0,0]
q2 = C[1,0]
if p2 >= 1:
    p2 = 1
if q2 <= 0:
    q2 = 0
print('p2:',p2)
print('q2:',q2)
print('p2*p1+(1-p2)*q1:',p2*p1+(1-p2)*q1)
print('q2*p1+(1-q2)*q1',q2*p1+(1-q2)*q1)
def First_Per(value):
    if value == 0:
        return 0
    possible_values = list(range(1,d+1))
    coin = random.random()
    if coin < p2 :
        return value
    else :
        possible_values.remove(value)
        return random.choice(possible_values)


def Second_Per(value):
    possible_values = list(range(d+1))
    coin = random.random()
    if coin < p1:
        return value
    else:
        possible_values.remove(value)
        return random.choice(possible_values)

x_max = d
x_min = 1
a = 2/(x_max-x_min)
b = 1-((2*x_max)/(x_max-x_min))
count = np.zeros(d+1).astype(int)
count_est = np.zeros(d+1).astype(int)
count_real = np.zeros(d+1).astype(int)
square_error = np.zeros(d+1)
ave_error = []
mean_error = []
null_error = []
for i in range(num):
    value = int(column.iloc[i])
    count_real[value] = count_real[value] + 1
mean_real = column.sum()/(num-count_real[0])
mean_real = a*mean_real +b
for i in range(100):
    print(i)
    mean = 0
    count = np.zeros(d+1).astype(int)
    count_est = np.zeros(d+1).astype(int)
    square_error = np.zeros(d+1)
    for j in range(num):
        value = int(column.iloc[j])
        value1 = First_Per(value)
        value2 = Second_Per(value1)
        count[value2] = count[value2]+1
    
    #estimate
    count_est[0] = round((count[0]-num*q1)/(p1-q1))
    #square_error[0] = (count_est[0]/num-count_real[0]/num)*(count_est[0]/num-count_real[0]/num)
    for j in range(1,d+1):
        count_est[j] = round((count[j]-count_est[0]*q1-(num-count_est[0])*(q2*p1+(1-q2)*q1))/((p2*p1+(1-p2)*q1)-(q2*p1+(1-q2)*q1)))
        #square_error[j] = (count_est[j]/num-count_real[j]/num)*(count_est[j]/num-count_real[j]/num)
    sum1 = sum(count_est)
    sum2 = sum1 - count_est[0]
    for j in range(d+1):
        mean = mean + j*(count_est[j]/sum2)
        square_error[j] = (count_est[j]/sum1-count_real[j]/num)*(count_est[j]/sum1-count_real[j]/num)
    mean = a*mean + b
    ave_error.append(np.mean(square_error))
    null_error.append(square_error[0])
    mean_error.append((mean-mean_real)*(mean-mean_real))
print("MSE:",sum(ave_error)/len(ave_error))
print('null_rate_MSE:',sum(null_error)/len(null_error))
print('mean_MSE:',sum(mean_error)/len(mean_error))
