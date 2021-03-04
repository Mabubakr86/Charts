import os
import pandas as pd

path_to_chart_data = r''

os.chdir(path_to_chart_data)

def get_y(path_to_chart_data,x_limit = 0.5, y_limit = 0.35 ,x_value = -1 ):
    """
    Return y value float
    Get Value from Chart , 
    Value of x
    x_limit limit of x axis
    """
    df= pd.read_excel(path_to_chart_data)
    plot = plt.plot(df['x'],df['y'])
    xvalues = plot[0].get_xdata()
    yvalues = plot[0].get_ydata()
    x_limit = xvalues[-1]
    plt.close()

    y = None
    if 0 < x_value < x_limit: 
        for ind, val in enumerate (xvalues):
            if x_value > xvalues[ind-1] :
                if x_value < val:
                    y = yvalues[ind-1]

    elif x_value < 0 :
        y = 0
    elif x_value > x_limit :
        y = y_limit

    return y