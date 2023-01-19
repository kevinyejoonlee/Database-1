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

def get_member_publications(cursor, pubTitle=None, pubType=None):
    """
    -------------------------------------------------------
    Queries the pub and member tables.
    Use: rows = get_member_publications(cursor)
    Use: rows = get_member_publications(cursor, pubTitle=v1)
    Use: rows = get_member_publications(cursor, pubType=v2)
    Use: rows = get_member_publications(cursor, pubTitle=v1, pubType=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        pubTitle - a partial pubTitle (str)
        pubType - a single letter publication type (str)
    Returns:
        rows - (list of member's last name, member's first
            name, the title of a publication, and the full publication
            type (i.e. 'article' rather than 'a') data)
            if pubTitle and/or pubType are not None:
                rows containing pubTitle and/or pubType
            else:
                all member and publication rows
            Sorted by last name, first name, publication title
    -------------------------------------------------------
    """
    #pubPubType
    #'article' rather than 'a'
    

    if (pubTitle is not None) and (pubType is not None):
        sql = """SELECT B.memberSurname, B.memberForename, A.pubTitle, C.pubTypeDesc
    FROM pub AS A
    INNER JOIN member AS B
    ON A.pubMemberId = B.memberId
    INNER JOIN pubType AS C
    ON A.pubPubType = C.pubType
WHERE A.pubTitle = %(pubTitle)s AND A.pubPubType = %(pubPubType)s
 ORDER BY B.memberSurname, B.memberForename, A.pubTitle
"""


    elif (pubTitle is not None) and (pubType is None):
        sql = """SELECT B.memberSurname, B.memberForename, A.pubTitle, C.pubTypeDesc
    FROM pub AS A
    INNER JOIN member AS B
    ON A.pubMemberId = B.memberId
    INNER JOIN pubType AS C
    ON A.pubPubType = C.pubType
    WHERE A.pubTitle = %(pubTitle)s
 ORDER BY B.memberSurname, B.memberForename, A.pubTitle
"""

    elif (pubTitle is None) and (pubType is not None):
        sql = """SELECT B.memberSurname, B.memberForename, A.pubTitle, C.pubTypeDesc
    FROM pub AS A
    INNER JOIN member AS B
    ON A.pubMemberId = B.memberId
    INNER JOIN pubType AS C
    ON A.pubPubType = C.pubType
    WHERE A.pubPubType = %(pubPubType)s
 ORDER BY B.memberSurname, B.memberForename, A.pubTitle
"""

    else:
       
        sql = """SELECT B.memberSurname, B.memberForename, A.pubTitle, C.pubTypeDesc
    FROM pub AS A
    INNER JOIN member AS B
    ON A.pubMemberId = B.memberId
    INNER JOIN pubType AS C
    ON A.pubPubType = C.pubType
 ORDER BY B.memberSurname, B.memberForename, A.pubTitle"""
   
    
    params = {'pubTitle': pubTitle, 'pubPubType': pubType}
    cursor.execute(sql, params)
    rows = cursor.fetchall()


    return rows


    
    
def get_publication_counts(cursor, memberId=None, pubType=None):
    """
    -------------------------------------------------------
    Queries the pub and member tables.
    Use: rows = get_publication_counts(cursor)
    Use: rows = get_publication_counts(cursor, memberId=v1)
    Use: rows = get_publication_counts(cursor, pubType=v2)
    Use: rows = get_publication_counts(cursor, memberId=v1, pubType=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        memberId - a member ID number (int)
        pubType - a publication type (str)
    Returns:
        rows - (list of member's last name, member's first
            name, and the number of publications of type
            pubType data)
            if memberId or pubType is not None:
                rows containing memberId and/or pubType
            else:
                all member names and publication counts
            Sorted by last name, first name
    -------------------------------------------------------
    """
    
    if (memberId is not None) and (pubType is not None):
        sql = """ 
        SELECT B.memberSurname, B.memberForename, COUNT(A.pubPubType)
    FROM pub AS A
    RIGHT JOIN member AS B
    ON A.pubMemberId = B.memberId AND A.pubPubType = %(pubPubType)s
GROUP BY B.memberId
HAVING B.memberId = %(memberId)s
ORDER BY B.memberSurname, B.memberForename
"""


    elif (memberId is not None) and (pubType is None):
        sql = """SELECT B.memberSurname, B.memberForename, COUNT(A.pubPubType)
    FROM pub AS A
    RIGHT JOIN member AS B
    ON A.pubMemberId = B.memberId
    WHERE memberId = %(memberId)s
GROUP BY B.memberId
ORDER BY B.memberSurname, B.memberForename
"""

    elif (memberId is None) and (pubType is not None):
        sql = """
        SELECT B.memberSurname, B.memberForename, COUNT(A.pubPubType)
    FROM pub AS A
    RIGHT JOIN member AS B
    ON A.pubMemberId = B.memberId AND A.pubPubType = %(pubPubType)s
GROUP BY B.memberId
ORDER BY B.memberSurname, B.memberForename

"""

    else:
       
        sql = """SELECT B.memberSurname, B.memberForename, COUNT(A.pubPubType)
    FROM pub AS A
    RIGHT JOIN member AS B
    ON A.pubMemberId = B.memberId
GROUP BY B.memberId
ORDER BY B.memberSurname, B.memberForename
"""
   
    
    params = {'memberId': memberId, 'pubPubType': pubType}
    cursor.execute(sql, params)
    rows = cursor.fetchall()

    return rows

    
    

def get_broad_counts(cursor, memberId=None):
    """
    -------------------------------------------------------
    Queries the member and broad tables.
    Use: rows = get_broad_counts(cursor)
    Use: rows = get_broad_counts(cursor, memberId=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        memberId - a member ID number (int)
    Returns:
        rows - (list of member's last name, member's first
            name, and the number of broad expertises they hold data)
            if memberId is not None:
                rows containing memberId
            else:
                all member and broad expertise rows
            Sorted by last name, first name
    -------------------------------------------------------
    """
    
    if (memberId is not None):
        sql = """SELECT b.memberSurname, b.memberForename , COUNT(c.memberBroadBroadId)
FROM memberBroad as c
LEFT JOIN member as b
ON c.memberBroadMemberId = b.memberId 
WHERE b.memberId= %(memberId)s
GROUP BY memberId
"""



    else:
       
        sql = """SELECT b.memberSurname, b.memberForename , COUNT(c.memberBroadBroadId)
FROM memberBroad as c
LEFT JOIN member as b
ON c.memberBroadMemberId = b.memberId 
GROUP BY memberId
        
"""
   
    
    params = {'memberId': memberId}
    cursor.execute(sql, params)
    rows = cursor.fetchall()

    return rows
    
def get_all_expertises(cursor, memberId=None):
    """
    -------------------------------------------------------
    Queries the member, broad, and narrow tables
    Use: rows = get_all_expertises(cursor)
    Use: rows = get_all_expertises(cursor, memberId=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        memberId - a member ID number (int)
    Returns:
        rows - (list of member's last name, member's first
            name, a broad description, and a narrow description data)
            if memberId is not None:
                rows containing memberId
            else:
                all member and expertise rows
            Sorted by last name, first name, broad description, narrow
                description
    -------------------------------------------------------
    """
    if (memberId is not None):
        sql = """
        SELECT B.memberSurname, B.memberForename, C.narrowDesc, D.broadDesc
FROM memberNarrow as X
INNER JOIN member as B
ON B.memberID = X.memberNarrowMemberId
INNER JOIN narrow as C
ON C.narrowId= X.memberNarrowNarrowId 
INNER JOIN broad as D
ON C.narrowBroadId = D.broadId
WHERE memberId = %(memberId)s
        
"""

    else:
        sql = """
        SELECT B.memberSurname, B.memberForename, C.narrowDesc, D.broadDesc
FROM memberNarrow as X
INNER JOIN member as B
ON B.memberID = X.memberNarrowMemberId
INNER JOIN narrow as C
ON C.narrowId= X.memberNarrowNarrowId 
INNER JOIN broad as D
ON C.narrowBroadId = D.broadId
        
"""
    
    params = {'memberId': memberId}
    cursor.execute(sql, params)
    rows = cursor.fetchall()

    return rows
    
    
    
    