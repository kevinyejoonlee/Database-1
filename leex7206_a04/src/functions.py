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

def get_table_info(cursor, tableSchema, tableName=None):
    """
    -------------------------------------------------------
    Queries information_schema.TABLES for metadata.
    Use: rows = get_table_info(cursor, tableSchema)
    Use: rows = get_table_info(cursor, tableSchema, tableName=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        tableSchema - the database table schema (str)
        tableName - a table name (str)
    Returns:
        rows - (list of the TABLE_NAME, TABLE_TYPE, TABLE_ROWS,
            and TABLE_COMMENT fields data)
            if tableName is not None:
                rows containing tableName
            else:
                all TABLES rows
            Sorted by TABLE_NAME, TABLE_TYPE
    -------------------------------------------------------
    """
    if tableName is None:
        sql = """
        SELECT TABLE_NAME, TABLE_TYPE, TABLE_ROWS, TABLE_COMMENT
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = %(tableSchema)s
ORDER BY TABLE_NAME,TABLE_TYPE, TABLE_ROWS
        
"""

    else:
        sql = """
        SELECT TABLE_NAME, TABLE_TYPE, TABLE_ROWS, TABLE_COMMENT
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = %(tableSchema)s AND TABLE_NAME = %(tableName)s
ORDER BY TABLE_NAME,TABLE_TYPE, TABLE_ROWS
"""
    
    params = {'tableSchema': tableSchema,'tableName': tableName}
    cursor.execute(sql, params)
    rows = cursor.fetchall()


    return rows
    

    
def get_column_info(cursor, tableSchema, tableName=None):
    """
    -------------------------------------------------------
    Queries information_schema.COLUMNS for metadata.
    Use: rows = get_column_info(cursor, tableSchema)
    Use: rows = get_column_info(cursor, tableSchema, tableName=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        tableSchema - the database table schema (str)
        tableName - a table name (str)
    Returns:
        rows - (list of the TABLE_NAME, COLUMN_NAME, IS_NULLABLE,
            and DATA_TYPE fields data)
            if tableName is not None:
                rows containing tableName
            else:
                all COLUMNS rows
            Sorted by TABLE_NAME, COLUMN_NAME
    -------------------------------------------------------
    """
    
    if tableName is None:
        sql = """
        SELECT TABLE_NAME, COLUMN_NAME, IS_NULLABLE, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = %(tableSchema)s
ORDER BY TABLE_NAME, COLUMN_NAME
"""

    else:
        sql = """
        SELECT TABLE_NAME, COLUMN_NAME, IS_NULLABLE, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = %(tableSchema)s AND TABLE_NAME = %(tableName)s
ORDER BY TABLE_NAME, COLUMN_NAME

"""
   
    
    params = {'tableSchema': tableSchema,'tableName': tableName}
    cursor.execute(sql, params)
    rows = cursor.fetchall()


    return rows
    
def get_constraint_info(cursor, tableSchema, constraintType=None):
    """
    -------------------------------------------------------
    Queries information_schema.TABLE_CONSTRAINTS for metadata.
    Use: rows = get_constraint_info(cursor, tableSchema)
    Use: rows = get_constraint_info(cursor, tableSchema, constraintType=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        tableSchema - the database table schema (str)
        constraintType - a database constraint type (str)
    Returns:
        rows - (list of the CONSTRAINT_NAME, TABLE_NAME,
            and CONSTRAINT_TYPE fields data)
            if constraintType is not None:
                rows containing constraintType
            else:
                all TABLE_CONSTRAINTS rows
            Sorted by CONSTRAINT_NAME, TABLE_NAME
    -------------------------------------------------------
    """
    if constraintType is None:
        sql = """SELECT CONSTRAINT_NAME, TABLE_NAME, CONSTRAINT_TYPE
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_SCHEMA = %(tableSchema)s
ORDER BY CONSTRAINT_NAME, TABLE_NAME
"""

    else:
        sql = """SELECT CONSTRAINT_NAME, TABLE_NAME, CONSTRAINT_TYPE
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_SCHEMA = %(tableSchema)s AND CONSTRAINT_TYPE = %(constraintType)s
ORDER BY CONSTRAINT_NAME, TABLE_NAME
"""
    
    
    params = {'tableSchema': tableSchema, 'constraintType': constraintType}
    cursor.execute(sql, params)
    rows = cursor.fetchall()

    return rows
    
def get_foreign_key_info(cursor, constraintSchema, tableName=None, refTableName=None):
    """
    -------------------------------------------------------
    Queries information_schema.REFERENTIAL_CONSTRAINTS for metadata.
    Use: rows = get_foreign_key_info(cursor, constraintSchema)
    Use: rows = get_foreign_key_info(cursor, constraintSchema, tableName=v1)
    Use: rows = get_foreign_key_info(cursor, constraintSchema, refTableName=v2)
    Use: rows = get_foreign_key_info(cursor, constraintSchema, tableName=v1, refTableName=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        constraintSchema - the database constraint schema (str)
        tableName - a table name (str)
        refTableName - a table name (str)
    Returns:
        rows - (list of the CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE,
            TABLE_NAME, and REFERENCED_TABLE_NAME fields data)
            if tableName and/or refTableName are not None:
                rows containing tableName and/or refTableName
            else:
                all REFERENTIAL_CONSTRAINTS rows
            Sorted by CONSTRAINT_NAME, TABLE_NAME, REFERENCED_TABLE_NAME
    -------------------------------------------------------
    """
    
    if tableName is None and refTableName is None :
        sql = """
        SELECT CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE,TABLE_NAME, REFERENCED_TABLE_NAME
FROM INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS
WHERE CONSTRAINT_SCHEMA = %(constraintSchema)s
ORDER BY CONSTRAINT_NAME, TABLE_NAME, REFERENCED_TABLE_NAME
        
"""

    elif tableName is not None and refTableName is None :
        sql = """
        SELECT CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE,TABLE_NAME, REFERENCED_TABLE_NAME
FROM INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS
WHERE CONSTRAINT_SCHEMA = %(constraintSchema)s AND TABLE_NAME = %(tableName)s
ORDER BY CONSTRAINT_NAME, TABLE_NAME, REFERENCED_TABLE_NAME    
"""
    elif tableName is  None and refTableName is not None :
            sql = """
            SELECT CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE,TABLE_NAME, REFERENCED_TABLE_NAME
FROM INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS
WHERE CONSTRAINT_SCHEMA = %(constraintSchema)s AND REFERENCED_TABLE_NAME = %(refTableName)s
ORDER BY CONSTRAINT_NAME, TABLE_NAME, REFERENCED_TABLE_NAME
           
        
"""

    else:
        sql = """
         SELECT CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE,TABLE_NAME, REFERENCED_TABLE_NAME
FROM INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS
WHERE CONSTRAINT_SCHEMA = %(constraintSchema)s AND REFERENCED_TABLE_NAME = %(refTableName)s AND TABLE_NAME = %(tableName)s
ORDER BY CONSTRAINT_NAME, TABLE_NAME, REFERENCED_TABLE_NAME
"""
    
    
    params = {'constraintSchema': constraintSchema,'refTableName': refTableName, 'tableName':tableName}
    cursor.execute(sql, params)
    rows = cursor.fetchall()

    return rows
    
    
def get_key_info(cursor, constraintSchema, tableName=None, refTableName=None):
    """
    -------------------------------------------------------
    Queries information_schema.KEY_COLUMN_USAGE for metadata.
    Use: rows = get_key_info(cursor, constraintSchema)
    Use: rows = get_key_info(cursor, constraintSchema, tableName=v1)
    Use: rows = get_key_info(cursor, constraintSchema, refTableName=v2)
    Use: rows = get_key_info(cursor, constraintSchema, tableName=v1, refTableName=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        constraintSchema - the database constraint schema (str)
        tableName - a table name (str)
        refTableName - a table name (str)
    Returns:
        rows - (list of the CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME,
            REFERENCED_TABLE_NAME, and REFERENCED_COLUMN_NAME fields data)
            if tableName and/or refTableName are not None:
                rows containing tableName and/or refTableName
            else:
                all KEY_COLUMN_USAGE rows
            Sorted by TABLE_NAME, COLUMN_NAME
    -------------------------------------------------------
    """
    
    if tableName is None and refTableName is None :
        sql = """
        SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE CONSTRAINT_SCHEMA = %(constraintSchema)s
ORDER BY TABLE_NAME, COLUMN_NAME     
"""

    elif tableName is not None and refTableName is None :
        sql = """
        SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE CONSTRAINT_SCHEMA = %(constraintSchema)s AND TABLE_NAME = %(tableName)s
ORDER BY TABLE_NAME, COLUMN_NAME     
"""
    elif tableName is  None and refTableName is not None :
            sql = """
            SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE CONSTRAINT_SCHEMA = %(constraintSchema)s AND REFERENCED_TABLE_NAME = %(refTableName)s
ORDER BY TABLE_NAME, COLUMN_NAME
"""
    else:
        sql = """
         SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE CONSTRAINT_SCHEMA = %(constraintSchema)s AND TABLE_NAME = %(tableName)s AND REFERENCED_TABLE_NAME = %(refTableName)s
ORDER BY TABLE_NAME, COLUMN_NAME  
"""
    
    
    params = {'constraintSchema': constraintSchema,'refTableName': refTableName, 'tableName':tableName}
    cursor.execute(sql, params)
    rows = cursor.fetchall()

    return rows