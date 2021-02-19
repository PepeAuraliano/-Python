#Задание 1
age = int(input("Сколько вам лет?"))
print(age)

#Задание 2
user_time = int(input("Введите время в сек.: "))
hours = user_time // 3600
minutes = (user_time - hours) / 3600
seconds = user_time - (hours * 3600 + minutes * 60)
print(f"{hours}:{minutes}:{seconds}")


#Задание 3
n = input("Введите целое неотрицательное число: ")
nn = n + n
nnn = n + n + n
sum(__iterable = n + nn + nnn, start = 0)
print(n + nn + nnn)

#Задание 4


user_number = abs(int(input("Введите целое число: ")))
max_number = 0
while user_number > 0: # True or False
    item = user_number % 10
    if item >= max_number:
        max_number = item


        user_number = user_number // 10
        print(max_number)

        #Задание 5

revenue_user = int(input("Какая у вас выручка?"))
cost_user = int(input("Какие у вас издержки?"))
if revenue_user > cost_user:
    print("Прибыль")

else: print("Убыток")
profit_user = revenue_user - cost_user
size_user = profit_user // revenue_user
if revenue_user > cost_user:
 print(size_user)

employee_user = int(input("Какая численность сотрудников?"))
count_user = revenue_user // employee_user
if revenue_user > cost_user:
    print(count_user)

#Задание 6

#К сожалению, не понял как решить - а именно как ввести подсчет дней и согласовать его с километражом