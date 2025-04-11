import pandas as pd
import numpy as np
import os
import re
import csv

from matplotlib import pyplot as plt
import matplotlib as mpl

def match_pattern(string):
    pattern = r"\d+\.\d+"
    match = re.search(pattern, string)

    if match:
        number = float(match.group())
    else:
        print("No match found.")
    return number

def get_afm_data(filename):
    with open(filename) as f:
        header = [next(f).strip() for _ in range(4)]
        data = [[float(value) for value in row] for row in csv.reader(f, delimiter='\t')]
    x = np.linspace(0, match_pattern(header[1]), np.shape(data)[1])
    y = np.linspace(0, match_pattern(header[2]), np.shape(data)[0])

    X, Y = np.meshgrid(x,y)
    Z = data
    
    return {'X':X, 'Y':Y, 'Z':Z}

filename = "<ENTER FULL FILENAME WITH PATH AND EXTENSION>"
data = get_afm_data(pdir_txt + filename)

fig,ax = plt.subplots()
c = plt.pcolor(data1['X'], -data1['Y'], [[dat*1e06 for dat in row] for row in data1['Z']], cmap='afmhot')
cbar = fig.colorbar(c)
cbar.set_label('Height ($\mu$m)')
plt.xlabel('x-distance ($\mu$m)')
plt.ylabel('y-distance ($\mu$m)')

yticks =  ax.get_yticks()
ax.set_yticklabels([int(abs(tick)) for tick in yticks])

plt.show()
