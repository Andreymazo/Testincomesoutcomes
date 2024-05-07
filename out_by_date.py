# import re
 # r = re.compile(f"{date}")
        # # result_lst = r.findall(lines)
        # result_lst = list(filter(r.match, lines))


def out_by_date(date):
    with open ('our_file.txt', 'r') as f:
        lines = [line.rstrip() for line in f]
        result_lst = []
        for i in lines:
            result_i = [x.strip() for x in i.split(',')]
            if result_i[0] == date:
                result_lst.append(result_i)
    print(result_lst)

if __name__ == '__main__':
    out_by_date('ggg')