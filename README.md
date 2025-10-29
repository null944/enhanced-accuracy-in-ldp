# Enhancing Local Differential Privacy Accuracy by Exploiting Inherent Uncertainty

---

## Abstract
Local differential privacy (LDP) has emerged as the de facto standard for privacy preservation in the local setting. It thwarts inference attacks by injecting uncertainty between users’ true sensitive data and reported values. While existing LDP protocols effectively prevent direct leakage of sensitive attributes, they largely overlook privacy risks arising from indirect inference where adversaries exploit correlated nonsensitive data to deduce private attributes. The core challenge lies in (1) accurately quantifying indirect leakage risks and (2) optimizing perturbation parameters to maximize data utility while maintaining strict LDP guarantees.

To address the above challenge, we propose the concept of inherent uncertainty, a novel metric to quantify correlations between the collected non-sensitive attributes and their associated sensitive attributes, and introduce an enhanced LDP framework by exploiting inherent uncertainty, which ensures compatibility with major LDP base protocols. We implement inherent uncertainty quantification and perturbation parameter recalibration through integration with concrete LDP protocols. Furthermore, we handle a hybrid scenario, where the collected attribute contains both directly sensitive and correlated non-sensitive values. We propose a dual-phase perturbation method to address the leakage-pattern-driven hybrid privacy problem, which maximizes data utility while satisfying distinct privacy requirements for different values. Theoretical analysis proves our approaches guarantee LDP, while experiments demonstrate their effectiveness. Code and data are available at https://anonymous.4open.science/r/enhancedaccuracy-in-ldp-6BC3/.

---
## Quick Start

### Install the required packages
`pip install  -r requirements.txt`

### Data Preprocessing

#### Missing List Generation
Run the following script to generate MCAR and MNAR missing lists. Before execution, specify the missing dataset by adjusting the `dataset` variable. Modify the `missing_rate` list to dynamically partition intervals and adjust the missing rate.

`python ./src/data_preprocessing/missing_generator.py`

The files `adult_salary_1_miss_MCAR.csv`, `adult_salary_1_miss_MNAR.csv`, `GentH_1_miss_MCAR.csv`, and `GentH_1_miss_MNAR.csv` in the `data/processed/` directory are generated missing lists. The missing data collection algorithm utilizes the  missing list and the original dataset to generate the missing dataset.

#### Data Scaling
Perform data normalization processing, and determine the target scaling dataset by adjusting the `dataset` variable prior to execution.

`python ./src/data_preprocessing/scaler.py`

The files `adult_salary_1.csv` and `GentH_1.csv` in the `data/processed/` directory are the scaled datasets.

### Enhanced Pure LDP Protocols
Corresponding to Section 4 of the paper.

Before running any method (including the proposed method and baseline methods), you must set the desired dataset name by modifying the `dataset` variable in the corresponding code file. The dataset names for different scenarios are listed in the table below.

<table border="1" style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">method comparison</th>
    <th>dataset1</th>
    <th>dataset2</th>
  </tr>
  <tr>
    <td><strong>RR vs ARR</strong></td>
    <td>adult_salary</td>
    <td>CDC_COST</td>
  </tr>
  <tr>
    <td><strong>GRR vs AGRR</strong></td>
    <td>adult_age</td>
    <td>CDC_BMI</td>
  </tr>
  <tr>
    <td><strong>OUE vs AOUE</strong></td>
    <td>adult_age</td>
    <td>CDC_BMI</td>
  </tr>
  <tr>
    <td><strong>UP vs TSP</strong></td>
    <td>adult_salary</td>
    <td>GentH</td>
  </tr>
  <tr>
    <td><strong>Bisample</strong></td>
    <td>adult_salary_1</td>
    <td>GentH_1</td>
  </tr>
</table>

This paper dynamically determines the perturbation parameters `p` and `q` for attribute `A` by calculating the inherent uncertainty parameters of the sensitive attribute `S` and the related attribute `A`, thereby optimizing the RR, GRR, and OUE protocols. The optimized protocols are ARR, AGRR, and AOUE.

#### Evaluate the mean square error
Run the following scripts to calculate the MSE for each method. Ensure that the dataset name specified in each script corresponds to your intended dataset.

`python ./src/our_method/correlation_perturbation/ARR.py`

`python ./src/our_method/correlation_perturbation/AGRR.py`

`python ./src/our_method/correlation_perturbation/AOUE.py`

Note: By adjusting the values of `p` and `q` in ARR.py, AGRR.py, and AOUE.py, you can test the MSE of the RR, GRR, and OUE protocols.

#### Evaluating Time and Space Overhead
Run the following performance evaluation script to determine the time-space overhead:

`python ./eval/metrics/test_AGRR_client.py`

`python ./eval/metrics/test_AGRR_server.py`

`python ./eval/metrics/test_AOUE_client.py`

`python ./eval/metrics/test_AOUE_server.py`

`python ./eval/metrics/text_ARR_server.py`

`python ./eval/metrics/text_ARR_server.py`

### Two-Stage Perturbation Method
Corresponding to Section 5 of the paper.

#### Evaluate the mean square error
Run the following scripts to calculate the MSE for each method. Ensure that the dataset name specified in each script corresponds to your intended dataset.

`python ./src/our_method/missing_perturbation/TSP.py`

`python ./src/baselines/UP.py`

`python ./src/baselines/Bisample.py`

#### Evaluating Time and Space Overhead
Run the following performance evaluation script to determine the time-space overhead:

`python ./eval/metrics/test_TSP_client.py`

`python ./eval/metrics/test_TSP_server.py`

All results (including runtime, memory usage, etc.) will be automatically saved to the corresponding files under the `results/` directory.

### Result Visualization
Generate images of temporal and spatial costs by running the Python files located in the `./eval/visualization/` directory.

Generate MSE images by running the MATLAB files located in the `./eval/visualization/` directory.
