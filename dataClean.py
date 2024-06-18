import pandas as pd

csv_file_path = 'data.csv'  
df = pd.read_csv(csv_file_path)

filtered_df = df[df['Age'] > 30]
print("Filtered DataFrame (Age > 30):")
print(filtered_df)

df_filled = df.fillna(df.mean(numeric_only=True))
print("\nDataFrame with Missing Values Filled:")
print(df_filled)

summary_stats = df.describe()
print("\nSummary Statistics:")
print(summary_stats)

filtered_multiple_conditions = df[(df['Age'] > 30) & (df['Salary'] > 50000)]
print("\nFiltered DataFrame (Age > 30 and Salary > 50000):")
print(filtered_multiple_conditions)

grouped_data = df.groupby('Gender')[['Age', 'Salary']].mean()
print("\nGrouped Data by Gender (Mean Age and Salary):")
print(grouped_data)

sorted_df = df.sort_values(by='Salary', ascending=False)
print("\nDataFrame Sorted by Salary (Descending):")
print(sorted_df)

df['Salary_Age_Ratio'] = df['Salary'] / df['Age']
print("\nDataFrame with New Column 'Salary_Age_Ratio':")
print(df)

df.to_csv('modified_data.csv', index=False)






