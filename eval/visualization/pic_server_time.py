import matplotlib.pyplot as plt
import numpy as np

# Set global font to Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'stix'

# Experimental data
domain_collected = [100, 200, 300, 400, 500, 600, 700, 800,900,1000]
uncertainty_time= [1.938499975949526e-05, 2.2772997617721557e-05, 2.6711998507380486e-05, 3.052700078114867e-05, 3.538200166076422e-05, 3.890999942086637e-05, 4.4579998357221486e-05, 4.645099863409996e-05, 5.040999385528266e-05, 5.3844997892156244e-05]
pertubation_time= [3.272003959864378e-06, 3.2170012127608063e-06, 3.301999531686306e-06, 3.3089984208345415e-06, 3.6019971594214437e-06, 3.391997888684273e-06, 3.4909998066723346e-06, 3.2970006577670575e-06, 3.37300356477499e-06, 3.2049999572336676e-06]
total_time= [2.2657003719359635e-05, 2.5989998830482365e-05, 3.001399803906679e-05, 3.3835999201983216e-05, 3.898399882018566e-05, 4.2301997309550645e-05, 4.807099816389382e-05, 4.974799929186702e-05, 5.3782997420057654e-05, 5.704999784938991e-05]
space_cost= [0.001556396484375, 0.003082275390625, 0.004608154296875, 0.006134033203125, 0.007659912109375, 0.009185791015625, 0.010711669921875, 0.012237548828125, 0.013763427734375, 0.015289306640625]

plt.figure(figsize=(8, 6))  # Change to 8×6 size

# Scale the x-axis data by 100 times
x_pos = np.arange(len(domain_collected))
x_values = [x/100 for x in domain_collected]  # 100->1, 200->2, ..., 1000->10

width = 0.3  # Adjust bar width to fit smaller figure size

# Create primary y-axis (left)
ax1 = plt.gca()

# Create stacked bar chart for time cost (left) - adjust transparency for grid lines visibility
bars_bottom = ax1.bar(x_pos - width/2, uncertainty_time, width, alpha=0.8, color=[0.6235, 0, 0],
                     edgecolor='navy', linewidth=1.5, label='Inherent UQ Time')
bars_top = ax1.bar(x_pos - width/2, pertubation_time, width, bottom=uncertainty_time, alpha=0.8, 
                  color=[0.0, 0.227, 0.459], edgecolor='navy', linewidth=1.5, 
                  label='Perturb Recalib Time')

ax1.set_xlabel('Domain Size ($\\times10^2$)', fontsize=28, fontfamily='Times New Roman')
ax1.set_ylabel('Time/s', fontsize=28, fontfamily='Times New Roman', color='black')

# Set x-axis labels to 1,2,...,10
x_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
plt.xticks(x_pos, x_labels)

# Add grid - adjust grid line color and thickness for visibility on all bars
ax1.grid(True, alpha=0.5, axis='y', color='gray', linewidth=1)

# Create secondary y-axis (right)
ax2 = ax1.twinx()

# Create bar chart for space cost (right) - adjust transparency for grid lines visibility
bars_space = ax2.bar(x_pos + width/2, space_cost, width, alpha=0.8, color=[0.0, 0.4, 0.0],  # Darker green
                    edgecolor='navy', linewidth=1.5, label='Space Cost')  # Add navy border

ax2.set_ylabel('Space/M', fontsize=28, fontfamily='Times New Roman', color='black')

# Combine legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, 
           prop={'family': 'Times New Roman', 'size': 22}, 
           frameon=True, edgecolor='black', facecolor='white', loc='upper left')

# Set axis ticks - specifically set x-axis tick font size to 28
ax1.tick_params(axis='x', which='major', labelsize=28, direction='in')  # x-axis tick font size 28
ax1.tick_params(axis='y', which='major', labelsize=28, direction='in')  # y-axis tick font size 28
ax2.tick_params(axis='y', which='major', labelsize=28, direction='in')  # right y-axis tick font size 28

# Set y-axis to use scientific notation
from matplotlib.ticker import ScalarFormatter

# Use scientific notation for time axis
ax1.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
ax1.yaxis.get_offset_text().set_fontsize(28)

# Ensure x-axis tick labels use Times New Roman font
for label in ax1.get_xticklabels():
    label.set_fontfamily('Times New Roman')
    label.set_fontsize(28)  # Ensure x-axis tick label font size is 28

# Set y-axis range
ax1.set_ylim(bottom=0, top=max(total_time) * 1.3)
ax2.set_ylim(bottom=0, top=max(space_cost) * 1.3)

# Set x-axis range to make the chart more compact
ax1.set_xlim(left=-0.5, right=len(domain_collected)-0.5)

plt.tight_layout()
plt.show()