# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

sum = int(input("Общее число сделанных журавликов: "))
if sum%6>0:
  print (f'Цело численного решения соответствующего условиям задачи нет ')
  print (f'Петя сделал: {int(sum/6)} журавликов')
  print (f'Катя сделала: {int(sum/6)*4} журавликов')
  print (f'Сережа сделал: {int(sum/6)} журавликов')
  print (f'Помогая друг другу было сделано: {(sum - int(sum/6)*6)} журавликов')
else:
  print (f'Петя сделал: {int(sum/6)} журавликов')
  print (f'Катя сделала: {int(sum/6)*4} журавликов')
  print (f'Сережа сделал: {int(sum/6)} журавликов')