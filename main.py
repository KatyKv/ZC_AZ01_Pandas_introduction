# Part1 - repeating lesson with other dataset
import pandas as pd

df = pd.read_csv('digital_literacy_dataset.csv', encoding='utf-8')
print(df.info(), '\n\n')
print(df.head(), '\n\n')
print(df.describe(), '\n\n')
print(df.Employment_Status, '\n\n')
print(df[['Age', 'Education_Level']], '\n\n')
print(df.loc[555], '\n\n')
print(df.loc[555, ['Gender', 'Overall_Literacy_Score']], '\n\n')
print(df[(df.Age > 60) & (df.Overall_Literacy_Score < 50)], '\n\n')
df['Edu_Emp'] = df.Education_Level + df.Employment_Status
print(df.tail(), '\n\n')
df.drop('Overall_Literacy_Score', axis=1, inplace=True)
df.drop(998, axis=0, inplace=True)
print(df.tail(3), '\n\n')
print(df[df.Education_Level.isna()], '\n\n')
df.Education_Level = df.Education_Level.fillna('unknown')
print(df.Education_Level, '\n\n')
df.dropna(inplace=True)
print(df, '\n\n')
group = df.groupby('Gender').Age.count()
print(group)

df.to_csv('digital_literacy_dataset_OUTPUT.csv', index=False)


# Part 2 - Homework

df_dz = pd.read_csv('dz.csv', encoding='utf-8')
print(df_dz, '\n\n')
df_dz.City = df_dz.City.fillna('xxx')
print(df_dz, '\n\n')
group_salary = df_dz.groupby('City').Salary.mean()
print('Средняя зарплата по городам:\n', group_salary)

# Результат вывода по зарплате:
# Средняя зарплата по городам:
#  City
# xxx        41000.0
# Москва    211400.0
# Томск      91250.0

