from settings import sql
import MySQLdb

con = MySQLdb.connect(
    db=sql.DB_NAME,
    user=sql.DB_USER,
    passwd=sql.DB_PASS,
    charset=sql.DB_CHAR
)
print(con)
c = con.cursor()
c.execute('drop tables if exists cities')
c.execute('''
create table cities(
cities_rank integer,
city text,
population integer
)
''')

con.commit()
con.close()
