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
from functions import get_publication_counts
from Connect import Connect

conn = Connect("dcris.txt")
cursor = conn.cursor

rows1 = get_publication_counts(cursor)
rows2 = get_publication_counts(cursor, memberId=34)
rows3 = get_publication_counts(cursor, pubType='b')
rows4 = get_publication_counts(cursor, memberId=1, pubType='b')

print(rows1)
print(rows2)
print(rows3)
print(rows4)

conn.close()