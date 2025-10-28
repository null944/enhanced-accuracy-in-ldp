import matplotlib.pyplot as plt
import numpy as np

# Set global font to Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 12
plt.rcParams['mathtext.fontset'] = 'stix'

# Experimental data
domain_collected = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
UP_pertubation_time = [2.525999807403423e-06, 2.5939999613910914e-06, 3.3149999217130243e-06, 4.311000011512078e-06, 5.0000000919681044e-06, 5.627999926218763e-06, 6.703999752062373e-06, 7.756000049994327e-06, 8.79999999597203e-06, 9.867999324342236e-06]
TSP_pertubation_time = [5.394999825512059e-06, 5.381999944802373e-06, 6.796000234317035e-06, 8.391999872401356e-06, 9.814000077312812e-06, 1.1247999573242851e-05, 1.3296999750309624e-05, 1.5131000254768879e-05, 1.6956999897956847e-05, 1.9180999806849286e-05]

plt.figure(figsize=(8, 6))

x_pos = np.arange(len(domain_collected))
width = 0.6

# Calculate the height of the upper bars (TSP - UP)
upper_part = [TSP_pertubation_time[i] - UP_pertubation_time[i] for i in range(len(domain_collected))]

# Create stacked bar chart - using specified colors
bars_bottom = plt.bar(x_pos, UP_pertubation_time, width, alpha=1, color=[0.6235, 0, 0],
                     edgecolor='navy', linewidth=1.5, label='UP Time')
bars_top = plt.bar(x_pos, upper_part, width, bottom=UP_pertubation_time, alpha=1, 
                  color=[0.0, 0.227, 0.459], edgecolor='navy', linewidth=1.5, 
                  label='TSP Time')

plt.xlabel('Domain Size', fontsize=16, fontfamily='Times New Roman')
plt.ylabel('Time/s', fontsize=16, fontfamily='Times New Roman')

# Set x-axis labels
plt.xticks(x_pos, domain_collected)

plt.grid(True, alpha=0.3, axis='y')

# Add total time labels on bars
for i, (bar_bottom, bar_top) in enumerate(zip(bars_bottom, bars_top)):
    total_height = bar_bottom.get_height() + bar_top.get_height()
    plt.text(bar_top.get_x() + bar_top.get_width()/2., total_height * 1.02,
            f'{total_height:.1e}', ha='center', va='bottom', fontsize=10,
            fontweight='bold', color='black', fontfamily='Times New Roman')

# Set legend
plt.legend(prop={'family': 'Times New Roman', 'size': 14}, 
           frameon=True, edgecolor='black', facecolor='white', loc='upper left')

# Set axis ticks
plt.tick_params(axis='both', which='major', labelsize=14, direction='in')

# Ensure x-axis tick labels use Times New Roman font
for label in plt.gca().get_xticklabels():
    label.set_fontfamily('Times New Roman')

# Set appropriate y-axis range
max_total_time = max(TSP_pertubation_time)
plt.ylim(bottom=0, top=max_total_time * 1.2)

# Set x-axis range to make the chart look more compact
plt.xlim(left=-0.5, right=len(domain_collected)-0.5)

plt.tight_layout()
plt.show()