# TestIncomesOutcomes
TestIncomesOutcomes


 - Task
        ![worktime](/media/Screenshot%20from%202024-05-05%2022-31-12.png)


argsparser подает параметры через консоль. 

# команды

- python IncomesOutcomes.py -date 2323-02-21 search_by_date;
- python IncomesOutcomes.py -amount 25 search_by_amount;
- python IncomesOutcomes.py -category Доход search_by_category;
- python IncomesOutcomes.py -amount 25 search_by_amount;
- python IncomesOutcomes.py -date 2323-02-21 -category Доход -amount 25 -comment аренда add_line;
- python IncomesOutcomes.py -date 25 show_amounts_by_date;
- python IncomesOutcomes.py -num_line 1 -pattern_changed category -pattern_to_change Доход update_line;
- python IncomesOutcomes.py -num_line 2 -pattern_changed category -pattern_to_change Расход update_line;
- python IncomesOutcomes.py -num_line 2 -pattern_changed amount -pattern_to_change 35 update_line;

# Туду:

Пагинация и лучше тинкером с кнопкой и красиво будет, а то если записей тыща, и не разберешься чего изменять и где.
тоесть вывод нормальный с перелистыванием.