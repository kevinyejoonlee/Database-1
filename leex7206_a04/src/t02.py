"""
-------------------------------------------------------
functions
-------------------------------------------------------
Author: Kevin Lee
ID:     210872060
Email:  leex7206@mylaurier.ca
__updated__ = '2022-01-15'
-------------------------------------------------------
"""


from functions import get_column_info
from Connect import Connect

conn = Connect("dcris.txt")
cursor = conn.cursor

rows1 = get_column_info(cursor, "dcris")
rows2 = get_column_info(cursor, "dcris", tableName='member')

print(rows1) 
print(rows2)


conn.close()