import sqlite3


class TasksDatabase:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, osoba text, vrijeme text, datum text, zadatak text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM tasks")
        rows = self.cur.fetchall()
        return rows
  
    def insert(self, osoba, vrijeme, datum, zadatak):
        self.cur.execute("INSERT INTO tasks VALUES (NULL, ?, ?, ?, ?)",
                         (osoba, vrijeme, datum, zadatak))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM tasks WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, osoba, vrijeme, datum, zadatak):
        self.cur.execute("UPDATE tasks SET osoba = ?, vrijeme = ?, datum = ?, zadatak = ? WHERE id = ?",
                         (osoba, vrijeme, datum, zadatak, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()



# db = TasksDatabase('tasks.db')
# db.insert("Davor Plazonic", "15:40", "15.4.2023.", "trening plivanja na bazenu")


