'''STATISTICS FOR AI/ML'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

#employee salaries(in thousand)
salaries=[22,28,35,42,38,55,48,60,72,85,30,45,52,65,28,34,41,58,75,90]

#central tendency-where is the 'centre' of data
mean =np.mean(salaries) #average
median=np.median(salaries) #middle value when sorted
mode=stats.mode(salaries,keepdims=True).mode[0] #most frequent

print(f'mean (average):Rs.{mean:.1f}k')
print(f'median  (middle value):Rs.{median}k')
print(f'mode  (most common): Rs.{mode}k')