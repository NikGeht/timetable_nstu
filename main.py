import datetime
import db


def get_result(res: []):
    for sub in res:
        for s in sub:
            print(s)


date = datetime.datetime.now()



week = int(date.strftime('%V'))-34
if date.weekday() == 6:
    week = week + 1

print("Расписание на данную неделю: ")
result = db.get_timetable(week)
get_result(result)

print("Расписание на следующую неделю: ")
result = db.get_timetable(week+1)
get_result(result)



