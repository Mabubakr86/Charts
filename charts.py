import os
import pandas as pd
import matplotlib.pyplot as plt

path_to_charts_data = r'F:\scripts\general\charts'
os.chdir(path_to_charts_data)
data = {'1/8':'chart1.csv'}

def get_y(x,ser=None):
    """
    Return y value float
    Get Value from Chart , 
    Value of x
    x_limit limit of x axis
    """
    df= pd.read_csv(data[ser])
    plot = plt.plot(df['x'],df['y'])
    xvalues = plot[0].get_xdata()
    yvalues = plot[0].get_ydata()
    x_limit = xvalues[-1]
    xmin = xvalues[0]
    y_limit = yvalues[-1]
    ymin = yvalues[0]
    plt.close()

    y = None
    if xmin < x < x_limit: 
        for ind, val in enumerate (xvalues):
            if x > xvalues[ind-1] :
                if x < val:
                    y = yvalues[ind-1]

    elif x < xmin :
        y = ymin
    elif x > x_limit :
        y = y_limit

    return y

if __name__ == '__main__':
    print(get_y(x=99.6, ser='1/8'))
