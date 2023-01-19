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


from functions import get_member_broad
from Connect import Connect

conn = Connect("dcris.txt")
cursor = conn.cursor



rows1 = get_member_broad(cursor)
rows2 = get_member_broad(cursor, memberId=1)
rows3 = get_member_broad(cursor, broadId=7)
rows4 = get_member_broad(cursor, memberId=2, broadId=7)

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