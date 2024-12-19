# Write a program using matplotlib to display Matplotlib Histograms and Legends.
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 