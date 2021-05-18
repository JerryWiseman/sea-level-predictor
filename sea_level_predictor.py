import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x = df['Year']
    y = df["CSIRO Adjusted Sea Level"]
    fig, ax = plt.subplots(figsize=(10,6))
    ax.scatter(x,y, color ='blue', label = "scatter plot" )
    
    # Create first line of best fit
    res = linregress(x,y)
    new_row = pd.Series(data={'Year':2050,"CSIRO Adjusted Sea Level":0})
    df2= df.append(new_row, ignore_index=True)
    x2 = df2['Year']
    y2 = res.intercept + res.slope*x2
    ax.plot(x2, y2, 'r', label='fitted line 1')

    # Create second line of best fit
    filt = df['Year']>=2000
    df3 = df[filt]
    x3 = df3['Year']
    y3 = df3["CSIRO Adjusted Sea Level"]
    res3 = linregress(x3,y3)
    df3= df3.append(new_row, ignore_index=True)
    x3 = df3['Year']
    y3 = res3.intercept + res3.slope*x3
    ax.plot(x3, y3, 'g', label='fitted line 2')
    plt.legend()
    
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()