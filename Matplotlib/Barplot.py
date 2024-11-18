import matplotlib.pyplot as plt
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [35, 30, 40],
        'City': ['New York', 'London', 'Rio de Janairo']}
df = pd.DataFrame(data)

# Plotting a bar chart for Age by City
df.groupby('City')['Age'].mean().plot(kind='bar')
plt.xlabel('City')
plt.ylabel('Avearge Age')
plt.title('Avearge Age by City')
plt.show()