def hello(): #Приветствие
    print("Приветствую в калькуляторе привычек.")

def choose(): #глав меню
    voit = int(input("Выберите что вы хотите: \n"
                                "1. Рассчёт времени привычки \n"
                                "2. Выйти \n"))
    if voit == 1:
        habits()
    elif voit == 2:
        print("Завершение программы")
        exit()

def habits(): #привычка и время
    name = input("Введите имя привычки:")
    flag = False
    while not flag:
        habits_time = int(input("Выберите формат времени: \n"
                                "1. Часы \n"
                                "2. Минуты \n"
                                "3. Секунды \n"))
        if habits_time == 1:
            habits_calc_hour(name)
            flag = True
            return name, habits_time

        elif habits_time == 2:
            habits_calc_min()
            flag = True
            return name, habits_time

        elif habits_time == 3:
            habits_calc_sec()
            flag = True
            return name, habits_time

        else:
            print("Ошибка, введите цифру от 1 до 3.")


def habits_calc_hour(name): #калькулятор часов
    t = int(input("Введите время: "))
    month_hour = t * 30
    year_hour = month_hour * 12
    if t > 8:
        print("Как ты собрался тратить", t, "часов в день на " f'{name}' "?")
        return habits()
    elif 8 >= t >= 5:
        print(f'{name}' " каждый день по", t, "часов довольно серьёзно. "
            "Это", month_hour, "часов в месяц и", year_hour, "часов в год. "
              "Уверен, что справишься?")
        return habits()
    elif 5 > t >= 2:
        print(f'{name}' " каждый день по", t, "часа в день звучит как хорошая цель. "
            "Это", month_hour, "часов в месяц и", year_hour, "часов в год. ")
        return habits()
    elif t == 1:
        print(f'{name}' " каждый день по", t, "часу это прекрасное начало. "
            "Это", month_hour, "часа в месяц и", year_hour, "часов в год. ")
        return habits()

def habits_calc_min(): #калькулятор минут
    t = int(input("Введите время: "))
    month_hour = (t * 30)/60
    year_hour = (month_hour * 12)
    if t >= 10:
        print("Ты готов тратить", t, "минут на своё занятие? Это", month_hour, "часов в месяц и", year_hour, "в год!"
              "Это хорошая инвестиция в себя.")
        return



def habits_calc_sec(): #калькулятор секунд
    t = int(input("Введите время: "))
    month_hour = (t * 30)/60
    year_hour = (month_hour * 12)
    if t >= 10:
        print("Ты готов тратить", t, "минут на своё занятие? Это", month_hour, "часов в месяц и", year_hour, "в год!"
              "Это хорошая инвестиция в себя.")
        return

if __name__ == "__main__":
    hello()
    choose()