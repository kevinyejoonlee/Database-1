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

from functions import get_broad 
from Connect import Connect



conn = Connect("dcris.txt")
cursor = conn.cursor


rowsAll = get_broad(cursor)
rows1 = get_broad(cursor, broadId=1)
rows2 = get_broad(cursor, broadId=7)

print(rowsAll) 
print(rows1)
print(rows2)

# establish the database connection
# get the connection cursor
# pass the cursor to the function being tested
# do something with the function return values
# close the connection



conn.close()