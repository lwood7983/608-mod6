import pandas as pd
titanic = pd.read_csv('https://vincentarelbundock.github.io/' + 
    'Rdatasets/csv/carData/TitanicSurvival.csv')


pd.set_option('precision', 2)
titanic.head()

titanic.tail()

titanic.columns = ['name', 'survived', 'sex', 'age', 'class']

titanic.describe()

(titanic.survived == 'yes').describe()


import matplotlib.pyplot as plt
histogram = titanic.hist()
plt.show()