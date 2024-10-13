# Напишите скрипт, который принимает два аргумента командной строки: число и
# строку. Добавьте следующие опции:
# ● --verbose, если этот флаг установлен, скрипт должен выводить
# дополнительную информацию о процессе.
# ● --repeat, если этот параметр установлен, он должен указывать,
# сколько раз повторить строку в выводе.


import argparse

def parse():
    parser = argparse.ArgumentParser(description="parser",
                                     epilog="endparse")

    # Обязательные аргументы:
    parser.add_argument('number', metavar='N', type=int, nargs=1, help='enter number')
    parser.add_argument('text', metavar='N', type=str, nargs=1, help='enter text')

    # Необязательные аргументы:
    parser.add_argument('-v', '--verbose', action='store_true', help='enter verbose')
    parser.add_argument('-r', '--repeat', type=int,
                        help='enter number of repeating', default=1)

    args = parser.parse_args()

    if args.verbose:
        print(f'Полученные аргументы: number={args.number}, '
              f'text = "{args.text}", repeat = {args.repeat}')
        return f'Число: {args.number}, Строка: {args.text * args.repeat}'

    return f'Число: {args.number}, Строка: {args.text * args.repeat}'

if __name__ == '__main__':
    # Запуск из терминала, командой вида "python Task4.py 5 text_sample -v -r 10"
    print(parse())
