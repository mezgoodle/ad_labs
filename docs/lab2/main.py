import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

from string import Template

"""
Варіант 7.

Файл Crime.csv.

1. Знайти середнє та медіанне значення витрат на поліцію.
2. Перевірити чи нормальні витрати на поліцію.
3. Перевірити чи в південних штатах вища частота злочинів.
4. Побудувати лінійну регресійну модель залежності частоти злочинів
від доходу.
"""

template = Template('#' * 10 + ' $string ' + '#' * 10)
alpha = 0.05

# get data
df = pd.read_csv('https://raw.githubusercontent.com/mezgoodle/ad_labs/master/data/Crime.csv')
crime_rate = df['CrimeRate']
crime_rate_10 = df['CrimeRate10']
expenditure = df['ExpenditureYear0']
expenditure_10 = df['ExpenditureYear10']
wage = df['Wage']
wage_10 = df['Wage10']

print(template.substitute(string='Dataframe'))
print(df)

print(template.substitute(string='Mean and median values for expenditure'))
print(crime_rate.mean())
print(crime_rate.median())
print(template.substitute(string='Mean and median values for expenditure after 10 years'))
print(crime_rate_10.mean())
print(crime_rate_10.median())

print(template.substitute(string='Test if sample differs from a normal distribution'))
_, p = stats.normaltest(expenditure)
print(p > alpha)
_, p = stats.normaltest(expenditure_10)
print(p > alpha)
plt.hist(expenditure, color='green', edgecolor='green', bins=8)
plt.show()

print(template.substitute(string='Test if crime rate in southern states is greater than in the non-southern'))
southern = df.query('Southern==1').CrimeRate
not_southern = df.query('Southern==0').CrimeRate
_, p = stats.ttest_ind(southern, not_southern, alternative='less')
print(p > alpha)

print(template.substitute(string='Build linear regression model for two sets'))
(slope, intercept, r_value, p_value, stderr) = stats.linregress(wage, crime_rate)
print(f'y = {intercept} + {slope}x + e')
# Plot linear regression line.
wage_pred = intercept + slope*wage
plt.scatter(wage, crime_rate, color='red', marker='o', label='Original data')
plt.plot(wage, wage_pred, color='green', label='Fitted line')
# Set labels
plt.legend(loc='best')
plt.xlabel('wage')
plt.ylabel('crime_rate')
plt.show()
