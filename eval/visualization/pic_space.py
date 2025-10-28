import matplotlib.pyplot as plt
import numpy as np

# Set global font to Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 12
plt.rcParams['mathtext.fontset'] = 'stix'

# Experimental data
domain_collected = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
space_cost= [0.1556396484375, 0.3082275390625, 0.4608154296875, 0.6134033203125, 0.7659912109375, 0.9185791015625, 1.0711669921875, 1.2237548828125, 1.3763427734375, 1.5289306640625]

plt.figure(figsize=(8, 6))

x_pos = np.arange(len(domain_collected))
width = 0.6  # Slightly adjust width to accommodate more bars

# Create single bar chart for space cost
bars = plt.bar(x_pos, space_cost, width, alpha=1, color=[0.0, 0.227, 0.459],
               edgecolor='navy', linewidth=1.5, label='Space Cost')

plt.xlabel('Domain Size', fontsize=16, fontfamily='Times New Roman')
plt.ylabel('Space/M', fontsize=16, fontfamily='Times New Roman')

# Set x-axis labels
plt.xticks(x_pos, domain_collected)

plt.grid(True, alpha=0.3, axis='y')

# Add value labels on bars, keep 3 decimal places
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height * 1.05,
             f'{height:.3f}', ha='center', va='bottom', fontsize=10,  # Modified here: {height:.3f}
             fontweight='bold', rotation=0, fontfamily='Times New Roman')

# Set legend
plt.legend(prop={'family': 'Times New Roman', 'size': 14}, 
           frameon=True, edgecolor='black', facecolor='white', loc='upper left')

# Set axis ticks
plt.tick_params(axis='both', which='major', labelsize=14, direction='in')

# Ensure x-axis tick labels use Times New Roman font
for label in plt.gca().get_xticklabels():
    label.set_fontfamily('Times New Roman')

# Set appropriate y-axis range
plt.ylim(bottom=0, top=max(space_cost) * 1.15)

# Set x-axis range to make the chart look more compact
plt.xlim(left=-0.5, right=len(domain_collected)-0.5)

plt.tight_layout()
plt.show()