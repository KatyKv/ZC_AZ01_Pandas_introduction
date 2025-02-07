# Repeating lesson

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import date_range
import random

df = pd.read_csv('../ZC_AZ01_Pandas_introduction/digital_literacy_dataset.csv', encoding='utf-8')

# Descriptive statistics
print(df.describe())
print()
print('Возраст:')
print(df.Age.mean(), '- средний')
print(df.Age.median(), '- медианный')
print(df.Age.mode()[0], '- мода')
print(df.Age.std(), '- стандартное отклонение')

# Time Series
print('\n\nВременные ряды')
dates = date_range(start='2024-08-25', periods=15, freq='D')
values = np.random.rand(15)
df = pd.DataFrame({'Date': dates, 'Values': values})
df.set_index('Date', inplace=True)
print('\nДатафрейм с днями:')
print(df)
# ресэмплирование: дни в месяцы по среднему
print('\nДатафрейм с месяцами и средним значением (последний день месяца пишется):')
month = df.resample('ME').mean()
print(month)

# Outliers
values = [random.randint(1, 20) for _ in range(30)]
values.append(99)
df = pd.DataFrame({'value': values})
df.value.hist(bins=30)
plt.show()
df.boxplot(column='value')
plt.show()
print(df.describe())
q1 = df.value.quantile(0.25)
q3 = df.value.quantile(0.75)
IQR = q3 - q1
down_bound = q1 - 1.5 * IQR
up_bound = q3 + 1.5 * IQR
df_new = df[(df.value > down_bound) & (df.value < up_bound)]
df_new.boxplot(column='value')
plt.show()

# categorical data
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'gender': ['female', 'male', 'male', 'male', 'female'],
    'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
}
df = pd.DataFrame(data)
print('\n\nТип столбца "gender":', df.gender.dtype)
print('Тип столбца "department":', df.department.dtype)
df.gender = df.gender.astype('category')
df.department = df.department.astype('category')
print('\nПосле преобразования в категории:')
print('Тип столбца "gender":', df.gender.dtype)
print('Категории:', df.gender.cat.categories)
print('Тип столбца "department":', df.department.dtype)
print('Категории:', df.department.cat.categories)
print('Категории в виде чисел:')
print(df.department.cat.codes)
df.department = df.department.cat.add_categories(['Finance', 'IT'])
print('department с новыми категориями:\n', df.department.cat.categories)
df.department = df.department.cat.remove_categories(['Finance', 'Engineering'])
print('Категории department, после удаления "Finance", "Engineering":\n', df.department.cat.categories)
print('В удалённых категориях NaN:\n', df)
