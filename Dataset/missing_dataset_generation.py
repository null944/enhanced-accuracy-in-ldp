import numpy as np
import pandas as pd
import random
from scipy.stats import pearsonr

dataset_name = 'GentH_1'
dataset = pd.read_csv(dataset_name + '.csv', header=None)
# Obtain the first column of the dataset
column = dataset.iloc[:, 0]
users_num = len(column)

csv_file_path = dataset_name + '_miss_MNAR.csv'
csv_file_path1 = dataset_name + '_miss_MCAR.csv'

missing_rate = [0.4, 0.35, 0.2, 0.1, 0.05]  # Change group numbers and missing rates based on the dataset
missing_data = []  # Store the positions of missing values


def generate_mnar_dataset():
    """
    Generate a dataset with MNAR mechanism where the probability of a value being missing depends on its own value.
    """
    global missing_data
    for i in range(users_num):
        # Determine the index of the missing rate list based on the value in the column
        index = int(np.floor((column.iloc[i] + 1) / 0.5))
        if index >= len(missing_rate):  # Handle edge case when value is greater than expected
            index = len(missing_rate) - 1
        rate = missing_rate[index]

        coin = random.random()
        if coin < rate:
            missing_data.append([i, 0])
    
    print('full_rate:', len(missing_data) / len(column))

    df = pd.DataFrame(missing_data)
    df.to_csv(csv_file_path, header=False, index=False)


generate_mnar_dataset()


def generate_mcar_dataset(n, missing_percentage):
    """
    Generate a dataset with MCAR mechanism where the probability of a value being missing does not depend on any value.
    """
    v_0 = np.ones(n)
    v_0[:int(n * missing_percentage)] = 0  # Assign missing status
    
    f_m = [0]  # Features that will have missing data; here only the first column is considered
    l = len(f_m)
    
    for m in range(l):
        v_1 = v_0.copy()
        np.random.shuffle(v_1)  # Shuffle to simulate randomness in missingness
        zero_indices = np.where(v_1 == 0)[0]  # Indices of elements that are missing
        
        data_to_append = pd.DataFrame(list(zip(zero_indices, [f_m[m]] * len(zero_indices))), columns=None)
        
        # Append data to CSV file
        data_to_append.to_csv(csv_file_path1, mode='a', header=False, index=False, index_label=False)
    
    # Sort and save the combined MNAR and MCAR data
    df = pd.read_csv(csv_file_path, header=None)
    df = df.sort_values(by=[1, 0])  # Sort by feature then by index
    df.to_csv(csv_file_path, index=False, header=False)
    
    print(f"CSV file sorted and saved to {csv_file_path}")


# Call the function to generate MCAR dataset using the length of the original dataset and the proportion of missing data from MNAR
generate_mcar_dataset(users_num, len(missing_data) / len(column))
