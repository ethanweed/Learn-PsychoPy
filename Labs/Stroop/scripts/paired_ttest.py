
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np

path = '/Users/ethan/Documents/GitHub/Learn-PsychoPy/Labs/Stroop/experiments/stroop/data/all_data_agg.csv'

df = pd.read_csv(path)           

incongruent = df.loc[(df.congruent == 'incong')]
congruent = df.loc[(df.congruent == 'cong')]

incong = incongruent['resp.rt'].to_numpy()
cong = congruent['resp.rt'].to_numpy()

from scipy import stats
import numpy as np
res = stats.ttest_rel(cong, incong)
print(res)