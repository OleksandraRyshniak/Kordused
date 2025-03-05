# 3 Вариант

# 1 Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n скворечников. Между двумя соседними скворечниками также имеется пустой (из пробелов) столбец. Разрешается вывести пустой столбец после последнего скворечника. Для упрощения рисования скопируйте скворечник из примера в среду разработки.
#    -----
#   |  O  |
#   !  -  !
 #   -----
print("Ül 1")
try:
    n=int(input("Sisestage number vahemikus 1 kuni 9:"))
except:
    print("Vale formaat!")
for i in range(n):
    print(" ----- ",end=" ")
print( )
for i in range(n):
    print("|  0  |",end=" ")
print( )
for i in range(n):
    print("!  -  !",end=" ")
print( )
for i in range(n):
    print(" ----- ",end=" ")
print( )


# 2 Вывести степени натуральных чисел, не превосходящие данного числа n**3. Пользователь задает показатель степени и число n.
print("Ül 2")
while True: 
    try:
        n=int(input("Sisesta arv: "))
    except:
        print("Vale formaat!")
    if n<=0:
        print("Arv peab olema positiivne.")
    else:
        try: 
            p=int(input("Sisestage indikaator:"))
        except:
             print("Vale formaat!")
        if p<=0:
            print("Indeks peab olema positiivne.")
        else:
            vastus=n**p
            if vastus<=n**3:
                print(f"Arv {n}, mille aste {p} on {vastus}")
            else: 
                ("Indeks peab olema väiksem.")
    break

# 3 Известны оценки по физике каждого из  учеников класса. Определить среднюю оценку. (Оценки и количество учеников получаем случайным образом)
print("Ül 3")
import random
summ=0
k=random.randint(10,30)
for i in range (k):
    hinne=random.randint(2,5)
    summ+=hinne
    kesk_hinne=round(summ/k,1)
print(f"Õpilasi klassis kokku: {k}")
print(f"Füüsika keskmine hinne :{kesk_hinne}")


# # 4 Мой богатый дядюшка подарил мне один доллар в мой первый день рождения. В каждый день рождения он увеличивал свой подарок и прибавлял к нему столько долларов, сколько лет мне исполнилось. Написать программу, указывающую, к какому дню рождения подарок превысит 100$.
print("Ül 4")
vanus=1
kingitus=1
while kingitus<=100:
    vanus+=1
    kingitus+=vanus
    print(f"Ma saan sel aastal {vanus} ja ma saan sel aastal {kingitus}.")
print(f"Aastaks {vanus} ületab kingitus 100 dollarit.")


# 5 При помощи цикла распечатать ряд Фибоначчи: 0 1 1 2 3 5 8 13 21. (Первые два числа равны 0 и 1, 
# а каждое последующее число равно сумме двух предыдущих чисел.)
print("Ül 5")
a=0
b=1
for i in range(9):
    print(a, end=" ")
    v=a
    a=b
    b=v+b