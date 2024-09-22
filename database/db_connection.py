from database.db_creds import connection as cnx

def db_get_top_billionaires(top_number : int, year = str | None):
    
    top_number = int(top_number)
    cursor = cnx.cursor()
    cursor.execute("USE billionaires")

    query = (f"Select No, Name, Net_worth_USD from billionaires_{year} limit {top_number}")

    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()

    if result is not None:
        return result
    else:
        return None
    
def db_get_billionaire_by_rank(year : int, rank : int):
    cursor = cnx.cursor()
    cursor.execute("USE billionaires")

    query = (f"Select Name, Net_worth_USD from billionaires_{int(year)} Where No={int(rank)}")

    cursor.execute(query)
    result = cursor.fetchone()

    cursor.close()

    if result is not None:
        return result
    else:
        return None

def db_get_details_billionaire(key : int, year : int):
    cursor = cnx.cursor()
    cursor.execute("USE billionaires")

    query = (f"Select * from billionaires_{int(year)} Where No={int(key)}")

    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()

    if result is not None:
        return result
    else:
        return None
    
def db_get_details_from_name(name : str):
    cursor = cnx.cursor()
    cursor.execute("USE billionaires")

    query = f"""
    SELECT No, Name, Net_worth_USD
    FROM billionaires_2024
    WHERE LOWER(name) LIKE LOWER(CONCAT('%', %s , '%'));
    """

    cursor.execute(query, (name,))
    result = cursor.fetchone()
    cursor.close()

    if result is not None:
        return result
    else:
        return None
    
def db_get_details_from_year(name : str, year :int):
    print("name is : ", name, " year is : ", year )
    cursor = cnx.cursor()
    cursor.execute("USE billionaires")

    table_name = f"billionaires_{year}"

    query = f"""
    SELECT No, Name, Net_worth_USD
    FROM {table_name}
    WHERE LOWER(name) LIKE LOWER(CONCAT('%', %s , '%'));
    """

    cursor.execute(query, (name,))
    result = cursor.fetchone()
    cursor.close()
    print("result in database details by year : ", result)

    if result is not None:
        return result
    else:
        return None
    
