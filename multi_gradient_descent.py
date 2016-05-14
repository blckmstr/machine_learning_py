import matplotlib.pyplot as plt
import os
import numpy as np

print(os.getcwd())

data = []

with open(os.getcwd()+'/ex1data2.txt','r') as f:
    for i in f.readlines():
        data.append(i.rstrip('\n').split(','))

print(data)
