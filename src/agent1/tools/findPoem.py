import sqlite3


conn = sqlite3.connect('semantic_index.db')

cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
table_count = cursor.fetchone()[0]

print(f"Number of tables: {table_count}")
conn.close()



def findPoem():
    pass