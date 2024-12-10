# import psycopg2

# подключение к базе данных
# connection = psycopg2.connect(
#     host='localhost',
#     database='postgres',
#     user='postgres',
#     password='81726354'
# )

# операции с базой данных
# cur = connection.cursor()
# cur.execute('INSERT INTO post VALUES (%s, %s, %s)', (8, 'G', 'l'))
# cur.execute('SELECT * FROM post')
# connection.commit()
#
#
# rows = cur.fetchall()
# for row in rows:
#     print(row)
#
# cur.close()
# connection.close()
