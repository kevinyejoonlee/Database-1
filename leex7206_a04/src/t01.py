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

from functions import get_table_info
from Connect import Connect

conn = Connect("dcris.txt")
cursor = conn.cursor

rows1 = get_table_info(cursor, "dcris")
rows2 = get_table_info(cursor, "dcris", tableName='broad')


print(rows1)
print(rows2)



conn.close()

# establish the database connection
# get the connection cursor
# pass the cursor to the function being tested
# do something with the function return values
# close the connection
#
# sql = """SELECT ...
# FROM ...
# JOIN ...
# ON ...
# WHERE ...
# ORDER BY ..."""

# sql = "SELECT * FROM broad WHERE broadId = %(broadId)s"
# params = {'broadId': broadId}
# # Execute the query from the cursor with parameter data
# cursor.execute(sql, params)
# rows = cursor.fetchall()


# SELECT * FROM dcris.pub;
# SELECT * FROM dcris.member;
#
# SELECT * FROM dcris.memberNarrow;
# SELECT * FROM dcris.memberBroad;
#
# SELECT * FROM dcris.Narrow;
# SELECT * FROM dcris.Broad;
#
# SELECT * FROM dcris.pubType;
#
# SELECT * FROM dcris.vBroadNarrow;
# SELECT * FROM dcris.vMemberBroad;
# SELECT * FROM dcris.vMemberNarrow;

        