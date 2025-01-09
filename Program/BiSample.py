import numpy as np
import pandas as pd
import math
import random

epsilon = 1.5

def BiSample_MD(value):   
    p_none = 1 / (math.exp(epsilon) + 1)
    p_pos = 0
    p_neg = 0
    b = 0
    s = 0
    coin = random.random()
    if coin < 0.5:
        s = 0  # Negative sampling
    else:
        s = 1  # Positive sampling
    if s == 0:  # Negative sampling
        if value is None:  # Perturbation for missing values
            coin = random.random()
            if coin <= p_none:
                b = 1
            else:
                b = 0
            return [s, b]
        else:
            if value < -1 or value > 1:
                print("value is invalid")
                return None
            p_neg = ((1 - math.exp(epsilon)) / (1 + math.exp(epsilon))) * (value / 2) + 0.5
            coin = random.random()
            if coin <= p_neg:
                b = 1
            else:
                b = 0
            return [s, b]
    else:  # Positive sampling
        if value is None:  # Perturbation for missing values
            coin = random.random()
            if coin <= p_none:
                b = 1
            else:
                b = 0
            return [s, b]
        else:
            if value < -1 or value > 1:
                print("value is invalid")
                return None
            p_pos = ((math.exp(epsilon) - 1) / (math.exp(epsilon) + 1)) * (value / 2) + 0.5
            coin = random.random()
            if coin <= p_pos:
                b = 1
            else:
                b = 0
            return [s, b]

# Generate a dataset with missing values
dataset = 'GentH_1'
mechanism = 'MNAR'
Dataset = pd.read_csv(dataset + '.csv', header=None)
Dataset1 = pd.read_csv(dataset + '.csv', header=None)
Miss_list = pd.read_csv(dataset + '_miss_' + mechanism + '.csv', header=None)

num = len(Dataset)  # The number of users
miss_list = np.loadtxt(dataset + '_miss_' + mechanism + '.csv', delimiter=",", skiprows=0)

for row in miss_list:  # Set missing positions to None
    i, j = int(row[0]), int(row[1])
    Dataset.iloc[i, j] = None
Dataset.replace({np.nan: None}, inplace=True)

if isinstance(Dataset, pd.DataFrame):
    # If it's a DataFrame, select the first column and convert to Series
    data_series = Dataset.iloc[:, 0]
else:
    # If it's already a Series
    data_series = Dataset

# Filter out None and NaN values
filtered_data = data_series[data_series.notna()]

# Calculate mean
mean_value = filtered_data.mean()
print(mean_value)

p = math.exp(epsilon) / (1 + math.exp(epsilon))
Perturb_result = []
real_average = mean_value
real_f_null = len(Miss_list) / num

Error_ave = []
Error_f = []
Var_ave = []
Var_f = []

for i in range(100):
    f_Pos = f_Neg = num_pos = num_neg = pos_per = neg_per = 0
    for column in Dataset.columns:  # Perturb every column
        Perturb_result = []  # Clear Perturb_result
        f_Pos = f_Neg = num_pos = num_neg = pos_per = neg_per = 0
        for index, value in Dataset[column].items():
            result = BiSample_MD(value)
            Perturb_result.append(result)

        # Count average
        for list_item in Perturb_result:
            if list_item[0] == 1:
                num_pos += 1
                if list_item[1] == 1:
                    pos_per += 1
            elif list_item[0] == 0:
                num_neg += 1
                if list_item[1] == 1:
                    neg_per += 1
        
        if num_pos > 0:
            f_Pos = pos_per / num_pos
        if num_neg > 0:
            f_Neg = neg_per / num_neg

        average = (f_Pos - f_Neg) / (f_Pos + f_Neg + 2*p - 2) if (f_Pos + f_Neg + 2*p - 2) != 0 else 0
        f_null = (1 - f_Pos - f_Neg) / (2*p - 1) if (2*p - 1) != 0 else 0

        error_ave = abs(average - real_average)
        var_ave = error_ave ** 2
        error_f = abs(f_null - real_f_null)
        var_f = error_f ** 2

        Error_ave.append(error_ave)
        Var_ave.append(var_ave)
        Error_f.append(error_f)
        Var_f.append(var_f)

mean_ave = sum(Error_ave) / len(Error_ave)
var_ave = sum(Var_ave) / len(Var_ave)
mean_f = sum(Error_f) / len(Error_f)
var_f = sum(Var_f) / len(Var_f)

print("mean_ave:", mean_ave)
print("var_ave:", var_ave)
print("mean_f:", mean_f)
print("var_f:", var_f)
