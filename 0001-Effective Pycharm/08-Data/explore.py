import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#%%
auto = pd.read_csv(
'https://www.fueleconomy.gov/feg/epadata/vehicles.csv.zip')


#%%
# Just look at Ford, Lexus, & Toyota
(auto
    .groupby(['year', 'make'])
    .size()
    .unstack('make')
    .loc[:,['Ford', 'Lexus', 'Toyota']]
    .plot(kind='bar', figsize=(14,10))
)
plt.show()