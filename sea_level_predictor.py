import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 10))
    y = df['CSIRO Adjusted Sea Level']
    x = df['Year']
    plt.scatter(x, y)

    # Create first line of best fit
    future_years = np.arange(x.min(), 2051)
    slope, intercept, r, p, se = linregress(x,y)
    future_sea_levels = intercept + slope * future_years
    plt.plot(future_years, future_sea_levels, 'r', label='Predicted Rise Until 2050')

    # Create second line of best fit
    df_recent = df[df['Year']>=2000]
    x_recent = df_recent['Year']
    y_recent = df_recent['CSIRO Adjusted Sea Level']
    r_slope, r_intercept, r_r, r_p, r_se = linregress(x_recent,y_recent)

    future_years = np.arange(x_recent.min(), 2051)
    future_sea_levels_recent = r_intercept + r_slope * future_years
    plt.plot(future_years, future_sea_levels_recent, 'r--', label='Predicted Rise Based on 2000 Onwards ')


    # Add labels and title
    plt.title('Year')
    plt.xlabel('Rise in Sea Level')
    plt.ylabel("Sea Level (inches)")
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

