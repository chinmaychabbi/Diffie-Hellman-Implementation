import matplotlib.pyplot as plt

# Data for bar graph
categories = ['Small-Scale Testing', 'Large-Scale Testing']
detection_rates = [74.3, 96.5]

# Create the bar graph
plt.figure(figsize=(8, 5))
plt.bar(categories, detection_rates, width=0.5, color=['blue', 'green'])

# Add titles and labels
plt.title('Comparison of Detection Rates', fontsize=14)
plt.ylabel('Detection Rate (%)', fontsize=12)
plt.xlabel('Testing Scale', fontsize=12)

# Add percentage labels on top of bars
for i, rate in enumerate(detection_rates):
    plt.text(i, rate + 1, f'{rate}%', ha='center', fontsize=10)

# Display the plot
plt.tight_layout()
plt.show()
