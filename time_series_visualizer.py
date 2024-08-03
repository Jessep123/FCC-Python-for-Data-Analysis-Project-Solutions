import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)
# Clean data
df_lower_quant =  df['value'].quantile(0.025)
df_upper_quant = df['value'].quantile(0.975)

df = df[(df['value'] <= df_upper_quant) & (df['value'] >= df_lower_quant)]

#df = df[(df['value'] <= df_upper_quant)]
#df = df[(df['value'] >= df_lower_quant)]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(20, 5))    
    # Plot the DataFrame on the provided axis
    df.plot(ax=ax, color='r',use_index=True)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['year'] = df.index.year
    df['month'] = df.index.month
    df_bar = df.groupby(['year', 'month'])['value'].mean().unstack()
    fig, ax = plt.subplots(figsize = (5,5))
    df_bar.plot(kind='bar', ax=ax)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
        # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    # Year-wise box plot
    sns.boxplot(data=df_box, x='year', y='value', hue='year', ax=axes[0], palette=['#4073a6', '#fba832', '#73b839', '#fb4032'])
    axes[0].set_ylabel('Page Views')
    axes[0].set_xlabel('Year')
    axes[0].set_title('Year-wise Box Plot (Trend)')
    # Month-wise box plot
    sns.boxplot(data=df_box, x='month', y='value', hue='month', ax=axes[1], order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axes[1].set_ylabel('Page Views')
    axes[1].set_xlabel('Month')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
