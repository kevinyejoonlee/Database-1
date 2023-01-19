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


def get_broad(cursor, broadId=None):
    """
    -------------------------------------------------------
    Queries the broad table.
    Use: rows = get_broad(cursor)
    Use: rows = get_broad(cursor, broadId=v)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        broadId - a broad ID (int)
    Returns:
        rows - (list of broad table data)
            if broadId is not None:
                rows matching broadId
            else:
                the entire broad table
            Sorted by broad description
    -------------------------------------------------------
    """
    
    if broadId is not None:
        # Define a SQL query
        sql = "SELECT * FROM broad WHERE broadId = %(broadId)s"
        params = {'broadId': broadId}
        # Execute the query from the cursor with parameter data
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        
    else: #return the entire broad table BUT YOU HAVE TO SORT
        sql = "select * from broad ORDER BY broadDesc"
        cursor.execute(sql)
        rows = cursor.fetchall()


    
    return rows
    
def get_publications(cursor, memberId=None, pubPubType=None):
    """
    -------------------------------------------------------
    Queries the pub table.
    Use: rows = get_publications(cursor)
    Use: rows = get_publications(cursor, memberId=v1)
    Use: rows = get_publications(cursor, pubPubType=v2)
    Use: rows = get_publications(cursor, memberId=v1, pubPubType=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        memberId - a member ID number (int)
        pubPubType - a publication type (str)
    Returns:
        rows - (list of pub table data)
            if memberId and/or pubPubType are not None:
                rows matching memberId and/or pubPubType
            else:
                the entire pub table
            Sorted by publication title
    -------------------------------------------------------
    """

    if (memberId is not None) and (pubPubType is not None):
        sql = "SELECT * FROM pub WHERE pubPubType = %(pubType)s AND pubMemberId = %(memberId)s"
        
    elif (memberId is not None) and (pubPubType is None):
        sql = "SELECT * FROM pub WHERE pubMemberId = %(memberId)s"

    elif (memberId is None) and (pubPubType is not None):
        sql = "SELECT * FROM pub WHERE pubPubType = %(pubType)s"
        
    else: # the entire pub table sorted by the publication title
        sql = "select * from pub ORDER BY pubTitle"

      
    params = {'pubType': pubPubType, 'memberId': memberId}
    cursor.execute(sql, params)
    rows = cursor.fetchall()
    

    return rows
    
def get_member_broad(cursor, memberId=None, broadId=None):
    """
    -------------------------------------------------------
    Queries the vMemberBroad view.
    Use: rows = get_member_broad(cursor)
    Use: rows = get_member_broad(cursor, memberId=v1)
    Use: rows = get_member_broad(cursor, broadId=v2)
    Use: rows = get_member_broad(cursor, memberId=v1, broadId=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        memberId - a member ID number (int)
        broadId - a broad ID number (int)
    Returns:
        rows - (list of vMemberBroad view data)
            if memberId and/or broadId are not None:
                rows matching memberId and/or broadId
            else:
                the entire vMemberBroad view
            Sorted by member last name, first name, and broad description
    -------------------------------------------------------
    """

    # ORDER BY  memberSurname, memberForename, broadDesc;
    # SELECT CONCAT
    # ex "SELECT CONCAT(last_name, ', ', first_name) AS name FROM member"
    

    if (memberId is not None) and (broadId is not None):
        sql = "SELECT * FROM vMemberBroad WHERE memberId = %(memberId)s AND broadId = %(broadId)s"
        
    elif (memberId is not None) and (broadId is None):
        sql = "SELECT * FROM vMemberBroad WHERE memberId = %(memberId)s"

    elif (memberId is None) and (broadId is not None):
        sql = "SELECT * FROM vMemberBroad WHERE broadId = %(broadId)s"
        
    else: # the entire pub table sorted by the publication title
        sql = "select * from vMemberBroad ORDER BY memberSurname, memberForename, broadDesc"
 
      
    params = {'memberId': memberId, 'broadId': broadId}
    cursor.execute(sql, params)
    rows = cursor.fetchall()
    
 
    return rows

    
def get_expertises(cursor, broad=None, narrow=None):
    """
    -------------------------------------------------------
    Queries the vBroadNarrow view.
    Use: rows = get_expertises(cursor)
    Use: rows = get_expertises(cursor, broad=v1)
    Use: rows = get_expertises(cursor, narrow=v2)
    Use: rows = get_expertises(cursor, broad=v1, narrow=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        broad - a partial broad expertise description (str)
        narrow - a partial narrow expertise description (str)
    Returns:
        rows - (list of vBroadNarrow view data)
            if broad and/or narrow are not None:
                rows containing broad and/or narrow
            else:
                the entire vBroadNarrow view
            Sorted by broad description, narrow broad description
    -------------------------------------------------------
    """
    
    #ORDER BY  broadDesc, narrowDesc;
    
 
    if (broad is not None) and (narrow is not None):
        sql = "SELECT * FROM vBroadNarrow WHERE broadDesc LIKE %(broadDesc)s AND narrowDesc LIKE %(narrowDesc)s"
        
    elif (broad is not None) and (narrow is None):
        sql = "SELECT * FROM vBroadNarrow WHERE broadDesc LIKE %(broadDesc)s"

    elif (broad is None) and (narrow is not None):
        sql = "SELECT * FROM vBroadNarrow WHERE narrowDesc LIKE %(narrowDesc)s"
        
    else: # the entire pub table sorted by the publication title
        sql = "select * from vBroadNarrow ORDER BY broadDesc, narrowDesc"

      
    params = {'broadDesc': broad, 'narrowDesc': narrow}
    cursor.execute(sql, params)
    rows = cursor.fetchall()
    

    return rows
    
