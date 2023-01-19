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


from functions import get_expertises
from Connect import Connect

conn = Connect("dcris.txt")
cursor = conn.cursor



rows1 = get_expertises(cursor)
rows2 = get_expertises(cursor, broad="Civil-Military Relations")
rows3 = get_expertises(cursor, narrow="Counter-Proliferation")
rows4 = get_expertises(cursor, broad="Arms Control and Non-Proliferation Studies", narrow="Confidence Building Measures")

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