# import sys
from datetime import datetime
from datetime import date
# if len(sys.argv) == 1:
#     print('Привет мир!')
# else:
#     p_name = sys.argv[1]
#     p_value = sys.argv[2]

#     if p_name == '--name':
#         print(f'Привет {p_value}')
#     else:
#         print(f'Неизвесный параметр {p_name}')
import argparse

parser = argparse.ArgumentParser()

""""Эта функция возвращает введеную дату, если введена верно и сегодняшнюю дату, если неверно"""
def valid_date(s: str) -> datetime:
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        return datetime.today().strftime('%Y-%m-%d')
    #     raise argparse.ArgumentTypeError(f"not a valid date: {s!r}")
    # finally:
    #     return datetime.today().strftime('%Y-%m-%d')
# parser.add_argument('name', nargs='?', default='мир!')
parser.add_argument('date', type=valid_date)

args = parser.parse_args()

print(f'Привет {args.date}')