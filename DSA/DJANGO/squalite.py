import sqlite3

conn = sqlite3.connect('demoDatabase1.db')
c = conn.cursor()
# create a table
# c.execute(''' CREATE TABLE STOCK1 (data text,trans text,symbol text,qty real,price real)''')

# insert values to table

# c.execute("INSERT INTO STOCK1 VALUES ('2006-3-12','buy','rhat',100,35.90)")
c.execute("SELECT * from STOCK1")
for row in c:
    print(row)

conn.commit()

conn.close()
try:
    pass
    # sql code

except sqlite3.Error as e:
    print('An error occured:',e.args[0])

