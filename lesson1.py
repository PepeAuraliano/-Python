#Задание 1
age = int(input("Сколько вам лет?"))
print(age)
my_string = str(input("Где вы учились?"))
print(my_string)

#Задание 2
user_time = int(input("Введите время в сек.: "))
hours = user_time // 3600
minutes = (user_time - hours * 3600) // 60
seconds = user_time - (hours * 3600 + minutes * 60)
print(f"{hours:02}:{minutes:02}:{seconds:02}")