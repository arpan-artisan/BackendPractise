import sqlite3

def create_column_timestamp():
    connection = sqlite3.connect('practice.db')
    cursor = connection.cursor()
    cursor.execute('''
        ALTER TABLE readings ADD COLUMN received_at text
    ''')
    connection.commit()
    connection.close()

if __name__== "__main__":
    create_column_timestamp()