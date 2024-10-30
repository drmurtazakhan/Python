# Import libraries
import numpy as np 
 
 
# Creating dataset
a = np.random.randint(100, size =(50))
 
# Creating histogram
np.histogram(a, bins = [0, 10, 20, 30, 40,
                        50, 60, 70, 80, 90,
                        100])
 
hist, bins = np.histogram(a, bins = [0, 10, 
                                     20, 30,
                                     40, 50,
                                     60, 70,
                                     80, 90,
                                     100]) 

# printing histogram
print()
print (hist) 
print (bins) 
print()