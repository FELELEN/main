'''
# 1. Логика игры

import random
print('Здравствуй, ты попал в казино "ТРИ ТОПОРА"')
print('---Правила!---')
print('1.Введи свой капитал: ')
print('2.Выбери число от 1 до 3: ')
print('3.Делай ставку, она удвоится в два раза:')

money = 1000
bet = 100
choosing = 1
count = 1
while True:
    money -= 100 
    rand_number = random.randint(1,3)
    if rand_number == 1:
       money += 100*2
       print('Выигрыш')
    else:
       print('Проигрыш')
    print(f'{count}.Ваши деньги :{money}')
    count += 1
    
    if money <= 0:
        print('Игра окончена')
        break
'''     
        
# 2. Пользовательский ввод
'''
import random

print('Здравствуй, ты попал в казино "ТРИ ТОПОРА"')
print('---Правила!---')
money = int(input('Введи свой капитал: '))
count = 1
while money > 0:
    rand_number = random.randint(1,3)
    choosing = int(input('Выбери число от 1 до 3: '))
    bet = int(input('Делай ставку, она удвоится в два раза: '))
    money = money - bet
    if rand_number == choosing:
        money += bet*2
        print('Ты удвоил ставку!')
        print(f'{count}.Ваши деньги :{money}')
        count += 1
    else:
        print('Твоя интуиция подвела тебя.')
        print(f'{count}.Ваши деньги :{money}')
        count += 1
        print('Хотите продолжить?')
    print('Нажмите "Enter" чтобы продолжить или напишите "q" чтобы выйти.')
    if input() != '':
            break
'''       
# 3. Проверки входных данных и исключения

import random

print('Здравствуй, ты попал в казино "ТРИ ТОПОРА"')
print('---Правила!---')
count = 1
while True:
    try:
        money = input('Введи свой депозит: ')
        money = int(money)
        assert money >= 0, ''
    except ValueError:
        print('Пиши числами!')
    except AssertionError:
        print('Не допутимое значение!')
    else:        
        while True:
            try:
                choosing = int(input('Выбери число от 1 до 3: '))
                assert choosing < 4 and choosing > 0, ''
            except ValueError:
                print('Пиши числами!')
            except AssertionError:
                print('Не допутимое значение!')
            else:
                try:
                    bet = int(input('Делай ставку, она удвоится в два раза: '))
                    assert bet <= money and bet > 0, ''
                except ValueError:
                    print('Пиши числами!')
                except AssertionError:
                    print('Не допутимое значение!')
                else:
                    rand_number = random.randint(1,3)
                    money = money - bet
                    if rand_number == choosing:
                        money += bet*2
                        print('Ты удвоил ставку!')
                        print(f'{count}.Ваши деньги :{money}')
                        count += 1
                    else:
                        print('Твоя интуиция подвела тебя.')
                        print(f'{count}.Ваши деньги :{money}')
                        count += 1
                    print('Хотите продолжить?')
                    print('Нажмите "Enter" чтобы продолжить или напишите "q" чтобы выйти.')
                    if input() != '':
                        break
                        
    if money <= 0:
        print('Игра окончена')
        break