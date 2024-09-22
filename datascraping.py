import requests
from bs4 import BeautifulSoup
from database.db_creds import connection

import mysql.connector

# connection = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='rish0515',
#     # database='billionaires'
# )

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS billionaires")
cursor.execute("USE billionaires")


Url = "https://en.wikipedia.org/wiki/The_World%27s_Billionaires"
r = requests.get(Url)

soup = BeautifulSoup(r.content, 'html5lib')



tables = soup.find_all('table', attrs = {'class':'wikitable sortable'})


years = soup.find_all('h3')
years_list = [year.text for year in years[1:]]
print("Years list : ", years_list)


for year, table in zip(years_list[:-10], tables[:-11]):

    table_name = f'billionaires_{year}'
    drop_table_query = f'DROP TABLE IF EXISTS {table_name}'
    create_table_query = f'''
    CREATE TABLE {table_name} (
        No INT,
        Name VARCHAR(255),
        Net_worth_USD VARCHAR(255),
        Age INT,
        Nationality VARCHAR(100),
        Primary_source_of_wealth VARCHAR(255)
    )
    '''

    try:
        cursor.execute(drop_table_query)
        cursor.execute(create_table_query)
        print(f"Table {table_name} created successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    

    heads = table.find_all('th')

    head_titles = [title.text.strip() for title in heads]

    head_row = table.find_all('tr')
    for row in head_row[1:]:
        columns = row.find_all('td')
        individual_data = [data.text.strip() for data in columns]
        print(individual_data)
        if len(columns) == len(head_titles):
            age_value = columns[3].text.strip()
            age = int(age_value) if age_value.isdigit() else None   # Ensure the number of columns matches
            values = [
                int(columns[0].text.strip()),  # No.
                columns[1].text.strip(),  # Name
                columns[2].text.strip().replace(',', '').replace('$', ''),  # Net worth
                # int(columns[3].text.strip()),  # Age
                age,
                columns[4].text.strip(),  # Nationality
                columns[5].text.strip()   # Primary source
            ]
            insert_query = f'''
            INSERT INTO {table_name} (No, Name, Net_worth_USD, Age, Nationality, Primary_source_of_wealth)
            VALUES (%s, %s, %s, %s, %s, %s)
            '''
            cursor.execute(insert_query, values)

    connection.commit()  # Commit the changes after each year

cursor.close()
connection.close()