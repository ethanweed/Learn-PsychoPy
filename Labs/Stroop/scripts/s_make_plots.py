import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np

pathin = '/Users/ethan/Documents/GitHub/Learn-PsychoPy/Labs/Stroop/experiments/stroop/data/'
pathout = '/Users/ethan/Documents/GitHub/Learn-PsychoPy/Labs/Stroop/figures/'
file = 'all_data_agg.csv'
file_out = pathout + 'stroop_boxplot.png'

df = pd.read_csv(pathin + file)
boxplot = sns.catplot(x="congruent", y="resp.rt", kind="box", data=df)

plt.savefig(file_out, transparent=True)
           
 
# paired t-test .... look into the warnings...
#incongruent = df.loc[(df.congruent == 0)].to_numpy()
#congruent = df.loc[(df.congruent == 1)].to_numpy()
#from scipy import stats
#import numpy as np
#res = stats.ttest_rel(congruent, incongruent)