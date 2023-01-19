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
from functions import get_all_expertises
from Connect import Connect

conn = Connect("dcris.txt")
cursor = conn.cursor




rows1 = get_all_expertises(cursor)
rows2 = get_all_expertises(cursor, memberId=34)

print(rows1)
print(rows2)




conn.close()