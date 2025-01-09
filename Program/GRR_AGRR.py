import math
import random
import pandas as pd
import numpy as np

epsilon = 1.5
d = 90
dataset = 'CDC_BMI'
Dataset = pd.read_csv(dataset+'.csv', header=None)
column = Dataset.iloc[:,0]
quasi_column = Dataset.iloc[:,1]
num = len(column)
count_0 = sum(quasi_column == 0)
count_1 = sum(quasi_column == 1)

index_list = []
for i in range(1,d+1):
    alpha_i = 0
    beta_i = 0
    count_i_0 = sum((column == i) & (quasi_column == 0))
    p_0 = count_i_0/count_0
    count_i_1 = sum((column == i) & (quasi_column == 1))
    p_1 = count_i_1/count_1
    if p_0 >= p_1 :
        alpha_i = p_0
        beta_i = p_1
    else:
        alpha_i = p_1
        beta_i = p_0
    index_list.append([alpha_i,beta_i])


alpha = index_list[0][0]
beta = index_list[0][1]
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

for i in range(1,d):
    alpha_i = index_list[i][0]
    beta_i = index_list[i][1]
    choice(alpha_i,beta_i)
print('alpha:',alpha)
print('beta:',beta)

p = min(((1-alpha)-(1-beta)*math.exp(epsilon))/((1-d*alpha)-(1-d*beta)*math.exp(epsilon)),1)
#p = math.exp(epsilon)/(math.exp(epsilon)-1+d)
print('p:',p)

def GRR(value):
    possible_values = list(range(1,d+1))
    coin = random.random()
    if coin < p :
        return value
    else :
        possible_values.remove(value)
        return random.choice(possible_values)




perturb_list = []
count = np.zeros(d).astype(int)
count_est = np.zeros(d).astype(int)
count_real = np.zeros(d).astype(int)
square_error = np.zeros(d)
ave_error = []
for i in range(num):
    value = int(column.iloc[i])
    count_real[value-1] = count_real[value-1]+1

q = (1-p)/(d-1)
for i in range(100):
    print(i)
    perturb_list = []
    square_error = np.zeros(d)
    count = np.zeros(d).astype(int)
    count_est = np.zeros(d).astype(int)
    for i in range(num) :
        value = column.iloc[i]
        value_updated = GRR(value)
        perturb_list.append(value_updated)
        count[int(value_updated)-1] = count[int(value_updated)-1] + 1
    for i in range(d) :
        count_est[i] = round((count[i]-num *q)/(p-q))
        square_error[i] = (count_est[i]/num-count_real[i]/num)*(count_est[i]/num-count_real[i]/num)
    ave_error.append(np.mean(square_error))
print("MSE:",sum(ave_error)/len(ave_error))
