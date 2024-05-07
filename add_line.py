def add_line(date, category, amount, comment ):
    with open ('our_file.txt', 'a') as f:
        f.write(f'\n{date}, {category}, {amount}, {comment}')

if __name__ == '__main__':
    add_line('g41', '45', 'rent5', 'Расход' )