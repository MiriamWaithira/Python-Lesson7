import pandas as pd

# Creating Dataframes from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [35, 30, 40],
        'City': ['New York', 'London', 'Rio de Janairo']}

df = pd.DataFrame(data)
# print(df)

# MANIPULATING DATAFRAMES
# Selecting columns
df_age = df['Age'] #select the age column

# Filtering Rows
df_filtered = df[df['Age'] > 30] #returns rows where age > 30
df_multiplefilter = df[(df['Age'] > 30) & (df['City'] == 'Rio de Janairo')]

# Adding/Removing Columns
df['Country'] = ['USA', 'UK', 'Brazil']  #Adds the column
df.drop('Country', axis=1, inplace=True)   #Drops the 'Country' column

# SORTING DATA
# Sort by columns
df_sorted = df.sort_values(by='Age', ascending=False)  #sort by age in descending order
# sort by multiple columns
df_multiplesorted = df.sort_values(by=['Age', 'City'], ascending=[True, False])   #sort by age in ascending order

# AGGREGATING DATA
# Groupby
grouped = df.groupby('City').agg({'Age': 'mean', 'Name': 'count'})
# summary statistics
mean_age = df['Age'].mean()  #mean of 'Age' column
sum_age = df['Age'].sum()   #sum of 'Age' column
max_age = df['Age'].max()   #maximum of 'Age' column
 


print(df)
print(df_age)
print(df_filtered)
print(df_multiplefilter)
print(df_sorted)
print(df_multiplesorted)
print(grouped)
print(mean_age)
print(sum_age)
print(max_age)