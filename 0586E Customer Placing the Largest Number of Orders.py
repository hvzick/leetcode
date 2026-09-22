'''#TODO
Table: Orders

+-----------------+----------+
| Column Name     | Type     |
+-----------------+----------+
| order_number    | int      |
| customer_number | int      |
+-----------------+----------+
order_number is the primary key (column with unique values) for this table.
This table contains information about the order ID and the customer ID.
 

Write a solution to find the customer_number for the customer who has placed the largest number of orders.

The test cases are generated so that exactly one customer will have placed more orders than any other customer.

The result format is in the following example.
'''

import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    x = orders.groupby('customer_number')['order_number'].count().reset_index()
    m = x['order_number'].max()
    x = x[x['order_number'] == m][['customer_number']]
    return x

data = [
    [1, 1], 
    [2, 2], 
    [3, 3], 
    [4, 3]
]
orders = pd.DataFrame(data, columns=['order_number', 'customer_number']).astype({'order_number':'Int64', 'customer_number':'Int64'})

print(largest_orders(orders))