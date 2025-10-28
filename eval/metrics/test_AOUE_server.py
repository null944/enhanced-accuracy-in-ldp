import numpy as np
import math
import time



domain_sens_list = [100,200,300,400,500,600,700,800,900,1000]
domain_collec_list = [100,200,300,400,500,600,700,800,900,1000]#column number
epsilon = 0.1
exp_epsilon = math.exp(epsilon)
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

#choose according rules
def choose(alpha_k,beta_k,alpha,beta):
    if alpha_k >= alpha and beta_k <= beta:
        return [alpha_k,beta_k]
    if alpha_k <= alpha and beta_k >= beta:
        return [alpha,beta]
    if alpha_k > alpha and beta_k > beta:
        delta1 = alpha_k - alpha
        delta2 = beta_k - beta
        if delta1/delta2 >= exp_epsilon:
            return [alpha_k,beta_k]
        else:
            return [alpha,beta]
    if alpha_k < alpha and beta_k < beta:
        delta1 = alpha - alpha_k
        delta2 = beta - beta_k
        if delta1/delta2 <= exp_epsilon:
            return [alpha_k,beta_k]
        else:
            return [alpha,beta]

domain_collected = domain_collec_list[1]
#domain_sensitive = domain_sens_list[1]
for domain_sensitive in domain_collec_list:
    space_cost = ((domain_sensitive*domain_collected + domain_sensitive*(domain_sensitive-1)*2)*8)/(1024*1024)
    space_cost_list.append(space_cost)
    '''Step1: generate conditional prob table'''
    cpt = generate_random_cpt(domain_sensitive, domain_collected)
    for a in range(100):
        start = time.perf_counter()
        #Check whether the sum of each row is 1
        #for i in range(domain_sensitive):
        #    print(np.sum(cpt[i]))
        #all_in_range = np.all((cpt >= 0) & (cpt <= 1))#Check whether all elements belong to the range [0,1]
        #print(all_in_range)

        '''Step2:Calculate multiple sets of alternative uncertainty parameter pairs'''
        cpt_array = np.array(cpt)
        s_i_indices, s_j_indices = [], []#store all possible (s_i,s_j)pairs
        #compute all possible (s_i,s_j)pairs
        for s_i in range(domain_sensitive):
            for s_j in range(domain_sensitive):
                if s_j != s_i:
                    s_i_indices.append(s_i)
                    s_j_indices.append(s_j)
        s_i_indices = np.array(s_i_indices)
        s_j_indices = np.array(s_j_indices)
        #extract the corresponding row in cpt
        p_i_matrix = cpt_array[s_i_indices]  # shape: (len(s_i_indice), domain_collected)
        p_j_matrix = cpt_array[s_j_indices]  # shape: (len(s_j_indice), domain_collected)
        #Parallel computation of all ratios corresponding to pairs (s_i, s_j)
        with np.errstate(divide='ignore', invalid='ignore'):
            ratios = np.divide(p_i_matrix, p_j_matrix)
            ratios[p_j_matrix == 0] = np.inf#denominator is zero, treat it as infinity
        condition1 = np.isinf(ratios)  # p_j == 0
        condition2 = ratios >= exp_epsilon  # p_i/p_j >= exp(epsilon)
        valid_mask = condition1 | condition2
        alpha_i_values = np.sum(p_i_matrix * valid_mask, axis=1)#store all alternative alpha_i
        beta_i_values = np.sum(p_j_matrix * condition2, axis=1)##store all alternative beta_i
        index_list = [[alpha, beta] for alpha, beta in zip(alpha_i_values, beta_i_values)]
        '''Step3: Select the final uncertainty parameter pair from all parameter pairs.'''
        alpha = -math.inf
        beta = math.inf
        for list in index_list:
            alpha_k = list[0]
            beta_k = list[1]
            result = choose(alpha_k,beta_k,alpha,beta)
            alpha = result[0]
            beta = result[1]
        #print("alpha:",alpha)
        #print("beta:",beta)
        middle = time.perf_counter()
        ##############Perturbation parameter calculation by the collector##############
        p = 1/2
        q = (alpha - beta*exp_epsilon) / ((exp_epsilon-1)+2*(alpha - beta*exp_epsilon))
        end = time.perf_counter()
        server_time1[a] = middle - start
        server_time2[a] = end - middle
        server_time3[a] = server_time1[a] + server_time2[a]
    ave_time1.append(np.mean(server_time1))
    ave_time2.append(np.mean(server_time2))
    ave_time3.append(np.mean(server_time3))


with open("./eval/results/time_cost_AOUE_server.txt", "a") as f:
    f.write("\n" + "="*50 + "\n")  
    f.write("clock:" + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
    f.write("domain_collected fixed: " + str(domain_collected) + "\n")
    f.write("domain_sensitive: " + str(domain_sens_list) + "\n")
    #f.write("domain_sensitive fixed: " + str(domain_sensitive) + "\n")
    #f.write("domain_collected: " + str(domain_collec_list) + "\n")
    f.write("uncertainty_time= " + str(ave_time1) + "\n")
    f.write("pertubation_time= " + str(ave_time2) + "\n") 
    f.write("total_time=" + str(ave_time3) + "\n")
    f.write("space_cost= " + str(space_cost_list) + "\n")