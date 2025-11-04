import math
import pandas as pd
import numpy as np
import random
import time
print("=" * 70)
print("                               TSP Protocol")
print("=" * 70)
print(" " * 70)
epsilon = 0.1
exp_eps = math.exp(epsilon)
dataset='GentH'
domain = 5#Target Collection Attribute Domain Size
mechanism = 'MNAR' 
Dataset = pd.read_csv('./data/processed/'+ dataset+'.csv', header=None)
num = len(Dataset)#the number of clients
column = Dataset.iloc[:,0].copy()
count_real_ori = np.zeros(domain).astype(int)#the real frequency table for target collection attribute without missing data
count_real = np.zeros(domain+1).astype(int)#the real frequency table for target collection attribute with missing data
count_miss = np.zeros(domain).astype(int)#Number of missing values for different attribute values
perturb_result = []#store all clients' data after TSP
index_list = []#Store all possible parameter pairs
print(f" Dataset: {dataset}")
print(f" Privacy Budget: {epsilon}")
print(f" Number of Users: {num:,}")
print(f" Collected ATTRIBUTE Domain Size: {domain}")
print(f" Missing Mechanism: {mechanism}")
print(" " * 70)

#compute the real frequency table for target collection attribute
for i in range(num):
    value = int(column.iloc[i])
    count_real_ori[value-1] = count_real_ori[value-1] + 1


#generate missing dataset based on miss_list
miss_list = np.loadtxt('./data/processed/'+ dataset+'_1_miss_'+mechanism+'.csv', delimiter=",", skiprows=0)               
for row in miss_list:
    i, j = int(row[0]), int(row[1])
    value = int(column.iloc[i])
    Dataset.iloc[i, j] = 0
    count_miss[value-1] = count_miss[value-1]+1

column = Dataset.iloc[:,0].copy()
#calculate the frequency table consisting of null
for i in range(num):
    value = int(column.iloc[i])
    count_real[value] = count_real[value] + 1

def choose(alpha_k,beta_k,alpha,beta):
    if alpha_k >= alpha and beta_k <= beta:
        return [alpha_k,beta_k]
    if alpha_k <= alpha and beta_k >= beta:
        return [alpha,beta]
    if alpha_k > alpha and beta_k > beta:
        delta1 = alpha_k - alpha
        delta2 = beta_k - beta
        if delta1/delta2 >= exp_eps:
            return [alpha_k,beta_k]
        else:
            return [alpha,beta]
    if alpha_k < alpha and beta_k < beta:
        delta1 = alpha - alpha_k
        delta2 = beta - beta_k
        if delta1/delta2 <= exp_eps:
            return [alpha_k,beta_k]
        else:
            return [alpha,beta]

'''
Calculate the maximum and minimum values of the conditional probability
for a given target attribute value
'''
def compute_max_min(target_value) : 
    max_prob = -math.inf
    min_prob = math.inf
    column_i = conditional_probs[:, target_value]
    valid_values = column_i[~np.isnan(column_i)]
    max_prob = np.max(valid_values)
    min_prob = np.min(valid_values)
    return [max_prob,min_prob]

missing_rate = np.zeros(domain)#store the missing rates of different values
for i in range(domain):
    if count_real_ori[i] != 0:
        missing_rate[i] = count_miss[i] / count_real_ori[i]
    else:
        missing_rate[i] = np.nan



'''
step1
determine the conditional frequency table
'''
print("============== Determine inherent uncertainty parameter ===============")

conditional_probs = np.zeros((domain, 2), dtype=float)#Initialize the conditional probability distribution table P(A|S)
#compute the conditional probability distribution table
for i in range(domain):
    if count_real_ori[i] == 0:
        conditional_probs[i, :] = np.nan#recognize i is not existing
    else:
        conditional_probs[i, 0] = missing_rate[i]
        conditional_probs[i, 1] = 1 - missing_rate[i]



##############Inherent uncertainty parameter selection by the collector##############

'''
step2
For each value of attribute A,
compute the corresponding alpha_i and beta_i 
and store them in list1.
'''
for direct_value in range(2):
    possible_list = compute_max_min(direct_value)
    index_list.append(possible_list)

'''
step3
Select the final uncertainty parameter pair from all parameter pairs.
    '''
alpha = -math.inf
beta = math.inf
for i in range (2):
    alpha_i = index_list[i][0]
    beta_i = index_list[i][1]
    result = choose(alpha_i,beta_i,alpha,beta)
    alpha = result[0]
    beta = result[1]

print("(alpha,beta):",(alpha,beta))
print(" " * 70)
print("================= Recalibrate perturbation parameter =================")





##############Perturbation parameter calculation by the collector##############
if alpha/beta <= exp_eps:
    p2 = 1
else:
    p2 = min(((1-alpha)-(1-beta)*exp_eps)/((1-(domain+1)*alpha)-(1-(domain+1)*beta)*exp_eps),1)
q2 = (1-p2)/domain
p1 = min((exp_eps*p2+((domain-2)*exp_eps-(domain-1))*q2)/((domain-1+exp_eps)*(p2-q2)),1)
q1 = max(0,(1-p1)/(domain-1))
    
print('p1:',p1)
print('q1:',q1)
print('p2:',p2)
print('q2:',q2)
print(" " * 70)
#print('p2*p1+(1-p2)*q1:',p2*p1+(1-p2)*q1)
#print('q2*p1+(1-q2)*q1',q2*p1+(1-q2)*q1)

#first perterbution
def First_Per(value):
    if value == 0:
        return 0
    possible_values = list(range(1,domain+1))
    coin = random.random()
    if coin < p1 :
        return value
    else :
        possible_values.remove(value)
        return random.choice(possible_values)

#second perturbation
def Second_Per(value):
    possible_values = list(range(domain+1))
    coin = random.random()
    if coin < p2:
        return value
    else:
        possible_values.remove(value)
        return random.choice(possible_values)

#aggregate
def aggregate(perturb_result,domain):
    count = np.zeros(domain+1).astype(int)
    for value_updated in perturb_result:
        count[int(value_updated)] = count[int(value_updated)] + 1
    return count

#estimate
def estimate(count,num,p1,p2,q1,q2,domain):
    '''
    p1,p2,q1,q2: perturb parameters
    count: the frequency table of perturbed data
    num: the number of pertured data
    domain: the estimated attribute domain size
    '''
    count_est = np.zeros(domain + 1)#initialize the estimated frequency table
    count_est[0] = round((count[0]-num*q2)/(p2-q2))
    for j in range(1,domain+1):
        count_est[j] = round((count[j]-count_est[0]*q2-(num-count_est[0])*(q1*p2+(1-q1)*q2))/((p1*p2+(1-p1)*q2)-(q1*p2+(1-q1)*q2)))
    return count_est

#calculate the squared error of frequency estimates for different values 
def error(count_real,count_est,num,domain):
    '''
    count_real: the real frequency table for attribute A
    count_est: the estimated frequency table for attribute A
    num: the number of pertured data
    domain: the estimated attribute domain size
    '''
    square_error = np.zeros(domain + 1)
    sum_value = sum(count_est)
    for j in range(domain + 1):
        #mean = mean + j*(count_est[j]/sum2)
        square_error[j] = (count_est[j]/sum_value-count_real[j]/num)*(count_est[j]/sum_value-count_real[j]/num)
    return square_error


#x_max = domain
#x_min = 1
#a = 2/(x_max-x_min)
#b = 1-((2*x_max)/(x_max-x_min))
count_time4 = np.zeros(100)
ave_error = []
#mean_error = []
#null_error = []

#mean_real = column.sum()/(num-count_real[0])
#mean_real = a*mean_real +b

print("=========================== Client Perturb ===========================")
print("Repeat 100 times")
#############################Client Perturb#######################
for i in range(100):#repeat 100 times
    print(i)
    perturb_result.clear()
    #mean = 0
    square_error = np.zeros(domain+1)
    for j in range(num):#stimulate num clients perturb data
        value = int(column.iloc[j])#original data
        value1 = First_Per(value)#value after first pertubation
        value2 = Second_Per(value1)#value after second pertubation
        perturb_result.append(value2)#stimulate client uploads perturbed data
    count = aggregate(perturb_result,domain)#server aggregate
    count_est = estimate(count,num,p1,p2,q1,q2,domain)#server estimate frequency
    square_error = error(count_real,count_est,num,domain)#compute square error
    #mean = a*mean + b
    ave_error.append(np.mean(square_error))
    #null_error.append(square_error[0])
    #mean_error.append((mean-mean_real)*(mean-mean_real))
print("MSE:",sum(ave_error)/len(ave_error))
#print('null_rate_MSE:',sum(null_error)/len(null_error))
#print('mean_MSE:',sum(mean_error)/len(mean_error))