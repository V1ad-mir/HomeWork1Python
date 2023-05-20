# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no


numberStorona1 = int(input("Введите количество долек по первой стороне шоколадки : "))
numberStorona2 = int(input("Введите количество долек по второйй стороне шоколадки : "))
numberDolek = int(input("Введите количество долек, которое необходимо отломить  : "))
if (numberDolek%numberStorona1==0 and numberDolek/numberStorona1<numberStorona2) or (numberDolek%numberStorona2==0 and numberDolek/numberStorona2<numberStorona1):
    print('yes')
else: 
    print('no')
