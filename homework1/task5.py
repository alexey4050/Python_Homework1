''' Напишите программу программу, которая принимает на вход цифру,
обозначающую день недели, и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> нет
- 2 -> нет '''

dayWeek= int(input('Введите число от 1 до 7: '))
if 1 <= dayWeek <= 5:
    print(f'{dayWeek} - сегодня рабочий день')
elif dayWeek == 6 or dayWeek == 7:
    print(f'{dayWeek} - сегодня выходной')
else:
    print(f'это не день недели')