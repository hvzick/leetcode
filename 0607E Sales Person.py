'''#TODO
Table: SalesPerson

+-----------------+---------+
| Column Name     | Type    |
+-----------------+---------+
| sales_id        | int     |
| name            | varchar |
| salary          | int     |
| commission_rate | int     |
| hire_date       | date    |
+-----------------+---------+
sales_id is the primary key (column with unique values) for this table.
Each row of this table indicates the name and the ID of a salesperson alongside their salary, commission rate, and hire date.


Table: Company

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| com_id      | int     |
| name        | varchar |
| city        | varchar |
+-------------+---------+
com_id is the primary key (column with unique values) for this table.
Each row of this table indicates the name and the ID of a company and the city in which the company is located.


Table: Orders

+-------------+------+
| Column Name | Type |
+-------------+------+
| order_id    | int  |
| order_date  | date |
| com_id      | int  |
| sales_id    | int  |
| amount      | int  |
+-------------+------+
order_id is the primary key (column with unique values) for this table.
com_id is a foreign key (reference column) to com_id from the Company table.
sales_id is a foreign key (reference column) to sales_id from the SalesPerson table.
Each row of this table contains information about one order. This includes the ID of the company, the ID of the salesperson, the date of the order, and the amount paid.


Write a solution to find the names of all the salespersons who did not have any orders related to the company with the name "RED".

Return the result table in any order.
'''

import pandas as pd


def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    a = company.loc[(company['name'] == 'RED'), ['com_id']]
    print(a)
    c = orders.loc[(orders['com_id'].isin(a['com_id'])), ['sales_id']]
    x = sales_person[~sales_person['sales_id'].isin(c['sales_id'])][['name']]
    return x

data = [
    [1, 'John', 100000, 6, '4/1/2006'], 
    [2, 'Amy', 12000, 5, '5/1/2010'], 
    [3, 'Mark', 65000, 12, '12/25/2008'], 
    [4, 'Pam', 25000, 25, '1/1/2005'], 
    [5, 'Alex', 5000, 10, '2/3/2007']
]
sales_person1 = pd.DataFrame(data, columns=['sales_id', 'name', 'salary', 'commission_rate', 'hire_date']).astype({'sales_id':'Int64', 'name':'object', 'salary':'Int64', 'commission_rate':'Int64', 'hire_date':'datetime64[ns]'})
data = [
    [1, 'RED', 'Boston'], 
    [2, 'ORANGE', 'New York'], 
    [3, 'YELLOW', 'Boston'], 
    [4, 'GREEN', 'Austin']
]
company = pd.DataFrame(data, columns=['com_id', 'name', 'city']).astype({'com_id':'Int64', 'name':'object', 'city':'object'})
data = [
    [1, '1/1/2014', 3, 4, 10000], 
    [2, '2/1/2014', 4, 5, 5000], 
    [3, '3/1/2014', 1, 1, 50000], 
    [4, '4/1/2014', 1, 4, 25000]
]
orders = pd.DataFrame(data, columns=['order_id', 'order_date', 'com_id', 'sales_id', 'amount']).astype({'order_id':'Int64', 'order_date':'datetime64[ns]', 'com_id':'Int64', 'sales_id':'Int64', 'amount':'Int64'})

print(sales_person(sales_person1, company, orders))
