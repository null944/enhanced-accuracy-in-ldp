import pandas as pd
import numpy as np
import math
import time

epsilon = 0.1#privacy budget

domain_direct = 90#domain of attribute A
domain_sensitive = 2#domain of attribute S

dataset = 'CDC_BMI'
Dataset = pd.read_csv(dataset+'.csv', header=None)
column_sensitive = Dataset.iloc[:,1]
column_direct = Dataset.iloc[:,0]
index_list = []#Store all possible parameter pairs


#choose according rules
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
initialize the joint frequency table
row : sensitive attribute S
column : direct_corelated attribute A
'''
joint_counts = np.zeros((domain_sensitive, domain_direct), dtype=int)
#compute the joint frequency table N(S,A)
for d, i in zip(column_sensitive, column_direct):
    joint_counts[int(d-1), i-1] += 1
marginal_counts = joint_counts.sum(axis=1)#marginal frequency table of attribute S
conditional_probs = np.zeros((domain_sensitive, domain_direct), dtype=float)#Initialize the conditional probability distribution table P(A|S)
#compute the conditional probability distribution table P(A|S)
for d in range(domain_sensitive):
    total_count = marginal_counts[d]
    if total_count > 0:
        conditional_probs[d, :] = joint_counts[d, :] / marginal_counts[d]
    else:#total_count = 0 && joint_count = 0
        conditional_probs[d, :] = 0 


list1 = np.zeros(100)
list2 = np.zeros(100)
for i in range(100):
    start =time.perf_counter()
#Compute all possible parameter pairs
    for s_i in range (1,domain_sensitive+1):
        for s_j in range (1,domain_sensitive+1) :
            if s_j != s_i:
                alpha_i = 0
                beta_i = 0
                for k in range (domain_direct) :
                    p_i = conditional_probs[s_i-1][k]#P(A=k+1|S=s_i)
                    p_j = conditional_probs[s_j-1][k]#P(A=k+1|S=s_j)
                    if p_j == 0:#p_i/p_j is regarded as infinity
                        alpha_i = alpha_i + p_i
                    elif p_i/p_j >= math.exp(epsilon):
                        alpha_i = alpha_i + p_i
                        beta_i = beta_i + p_j
        
                index_list.append([alpha_i,beta_i])


#choose the finale final parameter pair(alpha,beta)
    alpha = -math.inf
    beta = math.inf
    for list in index_list:
        alpha_k = list[0]
        beta_k = list[1]
        result = choose(alpha_k,beta_k,alpha,beta)
        alpha = result[0]
        beta = result[1]
    end = time.perf_counter()
    list1[i] = end - start
print(np.mean(list1))
for i in range(100):
    start = time.perf_counter()
    p = 1/2
    q = (alpha - beta*math.exp(epsilon)) / ((math.exp(epsilon)-1)+2*(alpha - beta*math.exp(epsilon)))
    end = time.perf_counter()
    list2[i] = end - start
print(np.mean(list2))
