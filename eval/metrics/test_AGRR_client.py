import random
import time
import numpy as np
domain_list = [100,200,300,400,500,600,700,800,900,1000]
p = 0.350492061555402
value = 1

def GRR(value,p,domain):
    possible_values = list(range(1,domain+1))
    coin = random.random()
    if coin < p :
        return value
    else :
        possible_values.remove(value)
        return random.choice(possible_values)

client_time = np.zeros(100)
time_list = []

for domain in domain_list:
    for i in range(100):
        start = time.perf_counter()
        GRR(value,p,domain)
        end = time.perf_counter()
        client_time[i] = end - start
    time_list.append(np.mean(client_time))


with open("./eval/results/time_cost_AGRR_client.txt", "a") as f:
    f.write("\n" + "="*50 + "\n")  
    f.write("clock:" + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
    f.write("domain: " + str(domain_list) + "\n")
    f.write("pertubation_time= " + str(time_list) + "\n") 

