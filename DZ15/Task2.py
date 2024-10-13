# Напишите скрипт, который получает текущее время и дату, а затем выводит их в
# формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер
# недели в году.

from datetime import datetime

now = datetime.now()

print(f'Сейчас {now.strftime('%Y-%m-%d %H:%M:%S')}, '
      f'день недели {now.strftime('%A')}, '
      f'номер недели в году {now.isocalendar()[1]}')