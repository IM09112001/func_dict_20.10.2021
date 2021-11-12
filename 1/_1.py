# Написать функцию которая принимает в аргумент номер месяца, а выводит его название 

#Пример: 
#monthNumToString(2) -> ‘February’
#monthNumToString(12) -> ‘December’

month={
    1:"January",
    2:'february',
    3:'march',
    4:'aprel',
    5:'may',
    6:'iyun',
    7:'iyul',
    8:'avgust', 
    9:'sentabr',
    10:'oktabr',
    11:'noyabr',
    12:'dekabr'
    }
k=True

while k==True:
    n=input("Введите число месяца в интервале [1; 12]: ")
    if n!=int(): k=False
    elif n>0 and n<13:       
        print("monthNumToString{0} -> {1}".format(n, month[n]))
    else: 
        k=False



