# -*- coding: utf-8 -*-

import sqlite3
from contextlib import closing

dbname = 'database.db'

with closing(sqlite3.connect(dbname)) as conn:
    c = conn.cursor()

    create_table = '''create table fortune (id int, text varchar(256))'''
    c.execute(create_table)

    insert_sql = 'insert into fortune (id, text) values (?,?)'
    fortune = [
        (1, 'マヨネーズを陰で飲んでいるのが、バレてしまうかも。'),
        (2, 'コーヒーを飲むと、息が臭くなります。'),
        (3, '目が合った異性に声を掛けると、50%の確率でデートができます。'),
        (4, 'シーフードヌードルにタバスコをかけて食べると、良いことがあります。'),
        (5, 'カレーを食べると、IQが150になります。'),
        (6, 'タバコの煙を鼻から出してみると、良い事があります。'),
        (7, '道の真ん中でバク転をしても、無視されます。'),
        (8, '板チョコを食べると、鼻血が出ます。'),
        (9, '水の蛇口をひねり、溢れるまで走ってください。'),
        (10, '適当な占いを考えるのが疲れました。'),
    ]
    c.executemany(insert_sql, fortune)
    conn.commit()

    select_sql = 'select * from fortune'
    for row in c.execute(select_sql):
        print(row)