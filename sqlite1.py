import sqlite3

conn = sqlite3.connect("test.db")
 
with conn:
    cur = conn.cursor()
    sql = "select * from Student where id = ? or name = ?"
    rows = cur.execute(sql, (1, '홍길순'))
    # rows = cur.execute(sql)
    # rows = cur.fetchall()  
    # rows = cur.fetchone()   
 
    for row in rows:
        print(row)