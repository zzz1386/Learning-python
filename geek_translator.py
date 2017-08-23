# Переводчик с гикского на русский
# Демонстрирует использование словарей

geek = {"404" : "Не знать. не владеть информацией. От сообщения об ошибке 404 'Страница не найдена'.",
        "Googling" : "'Гугление'. nоиск в Сети сведений о ком-либо.",
        "Keyboard Plaque" : "Мусор. который скапливается в клавиатуре компьютера.",
        "Link Rot" : "Процесс устаревания гиперссылок на веб-страницах.",
        "Percussive Maintenance" : "О ситуации. когда кто-либо бьет по корпусу неисправного электронного прибора в надежде восстановить его работу",
        "Uninstalled" : "Об увольнении кого-либо. Особенно популярно на рубеже 1990-2000-х годов."}

choice = None
while choice != "0":
    print(
        """
Переводчик с гикского на русский
О - Выйти
1 Найти толкование термина
2 Добавить термин
3 Изменить толкование
4 Удалить термин
""")
    choiсе = input("Ваш выбор: ")
    print()
    
    if choice == "0":
        print("Дo свидания.")
    elif choice == "1":
        term = input("Про какой термин вы хотите узнать?: ")
        if term in geek:
            definition = geek[term]
            print("\n", term, "это", definition)
        else:
            print("\n К сожалению", term, "я пока не знаю. Но я быстро учусь)")
    elif choice == "2":
        term = input("Какой термин вы хотите добавить?")
        if term not in geek:
            definition = input("\nВпишите ваше толкование: ")
            geek[term] = definition   # Добавляет в словарь
            print("\nВы расширили словарь значением ", term)
        else:
            print("\Это уже было! не надо шутить так")
    elif choice == "3":
        term = input("\nРасшифровку какого термина вы хотели бы поменять?: ")
        if term in geek:
            definition = input("\Введите новое толкование этого слова: ")
            geek[term] = definition   # то же самое, но теперь меняет толкование
            print("\nОтныне ", term, "значит ", definition)
        else:
            print("\nНу нет такого термина", term, "\nМожет добавишь?")
    elif choice == "4":
        term = input("\nКакой термин вы хотите удалить?: ")
        if term in geek:
            del geek[term]
            print("\n", term, "успешно удален")
        else:
            print("Чтобы что то удалить, надо сначала это создать.Так что не стесняйся, жми 2")
    else:
        print("\nОстановитесь, выдохните. И еще раз ВНИМАТЕЛЬНО посмотрите на цифры меню")

input("\n\nНажмите Еnter для выхода")

