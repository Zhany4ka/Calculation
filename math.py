import math
import random
print('Привет , это мой первый проект , не судите строго')
#Denote the variable and type
a=int(input('Введите данные первой переменной:'))
d=int(input('Что вы хотите ? все каждому или все сразу?'))
#Checking the type of information received
if (d == 0):
    c=int(input('Что вы хотите сделать с переменной?'))
#Structure of the first option
def math1(a):
   if (c == 1 ):
        print('Модуль числа: ', a ,
              'Равен:' , abs(a))
   elif (c == 2):
        print('Преобразование к общему числу: ' ,int(a))
   elif (c == 3):
        print('Округление числа' , a ,
              'Равно' , round(a))
   elif (c == 4):
        print('Квадратный корень числа ' , a , 'Равно:' , math.sqrt(a))
   elif (c == 5):
        print('Cинус угла в ', a , 'градусов ' , 'Равен:' , math.sin(a))
   elif (c == 6):
        print('Косинус угла в ' , a , 'градусов ' , 'Равен:' , math.cos(a))
   elif (c == 7):
        print('Екпонент числа ' , a , 'Равен' , math.exp(a))
   elif (c == 8):
        print('Натуральный логорифм числа ' , a , 'Равен' , math.log(a))
   elif (c == 9):
        print('Округление вниз числа ' , a , 'Равен' , math.floor(a))
   elif (c == 10):
        print('Округление вверх числа ' , a , 'Равен' , math.ceil(a))
   else:
        print('Неверный тип операции')
#Structure of the second option
def math2(a):
   if (d == 0):
      math1(c)
   elif (d == 1):
    print('Модуль числа:',  abs(a))
    print('Преобразование к общему числу:' ,int(a))
    print('Округление:'  , round(a))
    print('Квадратный корень:' , math.sqrt(a))
    print('Cинус угла равен:' , math.sin(a))
    print('Косинус угла равен:' , math.cos(a))
    print('Екпонент числа равен:' , math.exp(a))
    print('Натуральный логорифм числа равен:' , math.log(a))
    print('Округление вниз числа равен:' , math.floor(a))
    print('Округление вверх числа равен:' , math.ceil(a))
   else:
    for i in range(5):
        print(random.randint(1365546,2637729))
math2(a)

