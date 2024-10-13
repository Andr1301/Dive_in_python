# Напишите код, который запускается из командной строки и получает на вход путь
# до директории на ПК. Соберите информацию о содержимом в виде объектов
# namedtuple. Каждый объект хранит: имя файла без расширения или название
# каталога, расширение, если это файл, флаг каталога, название родительского
# каталога. В процессе сбора сохраните данные в текстовый файл используя
# логирование.

from collections import namedtuple
import logging
import argparse
from pathlib import Path

logging.basicConfig(filename='logs/data_path.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


Files = namedtuple('File', 'name extension dir parent')
def read_dir(path: str):
    path = Path(path)
    for file in path.iterdir():
        obj = Files(file.stem if file.is_file() else file.name, file.suffix, file.is_dir(), file.parent)
        logger.info(obj)
        if obj.dir:
            read_dir(str(Path(obj.parent) / obj.name))


def walker():
    my_walker = argparse.ArgumentParser(
        description='my_walker',
        prog='read_dir()',
    )
    my_walker.add_argument('path', metavar='p',
                           type=str, help='enter full path to directory')
    args = my_walker.parse_args()
    """
    return read_dir(Path(args.path))  - Тоже рабочий вариант, подсказанный чат-жпт)
    Но ИДЕ на него ругается и подчеркиват желтым, поэтому дописал альтернативный вариант избавления от кавычек    
    """
    return read_dir(args.path.strip("'"))

if __name__ == '__main__':
    # Запускается командой вида 'python Task5.py "C:\Users\Andr\Desktop\ee\Python2\123\DZ15"'
    walker()