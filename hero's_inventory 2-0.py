
# Арсенал героя
# Демонстрирует создание кортежа
# создадим пустой кортеж
inventory = ()
# рассмотрим его как условие
if not inventory:
    print("Вы безоружны.")
input("\nHaжмитe Enter. чтобы продолжить.")
# теперь создадим кортеж с несколькими элементами
inventory = ["меч" ,
             "кольчуга",
             "щит" ,
             "целебное снадобье"]
# выведем этот кортеж на экран
#print("\nСодержимое кортежа: ")
#print(inventory)
# выведем все элементы последовательно
print("\nПосле доната в вашем арсенале:")
for item in inventory:
    print(item)
input("\nHaжмитe Enter . чтобы продолжить. ")


# Арсенал 2.0

print("\nСейчас в вашем распоряжении ", len(inventory), " предмета/-ов.")
input("Haжмитe Enter . чтобы продолжить. ")
print("\nВы еще поживете и повоюете")
index = int(input("Введите порядковый номер одного из предметов арсенала: ")) 
print("Под номером ", index, " в арсенале находится ", inventory[index])
low = None
attempts = 0
while low != "":
    low = int(input("Введите начальный индекс среза: "))
    high = int(input("Введите конечный индекс среза: "))
    attempts += 1
    print("Срез inventory[ ", low, " : ", high, " ] - это (", inventory[low:high], ")")
    if attempts > 0:
        break
input("\nHaжмитe Enter . чтобы продолжить. ")


box = ("золото",
       "драгоценные камни")
print("Вы нашли ларец. Вот что в нем есть:")
print(box)
print("Вы приобщили содержимое ларца к своему арсеналу. \nТеперь в вашем распоряжении: ")
print(inventory + box)
input("\n\nHaжмитe Enter . чтобы выйти. ")
