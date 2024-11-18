import matplotlib.pyplot as plt
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [35, 30, 40],
        'City': ['New York', 'London', 'Rio de Janairo']}
df = pd.DataFrame(data)

# Plotting Age vs. Name
# plt.plot(df['Name'], df['Age'])
df['Age'].plot(kind='line', color='green', linestyle='--', linewidth=2)
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Name vs. Age')
plt.show()