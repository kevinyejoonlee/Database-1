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

from functions import get_key_info
from Connect import Connect

conn = Connect("dcris.txt")
cursor = conn.cursor



rows1 = get_key_info(cursor, 'dcris')
rows2 = get_key_info(cursor, 'dcris', tableName='pub')
rows3 = get_key_info(cursor, 'dcris', refTableName='pubType')
rows4 = get_key_info(cursor, 'dcris', tableName='pub', refTableName='pubType')



print(rows1) 
print(rows2)
print(rows3) 
print(rows4)

# establish the database connection
# get the connection cursor
# pass the cursor to the function being tested
# do something with the function return values
# close the connection



conn.close()