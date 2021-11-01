import pandas as pd
import numpy as np

from string import Template
template = Template('#' * 10 + ' $string ' + '#' * 10)

"""
Створити програму, яка за даними файлу відповідно до варіантів
лабораторної No2, виконує наступні завдання:

1. Виділити один зі стовпців (на вибір) з файлу як об’єкт Series. Задати
назви індексів цього об’єкту. Виділити підмасиви за допомогою прямої
та непрямої індексацій.
2. До об’єкту DataFrame, в який записано вміст файлу, додати новий
стовпець, що є результатом операцій над іншими стовпцями.
3. Створити ієрархічну індексацію (не менше двох рівнів) для цього об’єкту
DataFrame. Продемонструвати виділення підмасивів за певною ознакою
з використанням мультиіндексації. Продемонструвати розрахунок
результату операції агрегування з використанням ієрархічних рівнів.
4. Створити декілька власних об’єктів DataFrame за такою ж тематикою, що
й файл. Наприклад, якщо тема файлу – жаби, можна створити об’єкти,
що містять розміри жаб, вагу, стать, кількість особин в популяції і т.д.
Використати описані в теоретичних відомостях параметри методу merge
для різних видів злиття даних цих об’єктів.
"""

df = pd.read_csv('https://raw.githubusercontent.com/mezgoodle/ad_labs/master/data/Crime.csv')
print(template.substitute(string='Dataframe'))
print(df)

series = pd.Series(df['CrimeRate'], index=[i for i in range(0 + 3, len(df['CrimeRate']) + 3)])
print(template.substitute(string='Show indexes'))
print(series.loc[3:5])
print(series.iloc[3:5])

print(template.substitute(string='Create new column'))
df['WageRatio'] = df['Wage'] / df['StateSize']
print(df['WageRatio'])

print(template.substitute(string='Create hierarchical indexes'))
first_indexes = pd.Series(np.arange(0, 7))
second_indexes = pd.Series(['I', 'II', 'III'])
multi_index = pd.MultiIndex.from_product([['A', 'B'], second_indexes, first_indexes])
df = df[:-5]
df.set_index([multi_index], inplace=True)
print(df)
print(df.mean(level=1))
print(df.max(level=2))
crime_rate_series = pd.Series(df['CrimeRate'])
print(crime_rate_series[crime_rate_series > 100])
print(crime_rate_series[:, 'II', :])
print(crime_rate_series['A', 'II'])

print(template.substitute(string='Merge dataframes'))
a_df = pd.DataFrame({'CrimeRate': df['CrimeRate'], 'Youth': df['Youth'], 'Males': df['Males']})
b_df = pd.DataFrame({'CrimeRate_1': df['CrimeRate'], 'Wage': df['Wage'], 'Youth': df['Youth']})
c_df = pd.merge(a_df, b_df, left_on='CrimeRate', right_on='CrimeRate_1',
                suffixes=('_left', '_right')).drop('CrimeRate_1', axis=1)
print(c_df)
b_df = pd.DataFrame({'CrimeRate_1': df['CrimeRate'], 'Wage': df['Wage'], 'Youth': df['Youth'], 'Males': df['Males10']})
c_df = pd.merge(a_df, b_df, how='inner', suffixes=('_left', '_right'))
print(c_df)
