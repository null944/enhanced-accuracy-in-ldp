import time 
import random
import numpy as np

domain_miss = 2
domain_collec_list = [100,200,300,400,500,600,700,800,900,1000]
p1 = 0.490555041410482
p2 = 0.578939170852923
value = 2
FP_time = np.zeros(100)
SP_time = np.zeros(100)
total_time = np.zeros(100)
ave_time1 = []
ave_time2 = []
#first perterbution
def First_Per(value,domain,p1):
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
def Second_Per(value,domain,p2):
    possible_values = list(range(domain+1))
    coin = random.random()
    if coin < p2:
        return value
    else:
        possible_values.remove(value)
        return random.choice(possible_values)

for domain_collect in domain_collec_list:
    for j in range(100):
        start = time.perf_counter()
        value1 = First_Per(value,domain_collect,p1)#value after first pertubation
        middle = time.perf_counter()
        value2 = Second_Per(value1,domain_collect,p2)#value after second pertubation
        end = time.perf_counter()
        FP_time[j] = middle - start
        SP_time[j] = end - middle
        total_time[j] = FP_time[j] + SP_time[j]
    ave_time1.append(np.mean(SP_time))
    ave_time2.append(np.mean(total_time))

# ""a":使用追加模式
with open("./eval/results/time_cost_TSP_client.txt", "a") as f:
    f.write("\n" + "="*50 + "\n")  
    f.write("clock:" + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
    f.write("domain: " + str(domain_collec_list) + "\n")
    f.write("UP_pertubation_time= " + str(ave_time1) + "\n") 
    f.write("TSP_pertubation_time= " + str(ave_time2) + "\n") 