import sqlite3
import random 
fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")
first_names = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")

data=[]
for i in range(0,100):
    first_pick= ''.join(random.sample(first_names,2))
    fam_pick=random.choices(fam_names, k=1)
    s=fam_pick[0] + first_pick

    data.append((fam_pick[0] + first_pick,))  

print(data)


conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    sql = 'insert into Student(name) values(?)'
    cur.executemany(sql,data)

    conn.commit()

