# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 09:54:44 2023

@author: Jakob D Topping
Unit 12A Assignment
"""

import numpy as np
import matplotlib.pyplot as plt

#PART 1

#First Array
array1 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("Array 1:")
print(array1)
print("Data Type:", array1.dtype)

#Second Array
array2 = np.array([[1, 2, 3], ["cat", "dog", "ferret"]])
print("\nArray 2:")
print(array2)
print("Data Types:", array2.dtype)


#ARRAY INFOS


#array 1
print("\nArray 1 Info:")
print("Dimensions:", array1.ndim)
print("Shape:", array1.shape)
print("Data Type:", array1.dtype)
print("Item Size:", array1.itemsize)



#Array 2
print("\nArray 2 Info:")
print("Dimensions:", array2.ndim)
print("Shape:", array2.shape)
print("Data Types:", array2.dtype)
print("Item Size:", array2.itemsize)


#Array Axes
print("\nAxes:")
print("Array 1, Axis 0:", array1[0])
print("Array 2, Axis 1:", array2[1])


#PART 2

#RAINfall Data
rainfall_data = [
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    [1.75, 1.62, 2.19, 3.75, 3.94, 3.83, 3.33, 4.06, 3.67, 2.75, 2.96, 2.18]
]
rainfall_array = np.array(rainfall_data)

#ARRAY 3 INFO
print("\nRainfall Array:")
print(rainfall_array)
print("Data Types:", rainfall_array.dtype)


#FLOAT ARRAY
rainfall_float = rainfall_array[1].astype(float)
print("\nRainfall as Floats:")
print(rainfall_float)

#PLOT CHART
plt.plot(rainfall_array[0], rainfall_float)
plt.xlabel("Months")
plt.ylabel("Average Precipitation (inches)")
plt.title("Average Monthly Precipitation in Racine, WI")
plt.show()

#PART 3
#BAR CHART
plt.bar(rainfall_array[0], rainfall_float, color="yellow")
plt.ylabel("Average Precipitation (inches)")
plt.xlabel("Months")
plt.title("Average Monthly Precipitation in Racine, WI")
plt.show()


#SCATTER PLOT

plt.scatter(rainfall_array[0], rainfall_float, color="orange")
plt.xlabel("Months")
plt.ylabel("Average Precipitation (inches)")
plt.title("Scatter Plot of Average Monthly Precipitation in Racine, WI")
plt.show()