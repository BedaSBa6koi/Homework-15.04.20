print('Время 1:\n')
hours_1=int(input('Введите часы >> '))
minutes_1=int(input('Введите минуты >> '))
seconds_1=int(input('Введите секунды >> '))
print('Время 2:\n')
hours_2=int(input('Введите часы >> '))
minutes_2=int(input('Введите минуты >> '))
seconds_2=int(input('Введите секунды >> '))

if hours_2<hours_1:
    print('Второе время должно быть больше первого')
    exit()
else:
    hours_res=hours_2-hours_1

if minutes_2<minutes_1:
    hours_res-=1
    minutes_2+=60
minutes_res=minutes_2-minutes_1

if seconds_2<seconds_1:
    minutes_res-=1
    seconds_2+=60
seconds_res=seconds_2-seconds_1

secs=hours_res*60*60+minutes_res*60+seconds_res

print('Между двумя моментами ' + str(secs) + ' секунд')
