import pandas as pd

HairEyeColor = pd.read_csv('https://vincentarelbundock.github.io/' + 
    'Rdatasets/csv/datasets/HairEyeColor.csv')


HairEyeColor.head()

HairEyeColor.columns = ['remove', 'Hair', 'Eye', 'Gender', 'Count']

HairEyeColor.head()

HairEyeColor.pop('remove')

HairEyeColor.head()
HairEyeColor.describe()
pd.set_option('precision', 2)

HairEyeColor.describe()

import matplotlib.pyplot as plt
histogram = HairEyeColor.hist()
plt.show()

