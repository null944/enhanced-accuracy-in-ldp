import pandas as pd
import numpy as np
import math
import time


dataset='adult_salary'
Dataset = pd.read_csv(dataset+'.csv', header=None)
column_sensitive = Dataset.iloc[:,1].copy()#sensitive attribute S
column_direct = Dataset.iloc[:,0].copy()#corelated attribute A


domain_direct = 2
domain_sensitive = 2
epsilon = 0.1

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


def choose(alpha_k,beta_k,alpha,beta):
    if alpha_k >= alpha and beta_k <= beta:
        return [alpha_k,beta_k]
    if alpha_k <= alpha and beta_k >= beta:
        return [alpha,beta]
    if alpha_k > alpha and beta_k > beta:
        delta1 = alpha_k - alpha
        delta2 = beta_k - beta
        if delta1/delta2 >= math.exp(epsilon):
            return [alpha_k,beta_k]
        else:
            return [alpha,beta]
    if alpha_k < alpha and beta_k < beta:
        delta1 = alpha - alpha_k
        delta2 = beta - beta_k
        if delta1/delta2 <= math.exp(epsilon):
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
    column_i = conditional_probs[:, target_value-1]
    valid_values = column_i[~np.isnan(column_i)]
    max_prob = np.max(valid_values)
    min_prob = np.min(valid_values)
    return [max_prob,min_prob]

'''
step1
initialize the joint frequency table
row : sensitive attribute S
column : direct_corelated attribute A
'''
joint_counts = np.zeros((domain_sensitive, domain_direct), dtype=int)
#compute the joint frequency table N(S,A)
for d, i in zip(column_sensitive, column_direct):
    joint_counts[d-1, i-1] += 1
marginal_counts = joint_counts.sum(axis=1)#marginal frequency table of attribute S
conditional_probs = np.zeros((domain_sensitive, domain_direct), dtype=float)#Initialize the conditional probability distribution table P(A|S)
#compute the conditional probability distribution table P(A|S)
for d in range(domain_sensitive):
    total_count = marginal_counts[d]
    if total_count > 0:
        conditional_probs[d, :] = joint_counts[d, :] / marginal_counts[d]
    else:#total_count = 0 && joint_count = 0
        sensitive_category.remove(d+1)#the value d+1 is not recognized
        conditional_probs[d, :] = np.nan






'''
step2
For each value of attribute A,
compute the corresponding alpha_i and beta_i 
and store them in list1.
'''
list1 = np.zeros(100)
list2 = np.zeros(100)
for j in range(100):
    start = time.perf_counter()
    for direct_value in range(1 , domain_direct + 1):
        list = compute_max_min(direct_value)
        index_list.append(list)



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
    end = time.perf_counter()
    list1[j] = end - start
print(np.mean(list1))
for i in range(100):
    start = time.perf_counter()
    p = min(((1-alpha)-(1-beta)*math.exp(epsilon))/((1-d*alpha)-(1-d*beta)*math.exp(epsilon)),1)
    q = (1-p)/(domain_direct-1)
    end = time.perf_counter()
    list2[i] = end - start
print(np.mean(list2))


#q = 1/(1+math.exp(epsilon))