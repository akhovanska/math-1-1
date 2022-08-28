#Встановити рівень навчальних досягнень учня (початковий, середній, достатній, високий) відповідно до заданої оцінки (від 1 до 12).



n = int(input())
if 1 <= n <= 3:
    print("Initial")
elif 4 <= n <= 6:
    print("Average")
elif 7 <= n <= 9:
    print("Sufficient")
elif 10 <= n <= 12:
    print("High")
