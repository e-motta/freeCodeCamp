import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = 'Year'
    y = 'CSIRO Adjusted Sea Level'
    df.plot.scatter(x=x, y=y)

    # Create first line of best fit
    linreg_1080_2013 = linregress(df[x], df[y])
    series_1880_2050 = pd.DataFrame({'Year': [i for i in range(1880, 2051)]})
    plt.plot(series_1880_2050, linreg_1080_2013.slope * series_1880_2050 + linreg_1080_2013.intercept)

    # Create second line of best fit
    df_2000_2013 = df[df[x] >= 2000]
    linreg_2000_2013 = linregress(df_2000_2013[x], df_2000_2013[y])
    series_2000_2050 = pd.DataFrame({'Year': [i for i in range(2000, 2051)]})
    plt.plot(series_2000_2050, linreg_2000_2013.slope * series_2000_2050 + linreg_2000_2013.intercept)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
