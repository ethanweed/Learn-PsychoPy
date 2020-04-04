import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np

path = '/Users/ethan/Documents/GitHub/Learn-PsychoPy/Labs/Stroop/experiments/reverse stroop/data/'
file = 'all_data_agg.csv'
pathout = '/Users/ethan/Documents/GitHub/Learn-PsychoPy/Labs/Stroop/figures/'

df = pd.read_csv(path + file)
boxplot = sns.catplot(x="congruent", y="resp.rt", kind="box", data=df)
file_out = pathout + 'reverse_stroop_boxplot.png'

plt.savefig(file_out, transparent=True)
           
