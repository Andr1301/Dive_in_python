# Напишите функцию, которая принимает количество дней от текущей даты и
# возвращает дату, которая наступит через указанное количество дней. Дополнительно,
# выведите эту дату в формате YYYY-MM-DD.

from datetime import datetime, timedelta


def future_date(days: int):
    return(datetime.now() + timedelta(days=days)).strftime('%Y-%m-%d')

if __name__ == '__main__':
    print(future_date(5))