import os
import pandas as pd
import matplotlib.pyplot as plt

# Create the 'out' folder if it doesn't exist
output_folder = 'out'
os.makedirs(output_folder, exist_ok=True)

# Read the CSV file containing X and Y values
data = pd.read_csv('digitized_data.csv', header=None, names=['X', 'Y'])

# Compute (X * Y) for each row
data['X_times_Y'] = data['X'] * data['Y']

# Find the maximum power point (MPP)
max_power_point = data.loc[data['X_times_Y'].idxmax()]

# Save MPP data to a separate CSV file
mpp_data = pd.DataFrame({'Voltage': [max_power_point['X']], 'Current': [max_power_point['Y']], 'Power': [max_power_point['X_times_Y']]})
mpp_data.to_csv(os.path.join(output_folder, 'mpp.csv'), index=False)

# Generate a plot with only the maximum power point
plt.plot(data['X'], data['Y'], label='Original Data')
plt.scatter(max_power_point['X'], max_power_point['Y'], color='red', label='Maximum Power Point')
plt.xlabel('Voltage')
plt.ylabel('Current')
plt.title('Original Plot with Maximum Power Point')
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(output_folder, 'original_plot.png'))
plt.close()

# Generate a plot with X on the x-axis and X*Y on the y-axis, renamed to mpp_plot.png
plt.plot(data['X'], data['X_times_Y'], label='Voltage vs Power')
plt.scatter(max_power_point['X'], max_power_point['X_times_Y'], color='red', label='Maximum Power Point')
plt.xlabel('Voltage')
plt.ylabel('Power')
plt.title('Plot of Voltage vs Power')
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(output_folder, 'mpp_plot.png'))
plt.close()

print("Maximum power point data saved to 'out/mpp.csv'")
print("Original plot with maximum power point saved as 'out/original_plot.png'")
print("Plot of Voltage vs Power saved as 'out/mpp_plot.png'")
