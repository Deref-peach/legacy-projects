import sqlite3
from typing import List


class TimeTable:
    def __init__(self, conn: sqlite3.Connection):
        self.conn: sqlite3.Connection = conn

    def get_timetable(self) -> List[str]:
        with self.conn as conn:
            cur = conn.cursor()
            cur.execute("""
            SELECT * FROM timetable
            """)
            return cur.fetchall()

    def get_day_timetable(self, day: str) -> List[str]:
        pass

    def set_timetable(self, day: str, lesson: str, num: int):
        with self.conn:
            cur: sqlite3.Cursor = self.conn.cursor()
            cur.execute("""
            UPDATE timetable
            SET lesson = ?
            WHERE day_week = ?
            AND num = ?
            ORDER day_week;
            """, (lesson, day, num))

    def set_day_timetable(self, day: str, lessons: List[str]):
        for num, les in enumerate(lessons):
            self.set_timetable(day, les, num)

    def get_near_lesson(self, lesson: str):
        pass


class HomeWork:
    def __init__(self, conn: sqlite3.Connection):
        self.conn: sqlite3.Connection = conn

    def get_hw_lesson(self, lesson: str):
        with self.conn:
            cur: sqlite3.Cursor = self.conn.cursor()

    def get_hw_day(self, day: str):
        pass
