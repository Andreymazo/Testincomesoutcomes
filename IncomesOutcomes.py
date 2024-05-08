import argparse
from datetime import datetime
import os
import subprocess

class IncomesOutcomes:
  
    def __init__(self, date, category, amount, comment):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment
    """ Функция покакзывает текущий баланс, доходы, расходы, на входе дата"""
    def show_amounts_by_date(self, date):
        print('date', date)
        with open ('our_file.txt', 'r') as f:
            lines = [line.rstrip() for line in f]
            result_lst = []
            for i in lines:
                result_i = [x.strip() for x in i.split(',')]
                if result_i[1] == 'Доход':
                    result_lst.append(int(result_i[2]))
                if result_i[1] == 'Расход':
                    result_lst.append(-int(result_i[2]))
                else:
                    pass
            print(f'Баланс {sum(result_lst)}')
            plus_lst = [i for i in result_lst if i > 0]
            minus_lst = [i for i in result_lst if i < 0]
            print(f'Доходы  {sum(plus_lst)}')
            print(f'Расходы {sum(minus_lst)}')
        
    """ Функция добавляет текущую дату, доход или расход, комментарий, на входе ничего"""
    # def add_current_params(self)-> str:
    import os.path

    def add_line(self, date, category, amount, comment ):
        file_path = 'our_file.txt'
        if os.path.exists(file_path):
            with open ('our_file.txt', 'a') as f:
                f.write(f'\n{date}, {category}, {amount}, {comment}')
        else:
            with open ('our_file.txt', 'w') as f:
                f.write(f'{date}, {category}, {amount}, {comment}')

    """ Функция изменяет существующую запись, на входе дата"""
    def update_current(self,  date: str) -> str:
        pass
    """ Функция ищет запись или записи по дате """
    def search_by_date(self, date: str)-> str:
        with open ('our_file.txt', 'r') as f:
            lines = [line.rstrip() for line in f]
            result_lst = []
            for i in lines:
                result_i = [x.strip() for x in i.split(',')]
                if result_i[0] == str(date):
                    result_lst.append(result_i)
        
        keys_lst = ['Дата', 'Категория', 'Сумма', 'Примечание']
        dict_for_print = dict(zip(keys_lst, result_lst[0]))
        for k,v in dict_for_print.items():
            print(f'{k}: {v}\n')
     
    """ Функция ищет запись или записи по категории """
    def search_by_category(self, category: str)-> str:
        with open ('our_file.txt', 'r') as f:
            lines = [line.rstrip() for line in f]
            result_lst = []
            for i in lines:
                result_i = [x.strip() for x in i.split(',')]
                if result_i[1] == str(category):
                    result_lst.append(result_i)
        print(result_lst)
        
    """ Функция ищет запись или записи по сумме """
    def search_by_amount(self, amount: str)-> str:
        print('amount', amount)
        with open ('our_file.txt', 'r') as f:
            lines = [line.rstrip() for line in f]
            result_lst = []
            for i in lines:
                result_i = [x.strip() for x in i.split(',')]
                if result_i[2] == str(amount):
                    result_lst.append(result_i)
        print(result_lst)
    
                
    """ Функция изменяет существующюю запись """
    def update_line(self, num_line, pattern_changed, pattern_to_change):
        print('pattern_changed', pattern_changed)
        num_cell = ''
        # proverka(self, pattern_changed)
        dic_param = {'date':1, 'category':2, 'amount':3, 'comment':4}
        for k,v in dic_param.items():
            if k == pattern_changed:
                num_cell = v
   
        with open ('our_file.txt', 'r+') as f:
                lines = [line.rstrip() for line in f]
                for index, i in enumerate(lines):
                    if index == num_line-1:
                        i = [x.strip() for x in i.split(',')]
                        i[num_cell-1]=pattern_to_change
                        i = ', '.join(i)
                        subprocess.run(f"sed '{num_line}d' our_file.txt > tmpfile; mv tmpfile our_file.txt ", shell=True)# Уничтожаем строку
                        subprocess.run(f"sed -i '{num_line}i\{i}' our_file.txt", shell=True) # Вставляем строку
                        
                   
        with open ('our_file.txt', 'r') as f:
                lines = [line.rstrip() for line in f]
                for index, i in enumerate(lines):
                    print(index, i)


if __name__ == '__main__':
    msg = """Here will write description of app  cmds:
        python IncomesOutcomes.py -date 2323-02-21 search_by_date; 
        python IncomesOutcomes.py -amount 25 search_by_amount;
        python IncomesOutcomes.py -category Доход search_by_category;
        python IncomesOutcomes.py -amount 25 search_by_amount;
        python IncomesOutcomes.py -date 2323-02-21 -category Доход -amount 25 -comment аренда add_line;
        python IncomesOutcomes.py -date 25 show_amounts_by_date;
        python IncomesOutcomes.py -num_line 1 -pattern_changed category -pattern_to_change Доход update_line;
        python IncomesOutcomes.py -num_line 2 -pattern_changed category -pattern_to_change Расход update_line;
        python IncomesOutcomes.py -num_line 2 -pattern_changed amount -pattern_to_change 35 update_line;
            """
    parser = argparse.ArgumentParser(description = msg)

    """Эта функция возвращает введеную дату, если введена верно и сегодняшнюю дату, если неверно"""
    def valid_date(s: str) -> datetime:
        try:
            return datetime.strptime(s, "%Y-%m-%d").date()
        except ValueError:
            return datetime.today().strftime('%Y-%m-%d')
        

    parser.add_argument('-date', '--date', nargs='?',  type=valid_date)
    parser.add_argument('-category', '--category', nargs='?', type=str)
    parser.add_argument("-amount", "--amount", nargs='?', type=str )
    parser.add_argument("-comment", "--comment", nargs='?', type=str)
    parser.add_argument("-num_line", "--num_line", nargs='?', type=int )#Номер строки которую будем менять
    parser.add_argument("-pattern_changed", "--pattern_changed", nargs='?', type=str )#Ячейка, которую будем менять
    parser.add_argument("-pattern_to_change", "--pattern_to_change", nargs='?', type=str )# Что будем вставлять

    parser.add_argument("operation", help = "operation") 

    args = parser.parse_args()
    element_of_IncomesOutcomes = IncomesOutcomes(args.date, args.category, args.amount, args.comment)

    
    if args.operation == "add_line":
        element_of_IncomesOutcomes.add_line(args.date, args.category, args.amount, args.comment)
    elif args.operation == "search_by_date": 
        element_of_IncomesOutcomes.search_by_date(args.date)
    elif args.operation == "search_by_category": 
        element_of_IncomesOutcomes.search_by_category(args.category)
    elif args.operation == "search_by_amount":
        element_of_IncomesOutcomes.search_by_amount(args.amount)
    elif args.operation == "show_amounts_by_date":
        element_of_IncomesOutcomes.show_amounts_by_date(args.date)
    elif args.operation == "update_line":
        element_of_IncomesOutcomes.update_line(args.num_line, args.pattern_changed, args.pattern_to_change)
    