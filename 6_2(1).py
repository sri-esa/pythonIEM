# Write a program using matplotlib to use different types of Matplotlib Markers.
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, marker = '*g')
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
plt.show()
