import matplotlib.pyplot as plt
import numpy as np
import pandas

# Set global font to Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'stix'

# Experimental data
domain_collected = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
pertubation_time= [3.5326000070199374e-05, 7.281900150701403e-05, 0.00011053900350816549, 0.0001609259971883148, 0.0001865479990374297, 0.00022044400102458895, 0.0002619869960471988, 0.00029438000055961313, 0.0003333930007647723, 0.00035045899916440247]

plt.figure(figsize=(8, 6))

x_pos = np.arange(len(domain_collected))
width = 0.6  # Slightly adjust width to accommodate more bars

# Create single bar chart for perturbation time
bars = plt.bar(x_pos, pertubation_time, width, alpha=1, color=[0.0, 0.227, 0.459],
               edgecolor='navy', linewidth=1.5, label='Perturbation Time')

plt.xlabel('Domain Size ($\\times10^2$)', fontsize=28, fontfamily='Times New Roman')
plt.ylabel('Time/s', fontsize=28, fontfamily='Times New Roman')  # Modified y-axis label

# Set x-axis labels to 1,2,...,10
x_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
plt.xticks(x_pos, x_labels)

plt.grid(True, alpha=0.3, axis='y')

# Set legend
plt.legend(prop={'family': 'Times New Roman', 'size': 22}, 
           frameon=True, edgecolor='black', facecolor='white', loc='upper left')

# Set axis ticks
plt.tick_params(axis='both', which='major', labelsize=28, direction='in')

# Ensure x-axis tick labels use Times New Roman font
for label in plt.gca().get_xticklabels():
    label.set_fontfamily('Times New Roman')

# Set y-axis to use scientific notation
plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
plt.gca().yaxis.get_offset_text().set_fontsize(28)

# Set appropriate y-axis range
plt.ylim(bottom=0, top=max(pertubation_time) * 1.15)

# Set x-axis range to make the chart look more compact
plt.xlim(left=-0.5, right=len(domain_collected)-0.5)

plt.tight_layout()
plt.show()