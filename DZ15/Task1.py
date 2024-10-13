# Задание 1. Логирование с использованием нескольких файлов
# Напишите скрипт, который логирует разные типы сообщений в разные файлы.
# Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
# WARNING и выше — в warnings_errors.log.

import logging

FORMAT = '{levelname} - {asctime} - {msg}'
logging.basicConfig(level=logging.DEBUG)
log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(msg)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

debug_info_file_handler = logging.FileHandler('logs/debug_info.log', encoding='utf-8')
debug_info_file_handler.setLevel(logging.DEBUG)
debug_info_file_handler.addFilter(lambda msg: msg.levelno in (logging.DEBUG, logging.INFO))
debug_info_file_handler.setFormatter(log_format)
logger.addHandler(debug_info_file_handler)

warning_error_critical_file_handler = logging.FileHandler('logs/warnings_errors.log', encoding='utf-8')
warning_error_critical_file_handler.setLevel(logging.WARNING)
warning_error_critical_file_handler.setFormatter(log_format)
logger.addHandler(warning_error_critical_file_handler)

def math(a, b):
     try:
         logger.warning('Получены аргументы функции, начинаю расчет')
         result = a / b
         logger.info('Результат успешно получен!')
     except ZeroDivisionError as e:
         logger.error('Обнаружено деление на ноль!')
         return float('inf')
     return

if __name__ == '__main__':
    math(6, 2)