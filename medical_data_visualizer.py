import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = (df['weight'])/((df['height']/100)**2)
df.loc[(df['overweight'] <= 25) , 'overweight'] = 0
df.loc[(df['overweight'] > 25) , 'overweight'] = 1
df['overweight'] = df['overweight'].astype(int)

# 3
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1

df_heat = df[(df['ap_lo'] <= df['ap_hi'])]
df_heat  = df_heat[(df['height'] >= df['height'].quantile(0.025))& (df['height'] <= df['height'].quantile(0.975))]
df_heat = df_heat[(df['weight'] >= df['weight'].quantile(0.025))& (df['weight'] <= df['weight'].quantile(0.975))]

def draw_cat_plot():
    # Converting data to long form
    df_cat = pd.melt(df, id_vars= 'cardio', value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"])


    # Generating count plot that shows count of variables, split by cardio
    fig = sns.catplot(data=df_cat, x='variable', hue='value', kind='count', col='cardio')

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    #Cleaning data by removing patients who have higher diastolic pressure than systolic and weight/height is in the bottom/top 2.5% percentile
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])]
    df_heat  = df_heat[(df['height'] >= df['height'].quantile(0.025))& (df['height'] <= df['height'].quantile(0.975))]
    df_heat = df_heat[(df['weight'] >= df['weight'].quantile(0.025))& (df['weight'] <= df['weight'].quantile(0.975))]
    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14

    fig, ass = plt.subplots(figsize=(11,8.8))
    
    # 15
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", linewidths=1, center=0,   vmin=-.14, vmax=0.28, square=True, cbar_kws={'shrink': 0.5}, ax=ass )



    # 16
    fig.savefig('heatmap.png')
    return fig
