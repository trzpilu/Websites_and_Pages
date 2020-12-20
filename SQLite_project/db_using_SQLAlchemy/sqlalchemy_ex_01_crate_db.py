import sqlalchemy

from sqlalchemy import create_engine


engine = create_engine('sqlite:///C:\Kodilla\projekty\SQLite_project\SQLite\database.db')

print(engine.driver)

print(engine.table_names())

print(engine.execute("SELECT * FROM tasks"))

results = engine.execute("SELECT * FROM tasks")

for r in results:
   print(r)
   