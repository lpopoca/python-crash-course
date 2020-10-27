# 15-1 Cubes: A number raised to the third power is a cube. Plot the first five cubic numbers, and then plot the first 5000 cubic numbers.

import matplotlib.pyplot as plt

# Create the values
x_values = [1,2,3,4,5]
y_values = [x**3 for x in x_values]

# Style
plt.style.use('seaborn')

# Define the plot
fig,ax = plt.subplots()
ax.scatter(x_values,y_values,s=100)

# Set the chart title and labes the axes.
ax.set_title("Cubed Numbers",fontsize=24)
ax.set_xlabel("Values",fontsize=14)
ax.set_ylabel("Cubed Values",fontsize=14)

# Set the size of the tick labels.
ax.tick_params(axis='both',which='major',labelsize=14)

# Show the plot
plt.show()

