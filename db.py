import sqlite3


def get_timetable(week: int):
    connection = sqlite3.connect('timetable.db')
    cursor = connection.cursor()
    result = []
    if week % 2 == 1:
        numweek = "1"
        cursor.execute('SELECT weekdays, time, subject, gde, prepod FROM timetable WHERE numweeks=?', (numweek,))
        result.append(cursor.fetchall())
        add_week = [5, 9, 13, 15]
        if week in add_week:
            cursor.execute('SELECT weekdays, time, subject, gde, prepod FROM timetable WHERE numweeks="5,9,13,15"')
            result.append(cursor.fetchall())
    elif week % 2 == 0:
        numweek = "2"
        cursor.execute('SELECT weekdays, time, subject, gde, prepod FROM timetable WHERE numweeks=?', (numweek,))
        result.append(cursor.fetchall())
        add_week = [6, 10, 14, 18]
        if week in add_week:
            cursor.execute('SELECT weekdays, time, subject, gde, prepod FROM timetable WHERE numweeks="6,10,14,18"')
            result.append(cursor.fetchall())
    cursor.execute('SELECT weekdays, time, subject, gde, prepod FROM timetable WHERE numweeks="всегда"')
    result.append(cursor.fetchall())
    return result
