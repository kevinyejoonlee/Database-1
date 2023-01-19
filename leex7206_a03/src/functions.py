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

def get_all_pub_counts(cursor, memberId=None):
    """
    -------------------------------------------------------
    Queries the pub and member tables.
    Use: rows = pub_counts(cursor)
    Use: rows = pub_counts(cursor, memberId=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        memberId - a member ID (int)
    Returns:
        rows - (list of member's last name, a member's first
            name, and the numbers of publications of each type data.
            Name these three fields "articles", "papers", and "books")
            if memberId is not None:
                rows containing memberId
            else:
                all member and publication rows
            Sorted by last name, first name
    -------------------------------------------------------
    """
    #
    if (memberId is not None):
        sql = """
        SELECT A.memberSurname, A.memberForename,
                (SELECT COUNT(C.pubMemberId)
                FROM pub AS C
                WHERE A.memberId = C.pubMemberId AND C.pubPubType = 'a') AS articles,
                (SELECT COUNT(D.pubMemberId)
                FROM pub AS D
                WHERE A.memberId = D.pubMemberId AND D.pubPubType= 'p') AS papers,
                (SELECT COUNT(B.pubMemberId)
                FROM pub AS B
                WHERE A.memberId = B.pubMemberId AND B.pubPubType= 'b') AS books
            FROM member AS A
            WHERE A.memberId = %(memberId)s
            GROUP BY A.memberId
            ORDER BY A.memberSurname, A.memberForename
"""

    else:

        sql = """
        SELECT A.memberSurname, A.memberForename,
                (SELECT COUNT(C.pubMemberId)
                FROM pub AS C
                WHERE A.memberId = C.pubMemberId AND C.pubPubType = 'a') AS articles,
                (SELECT COUNT(D.pubMemberId)
                FROM pub AS D
                WHERE A.memberId = D.pubMemberId AND D.pubPubType= 'p') AS papers,
                (SELECT COUNT(B.pubMemberId)
                FROM pub AS B
                WHERE A.memberId = B.pubMemberId AND B.pubPubType= 'b') AS books
            FROM member AS A
            GROUP BY A.memberId
            ORDER BY A.memberSurname, A.memberForename
"""
   
    
    params = {'memberId': memberId}
    cursor.execute(sql, params)
    rows = cursor.fetchall()


    return rows

    
    
    
def get_expertise_counts(cursor, memberId=None):
    """
    -------------------------------------------------------
    Use: rows = get_expertise_counts(cursor)
    Use: rows = get_expertise_counts(cursor, memberId=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        memberId - a member ID number (int)
    Returns:
        rows - (list of member's last name, a member's first
            name, and the number of broad and narrow expertises
            for the member data. Name these fields "broadCount" and "narrowCount")
            if memberId is not None:
                rows containing memberId
            else:
                all member, broad, and narrow expertise rows
            Sorted by last name, first name
    -------------------------------------------------------
    """
    
    if (memberId is not None):
        sql = """SELECT A.memberSurname, A.memberForename,
                    (SELECT COUNT(C.memberBroadBroadId)
                    FROM memberBroad AS C
                    WHERE A.memberId = C.memberBroadMemberId) AS broadCount,    
                    (SELECT COUNT(C.memberNarrowNarrowId)
                    FROM memberNarrow AS C
                    WHERE A.memberId = C.memberNarrowMemberId) AS narrowCount
        FROM member AS A
        WHERE A.memberId = %(memberId)s
        GROUP BY A.memberId
        ORDER BY A.memberSurname, A.memberForename
"""

    else:

        sql = """
          SELECT A.memberSurname, A.memberForename,
            (SELECT COUNT(C.memberBroadBroadId)
            FROM memberBroad AS C
            WHERE A.memberId = C.memberBroadMemberId) AS broadCount,    
            (SELECT COUNT(C.memberNarrowNarrowId)
            FROM memberNarrow AS C
            WHERE A.memberId = C.memberNarrowMemberId) AS narrowCount
        FROM member AS A
        GROUP BY A.memberId
        ORDER BY A.memberSurname, A.memberForename
"""
   
    
    params = {'memberId': memberId}
    cursor.execute(sql, params)
    rows = cursor.fetchall()


    return rows
    

    
 
    
def get_broad_counts(cursor, broadId=None):
    """
    -------------------------------------------------------
    Use: rows = get_broad_counts(cursor)
    Use: rows = get_broad_counts(cursor, broadId=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        broadId - a keyword ID number (int)
    Returns:
        rows - (list of a broad expertise descriptions and the number of
            narrow expertises that belong to it data. Name the
            second field "narrowCount".)
            if broadId is not None:
                rows containing broadId
            else:
                all broad and narrow rows
            Sorted by broad expertise description
    -------------------------------------------------------
    """
    if (broadId is not None):
        sql = """
        SELECT A.broadDesc, 
            (SELECT COUNT(C.narrowId)
            FROM narrow AS C
            WHERE A.broadId = C.narrowBroadId) AS narrowCount 
        FROM broad AS A
        WHERE A.broadId =  %(broadId)s
        GROUP BY A.broadId
        ORDER BY A.broadDesc
        
"""

    else:

        sql = """
        SELECT A.broadDesc, 
            (SELECT COUNT(C.narrowId)
            FROM narrow AS C
            WHERE A.broadId = C.narrowBroadId) AS narrowCount 
        FROM broad AS A
        GROUP BY A.broadId
        ORDER BY A.broadDesc
        
        
"""
   
    
    params = {'broadId': broadId}
    cursor.execute(sql, params)
    rows = cursor.fetchall()


    return rows
    
    
def get_broad_member_counts(cursor, broadId=None):
    """
    -------------------------------------------------------
    Use: rows = get_broad_memberCounts(cursor)
    Use: rows = get_broad_memberCounts(cursor, broadId=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        broadId - a keyword ID number (int)
    Returns:
        rows - (list of a keyword description and the number of members
            that have it data. Name the second field "memberCount".)
            if broadId is not None:
                rows containing broadId
            else:
                all member and keyword rows
            Sorted by keyword description
    -------------------------------------------------------
    """
    if (broadId is not None):
        sql = """
   SELECT C.broadDesc, 
            (SELECT COUNT(D.memberBroadMemberId)
            FROM memberBroad as D
            WHERE D.memberBroadBroadId = C.broadId) as memberCount
    
        FROM broad as C
        WHERE C.broadId =  %(broadId)s
        GROUP BY C.broadId
"""

    else:
        sql = """
     SELECT C.broadDesc, 
            (SELECT COUNT(D.memberBroadMemberId)
            FROM memberBroad as D
            WHERE D.memberBroadBroadId = C.broadId) as memberCount
        FROM broad as C
        GROUP BY C.broadId
        
"""
   
    
    params = {'broadId': broadId}
    cursor.execute(sql, params)
    rows = cursor.fetchall()


    return rows
    
def get_narrow_member_counts(cursor, narrowId=None):
    """
    -------------------------------------------------------
    Use: rows = get_narrow_memberCounts(cursor)
    Use: rows = get_narrow_memberCounts(cursor, narrowId=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        narrowId - a supp_key ID number (int)
    Returns:
        rows - (list of a broad expertise description, a narrow
            expertise description, and the number of members that have that
            narrow expertise data. Name the last field "memberCount".)
            if narrowId is not None:
                rows containing narrowId
            else:
                all member, broad, and narrow expertises rows
            Sorted by broad description, narrow description
    -------------------------------------------------------
    """
    if (narrowId is not None):
        sql = """
        SELECT C.broadDesc, B.narrowDesc, 
            (SELECT COUNT(D.memberNarrowMemberId)
            FROM memberNarrow as D
            WHERE D.memberNarrowNarrowId = B.narrowId) as memberCount
            
        FROM broad as C

        RIGHT JOIN narrow AS B
        ON B.narrowBroadId = C.broadId
         WHERE narrowId = %(narrowId)s

"""



    else:

        sql = """
        SELECT C.broadDesc, B.narrowDesc, 
            (SELECT COUNT(D.memberNarrowMemberId)
            FROM memberNarrow as D
            WHERE D.memberNarrowNarrowId = B.narrowId) as memberCount
        FROM broad as C
        RIGHT JOIN narrow AS B
        ON B.narrowBroadId = C.broadId

"""
   
    
    params = {'narrowId': narrowId}
    cursor.execute(sql, params)
    rows = cursor.fetchall()


    return rows
    
    
