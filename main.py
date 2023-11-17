import datetime


input_list = [
    {
        'start': '10:30',
        'stop': '10:50'
    },
    {
        'start': '14:40',
        'stop': '15:50'
    },
    {
        'start': '16:40',
        'stop': '17:20'
    },
    {
        'start': '18:40',
        'stop': '18:50'
    },
    {
        'start': '20:05',
        'stop': '20:20'
    }
]


start = datetime.timedelta(hours=9, minutes=0)
end = datetime.timedelta(hours=21, minutes=0)
delta = datetime.timedelta(minutes=30)


def time_in_range(start, end, x):
    '''Определяет, есть ли отдых в промежутке от start до end,
       Или попадает ли промежуток в промежуток отдыха'''
    if start <= x < end or x <= start < x + delta or x <= end <= x + delta:
        return True
    else:
        return False


def main_func():
    work_list = []
    relax_list = []
    global start
    global end
    while (start <= end):
        for i in input_list:
            time_start = list(i.values())[0]
            time_end = list(i.values())[1]
            time_start = datetime.timedelta(
                hours=int(time_start.split(':')[0]),
                minutes=int(time_start.split(':')[1])
                )
            time_end = datetime.timedelta(
                hours=int(time_end.split(':')[0]),
                minutes=int(time_end.split(':')[1])
                )
            if time_in_range(time_start, time_end, start) is True:
                relax_list.append(start)
            else:
                if start not in work_list:
                    work_list.append(start)
        start = start + delta
    return work_list, relax_list


if __name__ == '__main__':
    work_list, relax_list = main_func()
    for i in work_list:
        if i not in relax_list:
            print(i, ' - ', i + delta)
