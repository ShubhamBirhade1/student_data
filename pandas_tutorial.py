import pandas as pd

#df = pd.read_csv('F:/student_data-main/student_data.csv')

df = pd.read_csv('F:/student_data-main/student_data.csv', names=['student_name', 'age', 'city', 'chemistry', 'physics', 'maths'])

min_age = df['age'].min()

print('min_age=',min_age)

max_age = df['age'].max()
print('max_age=', max_age)

avg_age = df['age'].mean()
print('avg_age=', avg_age)