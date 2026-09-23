'''#TODO
Table: Courses

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+
(student, class) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the name of a student and the class in which they are enrolled.


Write a solution to find all the classes that have at least five students.

Return the result table in any order.
'''

import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    x = courses.groupby('class')['student'].count().reset_index()
    x = x.sort_values(by='student', ascending=False)
    x = x.loc[x['student'] >= 5, ['class']]
    return x

data = [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'], ['E', 'Math'], ['F', 'Computer'], ['G', 'Math'], ['H', 'Math'], ['I', 'Math']]
courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student':'object', 'class':'object'})

print(find_classes(courses))