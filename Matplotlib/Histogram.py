import matplotlib.pyplot as plt
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [35, 30, 40],
        'City': ['New York', 'London', 'Rio de Janairo']}
df = pd.DataFrame(data)

# Plotting a histogram for Age
df['Age'].plot(kind='hist', bins=10)
plt.xlabel('Age')
plt.title('Age Distribution')
plt.show()