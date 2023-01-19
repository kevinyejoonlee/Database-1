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


from functions import get_publications
from Connect import Connect

conn = Connect("dcris.txt")
cursor = conn.cursor

rows1 = get_publications(cursor)
rows2 = get_publications(cursor, memberId=33)
rows3 = get_publications(cursor, pubPubType="a")
rows4 = get_publications(cursor, memberId=33, pubPubType="b")

print(rows1) 
print(rows2)
print(rows3)
print(rows4)

conn.close()