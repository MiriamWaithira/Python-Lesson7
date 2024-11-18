import matplotlib.pyplot as plt
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [35, 30, 40],
        'City': ['New York', 'London', 'Rio de Janairo']}
df = pd.DataFrame(data)

# Plotting a scatter plot of Age vs. City
df.plot(kind='scatter', x='City', y='Age')
plt.title('City vs. Age')
plt.show()