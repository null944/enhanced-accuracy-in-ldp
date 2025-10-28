import matplotlib.pyplot as plt
import numpy as np

# Set global font to Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 12
plt.rcParams['mathtext.fontset'] = 'stix'

# Experimental data
domain_collected = [100, 200, 300, 400, 500, 600, 700, 800,900,1000]
total_time = [2.9092070048500313e-04, 2.9781970019394065e-04, 3.103766999120126e-04, 3.156927003728924e-04, 3.263936994917458e-04, 3.4040370052389337e-04, 3.5009370038460475e-04, 3.5367269926064177e-04, 3.6089670071669385e-04, 3.709267011290649e-04]
uncertainty_time = [0.00028917870046279856, 0.00029605470014212187, 0.0003085276993660955, 0.00031390570044459307, 0.00032459969965566415, 0.0003384777008468518, 0.0003481776999105932, 0.0003519446994905593, 0.000359212700263015, 0.00036918670097657016]
pertubation_time= [1.7420000222045928e-06, 1.7650000518187881e-06, 1.849000545917079e-06, 1.7869999282993376e-06, 1.7939998360816389e-06, 1.9259996770415455e-06, 1.9160004740115253e-06, 1.7279997700825334e-06, 1.6840004536788911e-06, 1.7400001524947583e-06]

plt.figure(figsize=(8, 6))

x_pos = np.arange(len(domain_collected))
width = 0.6  # Slightly adjust width to accommodate more bars

# Create stacked bar chart
bars_bottom = plt.bar(x_pos, uncertainty_time, width, alpha=1, color=[0.6235, 0, 0],
                     edgecolor='navy', linewidth=1.5, label='Inherent UQ Time')
bars_top = plt.bar(x_pos, pertubation_time, width, bottom=uncertainty_time, alpha=1, 
                  color=[0.0, 0.227, 0.459], edgecolor='navy', linewidth=1.5, 
                  label='Perturb Recalib Time')

plt.xlabel('Domain Size', fontsize=16, fontfamily='Times New Roman')
plt.ylabel('Time/s', fontsize=16, fontfamily='Times New Roman')

# Set x-axis labels to 1100, 1200, ..., 1800
plt.xticks(x_pos, domain_collected)

# Linear scale (default)
# plt.yscale('log')  # Ensure no logarithmic scale

plt.grid(True, alpha=0.3, axis='y')

# Add value labels on bars, showing total time
for i, (bottom_bar, top_bar) in enumerate(zip(bars_bottom, bars_top)):
    total_height = bottom_bar.get_height() + top_bar.get_height()
    plt.text(bottom_bar.get_x() + bottom_bar.get_width()/2., total_height * 1.05,
             f'{total_height:.2e}', ha='center', va='bottom', fontsize=10,
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
plt.ylim(bottom=0, top=max(total_time) * 1.15)

# Set x-axis range to make the chart look more compact
plt.xlim(left=-0.5, right=len(domain_collected)-0.5)

plt.tight_layout()
plt.show()