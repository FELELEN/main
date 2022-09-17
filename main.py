money = int(input('Введи свой депозит: '))
choosing = int(input('Выбери число от 1 до 3: '))
bet = int(input('Делай ставку, она удвоится в два раза: '))
count = 1
try:
   assert choosing < 4 and choosing > 0, ''
   assert bet <= money, ''
except ValueError:
   print('Введи числами!')
except AssertionError:
   print('Что-то не так! Попробуй-ка ввести опять')
else:
   print('ахахахаахах')