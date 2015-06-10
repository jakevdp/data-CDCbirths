# Script to cleanup the raw data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

births = pd.read_csv('births.csv')

# throw out bad data
births = births.query('(births > 1000) & (births < 30000)')

# set 'day' column to integer; was a string due to nulls
births['day'] = births['day'].astype(int)

# compute an order
order = births['month'] + births['day'] / 31
births.groupby(order)['births'].mean().plot()
plt.gca().set_xticks(range(1, 14))
plt.gca().set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan'])
plt.xlim(0.5, 13.5)
plt.title('USA births by day of month')
plt.ylabel('mean births')

plt.show()
