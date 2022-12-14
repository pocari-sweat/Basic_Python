import sqlite3

conn = sqlite3.connect("test.db")

data = (
    (21, '김김김'),
    (22, '이이이')
)

with conn:
    cur = conn.cursor()
    sql = "insert into tt(id, name) values(?,?)"
    cur.executemany(sql, data)

    conn.commit()