import math
import random
import pandas as pd
import numpy as np
import time


print("=" * 70)
print("                               ARR Protocol")
print("=" * 70)
print(" " * 70)
d = 2
dataset = 'CDC_COST'
Dataset = pd.read_csv('./data/processed/'+ dataset+'.csv', header=None)
column_sensitive = Dataset.iloc[:,1].copy()#sensitive attribute S
column_direct = Dataset.iloc[:,0].copy()#corelated attribute A
num = len(column_direct)
perturb_result = []#Store the perturbed upload results for all users
count_real = np.zeros(d).astype(int)#the real frequency table for attribute A
ave_time = []
domain_direct = 2
domain_sensitive = 2
epsilon = 0.1
exp_eps = math.exp(epsilon)
print(f" Dataset: {dataset}")
print(f" Privacy Budget: {epsilon}")
print(f" Number of Users: {num:,}")
print(f" Attribute A Domain Size: {domain_direct}")
print(f" Sensitive Attribute S Domain Size: {domain_sensitive}")
print(" " * 70)
sensitive_category = []#store all values of sensitive attribute S
for i in range(domain_sensitive):
    sensitive_category.append(i+1)


'''
index_list[i][0] : alpha
index_list[i][0] : beta
'''
index_list = []#Store all possible parameter pairs
max_prob = -math.inf
min_prob = math.inf

#aggregate
def aggregate(perturb_result,domain):
    count = np.zeros(domain).astype(int)
    for value_updated in perturb_result:
        count[int(value_updated)-1] = count[int(value_updated)-1] + 1
    return count

#estimate
def estimate(count,num,p,q,domain):
    '''
    p,q: perturb parameters
    count: the frequency table of perturbed data
    num: the number of pertured data
    domain: the estimated attribute domain size
    '''
    count_est = np.zeros(domain)#initialize the estimated frequency table
    #estimate the frequency of each value in turn.
    for i in range(domain):
        count_est[i] = round((count[i]-num *q)/(p-q))
    return count_est

def error(count_real,count_est,num,domain):
    '''
    count_real: the real frequency table for attribute A
    count_est: the estimated frequency table for attribute A
    num: the number of pertured data
    domain: the estimated attribute domain size
    '''
    square_error = np.zeros(domain)
    for i in range(domain):
        square_error[i] = (count_est[i]/num-count_real[i]/num)*(count_est[i]/num-count_real[i]/num)
    return square_error

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
step1
initialize the joint frequency table
row : sensitive attribute S
column : direct_corelated attribute A
'''
print("============== Determine inherent uncertainty parameter ===============")

joint_counts = np.zeros((domain_sensitive, domain_direct), dtype=int)
#compute the joint frequency table N(S,A)
for x, y in zip(column_sensitive, column_direct):
    joint_counts[x, y] += 1
marginal_counts = joint_counts.sum(axis=1)#marginal frequency table of attribute S
conditional_probs = np.zeros((domain_sensitive, domain_direct), dtype=float)#Initialize the conditional probability distribution table P(A|S)
#compute the conditional probability distribution table P(A|S)
for k in range(domain_sensitive):
    total_count = marginal_counts[k]
    if total_count > 0:
        conditional_probs[k, :] = joint_counts[k, :] / marginal_counts[k]
    else:#total_count = 0 && joint_count = 0
        sensitive_category.remove(k+1)#the value d+1 is not recognized
        conditional_probs[k, :] = np.nan


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

##############Inherent uncertainty parameter selection by the collector##############
'''
step2
For each value of attribute A,
compute the corresponding alpha_i and beta_i 
and store them in list1.
'''
max_values = np.nanmax(conditional_probs, axis=0)
min_values = np.nanmin(conditional_probs, axis=0)
index_list = list(zip(max_values, min_values))
'''
step3
Select the final uncertainty parameter pair from all parameter pairs.
'''
alpha = -math.inf
beta = math.inf
for i in range (domain_direct):
    alpha_i = index_list[i][0]
    beta_i = index_list[i][1]
    result = choose(alpha_i,beta_i,alpha,beta)
    alpha = result[0]
    beta = result[1]
print("(alpha,beta):",(alpha,beta))
print(" " * 70)
print("================= Recalibrate perturbation parameter =================")



##############Perturbation parameter calculation by the collector##############
#p = math.exp(epsilon)/(math.exp(epsilon)-1+d)
p = min(((1-alpha)-(1-beta)*exp_eps)/((1-d*alpha)-(1-d*beta)*exp_eps),1)
q = 1-p
print('p',p)
print('q',q)
print(" " * 70)


def ARR(value):
    coin = random.random()
    if coin < p :
        return int(value)
    else :
        
        return int(1-value)




ave_error = []
for i in range(num):
    value = int(column_direct.iloc[i])
    count_real[value] = count_real[value]+1


#############################Client Perturb#######################
print("=========================== Client Perturb ===========================")
print("Repeat 100 times")
for i in range(100):
    print(i)
    perturb_result.clear()
    for i in range(num) :
        value = column_direct.iloc[i]#value of a client
        value_updated = ARR(value)
        perturb_result.append(value_updated)#Simulate upload to the server
    count = aggregate(perturb_result,domain_direct)#server aggregate and statistic 
    count_est = estimate(count,num,p,q,domain_direct)#estimate
    square_error = error(count_real,count_est,num,domain_direct)#compute the MSE
    ave_error.append(np.mean(square_error))

print("MSE:",sum(ave_error)/len(ave_error))

