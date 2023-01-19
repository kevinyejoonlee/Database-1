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

from Connect import Connect

try:
    # Connect to the DCRIS database with an option file
    conn = Connect("dcris.txt")
    # Get the connection cursor object
    cursor = conn.cursor
    # Define a SQL query
    sql = "SELECT * FROM broad"
    # Execute the query from the connection cursor
    cursor.execute(sql)
    # Print the column names from the query result
    print("Columns:")
    print(cursor.column_names)
    # Get and print the contents of the query results (raw results)
    rows = cursor.fetchall()
    print(f"Row count: {cursor.rowcount}")

    print("Data:")
    for row in rows:
        print(row)
    # Close the Connect object
    conn.close()
except Exception as e:
    print(str(e))
    
#
#     Columns:
# ('broadId', 'broadDesc')
#
# Row count: 19
#
# Data:
# (7, 'Arms Control and Non-Proliferation Studies')
# (13, 'Civil-Military Relations')
# (11, 'Defence Management and Policy')
# ...
# (16, 'Weapons Systems')