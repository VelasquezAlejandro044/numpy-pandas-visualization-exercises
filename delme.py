#import pyplot module as alias plt
import matplotlib.pyplot as plt  

#import other libraries 
import numpy as np
import math
from random import randint
import random
import pandas as pd

# create 1000 equally spaced points between -10 and 10
x = [num for num in range(-10, 10)]

# calculate the y value for each element of the x vector
y = x**2 + 2*x + 2  

plt.plot(x, y)
plt.show()
