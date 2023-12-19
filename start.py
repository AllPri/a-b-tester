from vyborki.razmer_vyborki import ravenstvo_doley, ravenstvo_srednego

print('Выберите действие:\n',
      '1 - расчет размера выборки для сравнения средних\n',
      '2 - расчет размера выборки для сравнения долей\n',)

x = int(input())
if x == 1:
    # получаем данные для расчета
    alpha = float(input('Уровень значимости теста: '))
    power = float(input('Уровень мощности теста: '))
    effect = float(input('Ожидаемый эффект: '))
    std = float(input('Стандартное отклонение: '))

    # проводим расчет
    ravenstvo_srednego(alpha, power, effect, std)

if x == 2:
    # получаем данные для расчета
    alpha = float(input('Уровень значимости теста: '))
    power = float(input('Уровень мощности теста: '))
    p1 = float(input('Доля событий до вмешательства: '))
    p2 = float(input('Доля событий после вмешательства: '))

    # проводим расчет
    ravenstvo_doley(alpha, power, p1, p2)

else: 'Ошибка ввода'