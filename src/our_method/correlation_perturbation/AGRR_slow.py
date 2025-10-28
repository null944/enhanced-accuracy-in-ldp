import math
import random
import pandas as pd
import numpy as np
import time


dataset = 'adult_age'
Dataset = pd.read_csv('./data/processed/'+dataset+'.csv', header=None)
column_direct = Dataset.iloc[:,0]#corelated attribute A
column_sensitive = Dataset.iloc[:,1]#sensitive attribute S
num = len(column_direct)
d = domain_direct = 100
domain_sensitive = 2
epsilon = 1.5
perturb_result = []#Store the perturbed upload results for all users
count_real = np.zeros(d).astype(int)#the real frequency table for attribute A
ave_time = []


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

##############Inherent uncertainty parameter selection by the collector##############

'''
step1
initialize the joint frequency table
row : sensitive attribute S
column : direct_corelated attribute A
'''
joint_counts = np.zeros((domain_sensitive, domain_direct), dtype=int)
#compute the joint frequency table N(S,A)
for x, y in zip(column_sensitive, column_direct):
    joint_counts[x-1, y-1] += 1
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
step2
For each value of attribute A,
compute the corresponding alpha_i and beta_i 
and store them in list1.
'''
server_time1 = np.zeros(100)
server_time2 = np.zeros(100)
server_time3 = np.zeros(100)
for i in range(100):
    start = time.perf_counter()
    for direct_value in range(1 , domain_direct + 1):
        possible_pairs = compute_max_min(direct_value)
        index_list.append(possible_pairs)

    

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
    print("alpha:",alpha)
    print("beta:",beta)
    middle = time.perf_counter()
##############Perturbation parameter calculation by the collector##############
    p = min(((1-alpha)-(1-beta)*math.exp(epsilon))/((1-d*alpha)-(1-d*beta)*math.exp(epsilon)),1)
    q = (1-p)/(domain_direct-1)
#p = math.exp(epsilon)/(math.exp(epsilon)-1+d)
#print('p:',p)
    end = time.perf_counter()
    server_time1[i] = middle - start
    server_time2[i] = end - middle
    server_time3[i] = end - start

print("server_time1:",np.mean(server_time1))
print("server_time2:",np.mean(server_time2))
print("server_time3:",np.mean(server_time3))


def GRR(value):
    possible_values = list(range(1,domain_direct+1))
    coin = random.random()
    if coin < p :
        return value
    else :
        possible_values.remove(value)
        return random.choice(possible_values)

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


ave_error = []
for i in range(num):
    value = int(column_direct.iloc[i])
    count_real[value-1] = count_real[value-1] + 1

client_time = np.zeros(num)#storge client perturb time

#############################Client Perturb#######################

for i in range(100):
    print(i)
    perturb_result.clear()
    for i in range(num) :
        value = column_direct.iloc[i]#value of a client
        start = time.perf_counter()
        value_updated = GRR(value)#perturb
        end = time.perf_counter()
        client_time[i] = end - start
        perturb_result.append(value_updated)#Simulate upload to the server
    ave_time.append(np.mean(client_time))
    count = aggregate(perturb_result,domain_direct)#server aggregate and statistic 
    count_est = estimate(count,num,p,q,domain_direct)#estimate
    square_error = error(count_real,count_est,num,domain_direct)#compute the MSE
    ave_error.append(np.mean(square_error))
print("MSE:",sum(ave_error)/len(ave_error))
print('TIME:',sum(ave_time)/len(ave_time))