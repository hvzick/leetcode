'''#TODO
Table: Customer

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+
In SQL, id is the primary key column for this table.
Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.


Find the names of the customer that are either:

referred by any customer with id != 2.
not referred by any customer.
Return the result table in any order.
'''

import pandas as pd


def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    customer = customer.loc[(customer['referee_id'] != 2) | (customer['referee_id'].isna()), ['name']]
    return customer

data = [
    [1, 'Will', None], 
    [2, 'Jane', None], 
    [3, 'Alex', 2], 
    [4, 'Bill', None], 
    [5, 'Zack', 1], 
    [6, 'Mark', 2]
]
customer = pd.DataFrame(data, columns=['id', 'name', 'referee_id']).astype({'id':'Int64', 'name':'object', 'referee_id':'Int64'})

print(find_customer_referee(customer))