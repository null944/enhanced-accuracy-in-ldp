import random
import time
import numpy as np
domain_list = [100,200,300,400,500,600,700,800,900,1000]
q = 0.350492061555402
value = 1

#encode
def Encode(value,domain):
    array = np.zeros(domain)
    array[value-1] = 1
    return array

#perturb
def OUE(en_value,domain,q):
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

client_time = np.zeros(100)
time_list = []

for domain in domain_list:
    for i in range(100):
        start = time.perf_counter()
        en_value = Encode(value,domain)
        OUE(en_value,domain,q)
        end = time.perf_counter()
        client_time[i] = end - start
    time_list.append(np.mean(client_time))


with open("./eval/results/time_cost_AOUE_client.txt", "a") as f:
    f.write("\n" + "="*50 + "\n") 
    f.write("clock:" + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
    f.write("domain: " + str(domain_list) + "\n")
    f.write("pertubation_time= " + str(time_list) + "\n") 

