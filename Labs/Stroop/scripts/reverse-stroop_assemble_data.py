import pandas as pd
import glob
import re

path = '/Users/ethan/Documents/GitHub/Learn-PsychoPy/Labs/Stroop/experiments/reverse stroop/data'
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    #match = re.search('(?<=/)\d+', filename)
    #idnum = match.group()
    #df['ID'] = idnum
    df = df[df['resp.rt'].notna()]
    li.append(df)

df = pd.concat(li, axis=0, ignore_index=True)

out = path + '/all_data.csv'
df.to_csv(out, sep=',', encoding='utf-8')


data = df['resp.rt'].groupby([df['participant'], df['congruent']]).mean()

data = data.to_frame()

out = path + '/all_data_agg.csv'
data.to_csv(out, sep=',', encoding='utf-8')