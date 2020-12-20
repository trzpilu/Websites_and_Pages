# sqlalchemy_ex_02.py
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine

engine = create_engine('sqlite:///C:\Kodilla\projekty\SQLite_project\SQLite\database.db')

meta = MetaData()

students = Table(
   'students', meta,
   Column('id', Integer, primary_key=True),
   Column('name', String),
   Column('lastname', String),
)

meta.create_all(engine)
print(engine.table_names())