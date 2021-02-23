import sqlite3

from resources.models import TimeTable

conn = sqlite3.connect("./db/lessons.db")

with conn:
    cur = conn.cursor()

    cur.execute("""
                CREATE TABLE timetable
                    (day_week text, lesson text, num int)
                """)

    cur.execute("""
                CREATE TABLE tasks
                    (day_week text, lesson text, todo text)
                """)


table = TimeTable(conn)

table.get_timetable()
