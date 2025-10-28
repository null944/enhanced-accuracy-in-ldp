import numpy as np
import math
import time



domain_collec_list = [100,200,300,400,500,600,700,800,900,1000]
epsilon = 0.1
exp_eps = math.exp(epsilon)
index_list = []#Store all possible parameter pairs
server_time1 = np.zeros(100)
server_time2 = np.zeros(100)
server_time3 = np.zeros(100)
ave_time1 = []
ave_time2 = []
ave_time3 = []
space_cost_list = []

def generate_random_cpt(domain_sensitive, domain_collected):
    """
    Completely Randomly Generated Conditional Probability Distribution Table.
    Each element is independently and randomly generated, then normalized.
    """
    conditional_prob = np.zeros((domain_sensitive, domain_collected))
    
    for i in range(domain_sensitive):
        random_numbers = np.random.rand(domain_collected)
        conditional_prob[i] = random_numbers / np.sum(random_numbers)

    return conditional_prob

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

def compute_max_min(conditional_probs,target_value) : 
    max_prob = -math.inf
    min_prob = math.inf
    column_i = conditional_probs[:, target_value-1]
    max_prob = np.max(column_i)
    min_prob = np.min(column_i)
    return [max_prob,min_prob]

domain_miss = 2#missing status
for domain_collect in domain_collec_list:
    space_cost = ((domain_collect*domain_miss + domain_miss*2)*8)/(1024*1024)
    space_cost_list.append(space_cost)
    cpt = generate_random_cpt(domain_collect, domain_miss)
    for a in range(100):
        start = time.perf_counter()
        '''Step1: generate conditional prob table'''
        #Check whether the sum of each row is 1
        #for i in range(domain_sensitive):
        #    print(np.sum(cpt[i]))
        #all_in_range = np.all((cpt >= 0) & (cpt <= 1))#Check whether all elements belong to the range [0,1]
        #print(all_in_range)

        '''Step2:Calculate multiple sets of alternative uncertainty parameter pairs'''
        #for direct_value in range(1 , domain_collected + 1):
        #    possible_pairs = compute_max_min(cpt,direct_value)
        #    index_list.append(possible_pairs)
        max_values = np.max(cpt, axis=0)
        min_values = np.min(cpt, axis=0)
        index_list = list(zip(max_values, min_values))
    
    
        #for direct_value in range(1 , domain_collected + 1):
        #        possible_pairs = compute_max_min(cpt,direct_value)
        #        index_list.append(possible_pairs)
        #verify
        #print(index_list1==index_list)

        '''Step3: Select the final uncertainty parameter pair from all parameter pairs.'''
        alpha = -math.inf
        beta = math.inf
        for i in range (domain_miss):
            alpha_i = index_list[i][0]
            beta_i = index_list[i][1]
            result = choose(alpha_i,beta_i,alpha,beta)
            alpha = result[0]
            beta = result[1]
        #print("alpha:",alpha)
        #print("beta:",beta)
        middle = time.perf_counter()
        ##############Perturbation parameter calculation by the collector##############
    
        if alpha/beta <= math.exp(epsilon):
            p2 = 1
        else:
            p2 = min(((1-alpha)-(1-beta)*exp_eps)/((1-(domain_collect+1)*alpha)-(1-(domain_collect+1)*beta)*exp_eps),1)
        q2 = (1-p2)/domain_collect
    
        p1 = min((exp_eps*p2+((domain_collect-2)*exp_eps-(domain_collect-1))*q2)/((domain_collect-1+exp_eps)*(p2-q2)),1)
        q1 = max(0,(1-p1)/(domain_collect-1))


        end = time.perf_counter()
        server_time1[a] = middle - start
        server_time2[a] = end - middle
        server_time3[a] = server_time1[a] + server_time2[a]
    ave_time1.append(np.mean(server_time1))
    ave_time2.append(np.mean(server_time2))
    ave_time3.append(np.mean(server_time3))

# "a": use append mode
with open("./eval/results/time_cost_TSP_server.txt", "a") as f:
    f.write("\n" + "="*50 + "\n")  # Add separator line
    f.write("clock:" + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
    f.write("domain_miss fixed: " + str(domain_miss) + "\n")
    f.write("domain_collect: " + str(domain_collec_list) + "\n")
    f.write("uncertainty_time= " + str(ave_time1) + "\n")
    f.write("pertubation_time= " + str(ave_time2) + "\n") 
    f.write("total_time= " + str(ave_time3) + "\n")
    f.write("space_cost: " + str(space_cost_list) + "\n")