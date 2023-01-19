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

from functions import get_narrow_member_counts
from Connect import Connect

conn = Connect("dcris.txt")
cursor = conn.cursor



rows1 = get_narrow_member_counts(cursor)
rows2 = get_narrow_member_counts(cursor, narrowId=7)



print(rows1) 
print(rows2)

# establish the database connection
# get the connection cursor
# pass the cursor to the function being tested
# do something with the function return values
# close the connection



conn.close()