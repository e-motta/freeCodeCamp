import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)
df.loc[df['BMI'] > 25, 'overweight'] = 1
df.loc[df['BMI'] <= 25, 'overweight'] = 0
df['overweight'] = df['overweight'].convert_dtypes()
df.drop(columns=['BMI'], inplace=True)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.value_counts().reset_index(name='total').sort_values('variable')

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x='variable', y ='total', hue='value', data=df_cat, col='cardio', kind='bar').fig

    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[df['ap_lo'] <= df['ap_hi']]
    df_heat = df_heat[df['height'] >= df['height'].quantile(0.025)]
    df_heat = df_heat[df['height'] <= df['height'].quantile(0.975)]
    df_heat = df_heat[df['weight'] >= df['weight'].quantile(0.025)]
    df_heat = df_heat[df['weight'] <= df['weight'].quantile(0.975)]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(len(corr), len(corr.columns)))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(data=corr, mask=mask, vmax=0.3, center=0, annot=True, ax=ax,
                square=True, linewidths=1, cbar_kws={"shrink": .5}, fmt='.1f')

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

# draw_heat_map()