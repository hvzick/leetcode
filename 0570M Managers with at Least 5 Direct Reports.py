'''#TODO
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.


Write a solution to find managers with at least five direct reports.

Return the result table in any order.

The result format is in the following example.



Example 1:

Input: 
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
Output: 
+------+
| name |
+------+
| John |
+------+
'''

import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    x = employee['managerId'].value_counts().reset_index()
    r = x['managerId'].loc[(x['count'] >= 5)].tolist()
    x = employee.loc[(employee['id'].isin(r)), ['name']]
    return x

data = [
    [101, 'John',  'A', None], 
    [102, 'Dan',   'A', 101], 
    [103, 'James', 'A', 101], 
    [104, 'Amy',   'A', 101], 
    [105, 'Anne',  'A', 101], 
    [106, 'Ron',   'B', 101],
    [107, 'Tom',   'A', 102], 
    [108, 'Tommy', 'A', 102], 
    [109, 'Peter', 'A', 102], 
    [110, 'Dong',  'B', 102]
]
employee = pd.DataFrame(data, columns=['id', 'name', 'department', 'managerId']).astype({'id':'Int64', 'name':'object', 'department':'object', 'managerId':'Int64'})
print(find_managers(employee))