import sqlite3

connection = sqlite3.connect('practice.db')

cursor = connection.cursor()

def print_rows():
    cursor.execute("""
    SELECT * FROM readings
    """)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def delete_table(table_name):
    cursor.execute(f'DROP TABLE IF EXISTS "{table_name}"')
    connection.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS readings (
    id INTEGER PRIMARY KEY,
    sensor_id INTEGER NOT NULL,
    temperature REAL NOT NULL,
    unit TEXT NOT NULL
)
""")

cursor.execute("""
Insert into readings (id, sensor_id, temperature, unit) values
(1, 101, 45, 'C'),
(2, 102, 35, 'C'),
(3, 103, 40, 'C'),
(4, 104, 45, 'C'),
(5, 105, 30, 'C')
""")

sensor_id = 101
cursor.execute("""
SELECT * FROM readings where sensor_id = ?
""", (sensor_id,))

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("""
Update readings set temperature = 38.5 where id = 3
""")

cursor.execute("""
select * from readings where id = ?
""",(3,))
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("""
Delete from readings where id = 5
""")
print("Rows deleted:", cursor.rowcount)

delete_table("readings")

connection.commit()
connection.close()