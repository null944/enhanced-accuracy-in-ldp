import numpy as np
import pandas as pd
import random

dataset_name = 'GentH_1'
dataset = pd.read_csv(dataset_name+'.csv',header=None)
# Get first column
column = dataset.iloc[:,0]
users_num = len(column)
csv_file_path = dataset_name + '_miss_MNAR.csv'

csv_file_path1 = dataset_name + '_miss_MCAR.csv'
missing_rate = [0.4,0.35,0.1,0.05]#Change grouping and missing rate according to different datasets
missing_data = []#Store missing value positions

def generate_mnar_dataset():
    for i in range(users_num):
        index = int(np.floor((column.iloc[i] + 1)/0.5))#Determine the interval where data column.iloc[i] belongs
        rate = missing_rate[index]#Determine the missing rate of data in the interval

        coin = random.random()
        if coin < rate:
            missing_data.append([i,0])
    print('full_rate:',len(missing_data)/len(column))

    df = pd.DataFrame(missing_data)
    df.to_csv(csv_file_path,header=False,index=False)


generate_mnar_dataset()  

def generate_mcar_dataset(n, missing_percentage):
    # Generate vector v_0 of length n with first 20% positions as 0, rest as 1
    v_0 = np.ones(n)
    v_0[:int(n * missing_percentage)] = 0
    
    #Randomly select attributes with missing values
    #f_m=random.sample(n_feature, d//2)
    f_m=[0]
    l=len(f_m)
    for m in range(l):
        # Randomly shuffle positions of 0 and 1 in v_0 to get new 0-1 vector v_1
        v_1 = v_0.copy()
        np.random.shuffle(v_1)
        zero_indices = np.where(v_1 == 0)[0]#Indices where positions are 0
        data_to_append = pd.DataFrame(list(zip(zero_indices, [f_m[m]] * len(zero_indices))),columns=None)
        # Append data to CSV file
        data_to_append.to_csv(csv_file_path1, mode='a', header=False, index=False)
    df = pd.read_csv(csv_file_path, header=None)
        # Sort the dataframe
    df = df.sort_values(by=[1, 0])
        # Write sorted data back to CSV file
    df.to_csv(csv_file_path, index=False, header=False)
    print(f"CSV file sorted and saved to {csv_file_path}")
    return None
# Set sample count and attribute count
dataset = generate_mcar_dataset(users_num,len(missing_data)/len(column))