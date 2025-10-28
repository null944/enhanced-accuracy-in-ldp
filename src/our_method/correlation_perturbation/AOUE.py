import math
import random
import pandas as pd
import numpy as np

epsilon = 1.5

dataset = 'adult_age'
Dataset = pd.read_csv('./data/processed/'+ dataset+'.csv', header=None)
d = domain_direct = 100#domain of attribute A
domain_sensitive = 2#domain of attribute S
catagory = []#store all possible values of sensitive attributes
column_sensitive = Dataset.iloc[:,1]
column_direct = Dataset.iloc[:,0]
num = len(column_direct)
index_list = []#Store all possible parameter pairs
perturb_result = []#Store the perturbed upload results for all users
count_real = np.zeros(d).astype(int)#the real frequency table for attribute A


for a in range(domain_sensitive):
    catagory.append(a + 1)

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

##############Inherent uncertainty parameter selection by the collector##############
'''
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
        catagory.remove(d+1)#this value of S is recognized not exist
        conditional_probs[d, :] = np.nan



#Compute all possible parameter pairs
cpt_array = np.array(conditional_probs)
s_indices = np.arange(domain_sensitive)
s_i_indices, s_j_indices = [], []#store all possible (s_i,s_j)pairs
#compute all possible (s_i,s_j)pairs
for s_i in range(1,domain_sensitive+1):
    if s_i in catagory:
        for s_j in range(1,domain_sensitive+1):
            if s_j in catagory:
                if s_j != s_i:
                    s_i_indices.append(s_i-1)
                    s_j_indices.append(s_j-1)
s_i_indices = np.array(s_i_indices)
s_j_indices = np.array(s_j_indices)
#extract the corresponding row in cpt
p_i_matrix = cpt_array[s_i_indices]  # shape: (len(s_i_indice), domain_collected)
p_j_matrix = cpt_array[s_j_indices]  # shape: (len(s_j_indice), domain_collected)
#Parallel computation of all ratios corresponding to pairs (s_i, s_j)
with np.errstate(divide='ignore', invalid='ignore'):
    ratios = np.divide(p_i_matrix, p_j_matrix)
    ratios[p_j_matrix == 0] = np.inf#denominator is zero, treat it as infinity
exp_epsilon = math.exp(epsilon)
condition1 = np.isinf(ratios)  # p_j == 0
condition2 = ratios >= exp_epsilon  # p_i/p_j >= exp(epsilon)
valid_mask = condition1 | condition2
alpha_i_values = np.sum(p_i_matrix * valid_mask, axis=1)#store all alternative alpha_i
beta_i_values = np.sum(p_j_matrix * condition2, axis=1)##store all alternative beta_i
index_list = [[alpha, beta] for alpha, beta in zip(alpha_i_values, beta_i_values)]


#choose the finale final parameter pair(alpha,beta)
alpha = -math.inf
beta = math.inf
for list in index_list:
    alpha_k = list[0]
    beta_k = list[1]
    result = choose(alpha_k,beta_k,alpha,beta)
    alpha = result[0]
    beta = result[1]
print("alpha:",alpha)
print("beta:",beta)


##############Perturbation parameter calculation by the collector##############
#compute perturb parameters
p = 1/2
q = (alpha - beta*math.exp(epsilon)) / ((math.exp(epsilon)-1)+2*(alpha - beta*math.exp(epsilon)))
#q = 1/(1+math.exp(epsilon))
#print('p:',p)
#print('q:',q)



#encode
def Encode(value,domain):
    array = np.zeros(domain)
    array[value-1] = 1
    return array


#perturb
def OUE(en_value,domain):
   for i in range(domain):#perturb bit by bit
       if (en_value[i]==1):
           coin = random.random()
           if coin >= 1/2:
               en_value[i] = 0
       else:
           coin = random.random()
           if coin < q:
               en_value[i] = 1
   return en_value

#aggregate
def aggregate(perturb_result,domain):
    count = np.zeros(domain).astype(int)
    for value_updated in perturb_result:
        index_ones = np.where(value_updated==1)[0]
        for index in index_ones:
            count[index] = count[index] + 1
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
        count_est[i] = round((count[i]-num*q)/(p-q))
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

ave_error = []#store the MSE

#compute the real frequency table for attribute A
for i in range(num):
    value = int(column_direct.iloc[i])
    count_real[value-1] = count_real[value-1] + 1

#############################Client Perturb#######################
for j in range(100):#repeat 10 times
    perturb_result.clear()
    for i in range(num):#Simulate num clients
        value = column_direct.iloc[i]#value of a client
        en_value = Encode(value,domain_direct)#encode
        value_updated = OUE(en_value,domain_direct)#perturbrt
        perturb_result.append(value_updated)#Simulate upload to the server
    print(j)
    count = aggregate(perturb_result,domain_direct)# server aggregate and statistic
    count_est = estimate(count,num,p,q,domain_direct)#estimate
    square_error = error(count_real,count_est,num,domain_direct)#compute the MSE
    ave_error.append(np.mean(square_error))

print('MSE:',sum(ave_error)/len(ave_error))