from vkwave.bots import SimpleBotEvent

from .loader import bot, conn
from .models import HomeWork, TimeTable
from .filters import MatFilter, TimeTableFilter, GetTimeTableFilter, SetTimeTableFilter

table: TimeTable = TimeTable(conn)
hwork: HomeWork = HomeWork(conn)


@bot.message_handler(MatFilter())
async def mat(event: SimpleBotEvent) -> str:
    return "Не матерись"


@bot.message_handler(TimeTableFilter(), SetTimeTableFilter())
async def set_table(event: SimpleBotEvent):
    args = event["args"]
    day: str = args[2]
    if day == "-day":
        table.set_day_timetable(day, args[3:])
    else:
        table.set_timetable(day, args[3], int(args[4]))


@bot.message_handler(TimeTableFilter(), GetTimeTableFilter())
async def get_table_day(event: SimpleBotEvent):
    if day == "-day":
        res = table.get_day_timetable(day)
    else:
        res = table.get_timetable()
    return res


async def get_day_hwork(event: SimpleBotEvent):
    pass


async def get_lesson_hwork(event: SimpleBotEvent):
    pass

# TODO: Хэндлер Мата

# TODO: Создавать расписание на день\урок \/
# TODO: Возвращать расписание на день\урок

# TODO: Создавать дз на день\урок
# TODO: Возвращать дз на день\урок

# TODO: Каждый день отправлять расписание на завтра
# TODO: Каждый день отправлять дз на завтра

# TODO: Хэндлер "Когда <урок>"
# TODO: Хэндлер "Что задали по <урок>"
