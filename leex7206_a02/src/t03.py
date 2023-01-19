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
from functions import get_broad_counts
from Connect import Connect

conn = Connect("dcris.txt")
cursor = conn.cursor

rows1 = get_broad_counts(cursor)
rows2 = get_broad_counts(cursor, memberId=34)

print(rows1)
print(rows2)
conn.close()