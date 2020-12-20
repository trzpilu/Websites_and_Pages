import sqlite3
from sqlite3 import Error

class Todos:
    
    # Inits the database, establishes connection.
    def __init__(self, database):
        self.conn = None
        try:
            self.conn = sqlite3.connect(database, check_same_thread=False)
            if self.conn is not None:
                self.conn.cursor().execute("""CREATE TABLE IF NOT EXISTS todos (
                                            id integer PRIMARY KEY,
                                            title VARCHAR(250) NOT NULL,
                                            description TEXT,
                                            done BIT);""")
            self.cur = self.conn.cursor()
        except Error as e:
            print(e)


    # Fetches all cursors from todos.
    def all(self):
        result = self.cur.execute("SELECT * FROM todos")
        return result.fetchall()

    # Fetches cursor with particular id from todos.
    def get(self, id):
        result = self.cur.execute(f"SELECT * FROM todos WHERE id={id}")
        return result.fetchone()

    # Creates entry into todos with 3 columns (named below), and commits the new entry
    # to the database, returning the new entry at the end of the list. 
    def create(self, data):
        sql = '''INSERT INTO todos(title, description, done)
                    VALUES(?,?,?)'''
        result = self.cur.execute(sql, data)
        self.conn.commit()
        return result.lastrowid
    
    # ----------------------------------------------------------------------- #    
    # save_all function not needed, as database automatically stores data
    # def save_all(self):
    #     with open("todos.json", "w") as f:
    #         json.dump(self.todos, f)
    # ----------------------------------------------------------------------- #

    # Updates chosen entry by id and sets new values, and commits the updated entry
    # to the database.

    
    def update(self, id, data):
        sql = f''' UPDATE todos
                    SET title = ?, description = ?, done = ?
                    WHERE id = {id}'''
        try:
            self.cur.execute(sql, data)
            self.conn.commit()
        except sqlite3.OperationalError as e:
            print(e)
   
    def delete_where(self, **kwargs):
        """
        Delete from table where attributes from
        :param kwargs: dict of attributes and values
        :return:
        """
        qs = []
        values = tuple()
        for k, v in kwargs.items():
            qs.append(f"{k}=?")
            values += (v,)
        q = " AND ".join(qs)

        sql = f'DELETE FROM todos WHERE {q}'
        cur = self.conn.cursor()
        cur.execute(sql, values)
        self.conn.commit()
        print("Deleted")



database = "database.db"
todos = Todos(database)

if __name__ == "__main__":
   
   db_file = "database.db"
   todos_test = Todos(db_file)

   todo1 = ("Powtórka z Pythona", "Powtórzyć materiał z modułu 10", "1")
   todo2 = ("Zakupy", "Piekarnia i warzywniak", "0")
   todo3 = ("Sprzątanie", "Odkurzyć i pozmywać naczynia", "0")
   todo4 = ("Pies", "Spacer z psem", "0")
   #todo_id = add(conn, todo3)
   
   #todos_test.create(todo1)
   #todos_test.create(todo2)
   #todos_test.create(todo3)
   
   #todos_test.delete_where(id=2)
   
   #print(todos_test.update())

   #print(todos_test.get(id=2))

   
   #todos_test.update(id=2)

   todos_test.update(id=3, data=["Bob", "spoko", "false"])

   #todos_test.add(todo4)

   print(todos_test.all())