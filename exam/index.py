import sqlite3
def make_grade(score):
    grades = ['A', 'B', 'C', 'D', 'F']
    grades.reverse()
    if score == '100':
        return 'A+'
    else:
        return grades[ int(score) // 10 -5]

def make_age_gen(age):
    try:                                    # age 가 숫자가 아닌 스트링이면 변환불가이기에
        return str( int(age) // 10 ) + '0대'
    except:
        return '알수 없음'

    


def make_gender(gend):
    return 'M' if gend == '남' else 'F'

def make_addr(addr):
    lst = addr.split(' ')
    gu = ''                   #에러 방지위해 빈 변수 미리 만들어줌
    dong = ''
    for word in lst:
        if word[-1] == '구':
            gu = word
        elif word[-1] == '동':
            dong = word
    return '{} {}'.format(gu, dong)



def read_csv():
    studs = []
    insert_Data = []
    with open('exam/students.csv', 'r', encoding = 'utf-8') as file:
        for line in file:
            studs.append(line)
    for i, student in enumerate(studs):
        studs[i] = student.split(',')
        for j, item in enumerate(studs[i]):
            studs[i][j] = item.strip()
    del studs[0]

    # for i in studs:
    #     print(i)


    for i, stu in enumerate(studs):
        studs[i].append(stu[0][0] + '**')
        studs[i].append(make_gender(stu[1]))
        studs[i].append(make_age_gen(stu[2]))
        studs[i].append(make_grade(stu[3]))
        studs[i].append(make_addr(stu[4]))

    # for i in studs:
    #     print(i)

    results = []
    for stu in studs:
        results.append(( stu[5],stu[6],stu[7],stu[8],stu[9] ))
    

    return tuple(results)

# print(read_csv())


conn = sqlite3.connect('exam.db')
cur = conn.cursor()

def insert_data(data):
    with conn:
        sql = 'insert into student(name, gender, age, grade, address) values(?, ?, ?, ?, ?)'
        cur.executemany(sql,data)

        conn.commit()

def make_table():
    with conn:
        sql = 'create table student(id integer not null primary key autoincrement,name text not null, gender text, age text, grade text, address text)'
        cur.execute(sql)
        conn.commit()

def modify_table():
    # cur.execute('alter table Student add column gender test')    #테이블 자체 수정, 새로운 컬럼 넣기
    print(1)

def delete_table():
    with conn:
        sql = 'drop table student'
        cur.execute(sql)
        conn.commit()
def select_data():
    with conn:
        sql = 'select id, name, gender, age, grade, address\
               from student \
               order by substr(grade,1,1), grade desc'
        cur.execute(sql)
        rows = cur.fetchall()

        for row in rows:
            print(row)


print(read_csv())
make_table()
insert_data(read_csv())
select_data()
delete_table()