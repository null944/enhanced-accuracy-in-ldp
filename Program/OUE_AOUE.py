import math
import random
import pandas as pd
import numpy as np

epsilon = 1.5
d = 90
quasi_d = 2
category = []
for i in range (quasi_d) : 
    category.append(i)
dataset = 'CDC_BMI'
Dataset = pd.read_csv(dataset+'.csv', header=None)
column = Dataset.iloc[:,0]
quasi_column = Dataset.iloc[:,1]
num = len(column)
index_list = []

#q = 1/(1+math.exp(epsilon))

for i in range (quasi_d) :
    s_i = category[i]
    count_i = sum(quasi_column == s_i)
    for j in range (quasi_d) :
        if j == i :
            continue
        alpha_i = 0
        beta_i = 0
        s_j = category[j]
        count_j = sum(quasi_column == s_j)
        for k in range (1,d+1) :
            count_ki = sum((column == k) & (quasi_column == s_i))
            count_kj = sum((column == k) & (quasi_column == s_j))
            p_i = count_ki / count_i
            p_j = count_kj / count_j
            if (p_j == 0) or (p_i / p_j >= math.exp(epsilon)):
                alpha_i = alpha_i + p_i
                beta_i = beta_i + p_j
        
        index_list.append([alpha_i,beta_i])

alpha = index_list[0][0]
beta = index_list[0][1]
print(index_list)
def choice(alpha_i,beta_i):
    global alpha,beta
    if alpha >= alpha_i and  beta <= beta_i:
        None
    elif alpha <= alpha_i and beta >= beta_i:
        alpha = alpha_i
        beta = beta_i
    elif alpha > alpha_i and beta > beta_i:
        deta_1 = alpha - alpha_i
        deta_2 = beta - beta_i

        if deta_1/deta_2 >= math.exp(epsilon):
            None
        else:
            alpha = alpha_i
            beta = beta_i
    elif alpha < alpha_i and beta < beta_i:
        deta_1 = alpha_i - alpha
        deta_2 = beta_i - beta
        if deta_1/deta_2 <= math.exp(epsilon):
            None
        else:
            alpha = alpha_i
            beta = beta_i

for i in range(1,len(index_list)):
    alpha_i = index_list[i][0]
    beta_i = index_list[i][1]
    choice(alpha_i,beta_i)
print('alpha:',alpha)
print('beta:',beta)
p = 1/2
print('p:',p)
q = (alpha - beta*math.exp(epsilon)) / ((math.exp(epsilon)-1)+2*(alpha - beta*math.exp(epsilon)))
print('q:',q)
def Encode(value):
    array = np.zeros(d)
    array[value-1] = 1
    return array

def OUE(value):
   en_value = Encode(value)
   for i in range(d):#perturb bit by bit
       if (en_value[i]==1):
           coin = random.random()
           if coin >= 1/2:
               en_value[i] = 0
       else:
           coin = random.random()
           if coin < q:
               en_value[i] = 1
   return en_value

count = np.zeros(d).astype(int)#count[i] is the number of value_updated whose value_updated[i]==1  
count_est = np.zeros(d).astype(int)
count_real = np.zeros(d).astype(int)
square_error = np.zeros(d)
ave_error = []
for i in range(num):
    value = int(column.iloc[i])
    count_real[value-1] = count_real[value-1]+1
for j in range(100):
    count = np.zeros(d)
    for i in range(num):#perturb value by value
        value = column.iloc[i]
        value_updated = OUE(value)
        index_ones = np.where(value_updated==1)[0]
        for index in index_ones:
            count[index] = count[index]+1
    print(j)
    for i in range(d):
        count_est[i] = round((count[i]-num*q)/(p-q))
        square_error[i] = (count_est[i]/num-count_real[i]/num)*(count_est[i]/num-count_real[i]/num)
    ave_error.append(np.mean(square_error))

print('MSE:',sum(ave_error)/len(ave_error))
