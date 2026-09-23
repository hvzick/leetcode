'''#TODO
Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.


Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).
'''

import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset='salary', keep='last').sort_values(by='salary', ascending=False)
    print(employee)
    if len(employee) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    else:
        employee = employee.iloc[1:2].rename(columns={'salary':'SecondHighestSalary'})
    return employee[['SecondHighestSalary']]

data = [
    [1, 100],
    [2, 100]
]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})

print(second_highest_salary(employee))