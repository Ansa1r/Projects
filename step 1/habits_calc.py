from sys import flags

from unicodedata import name


def hello(): #Приветствие
    print("Приветствую в калькуляторе привычек.")

def habits():
    name = input("Введите имя привычки:")
    flag = False
    while not flag:
        habits_time = int(input("Выберите формат времени: \n"
                                "1. Часы \n"
                                "2. Минуты \n"
                                "3. Секунды \n"))
        if habits_time == 1:
            habits_calc_hour()
            flag = True
            return name, habits_time, habits_calc_hour()

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


def habits_calc_hour(name): # основная функция
    t = int(input("Введите время: "))
    month_hour = t * 30
    year_hour = month_hour * 12
    if t > 8:
        print("Как ты собрался тратить", t, "часов в день на" f'{name}' "?")
        return habits()


def habits_calc_min(): # основная функция
    t = int(input("Введите время: "))
    month_hour = (t * 30)/60
    year_hour = (month_hour * 12)
    if t >= 10:
        print("Ты готов тратить", t, "минут на своё занятие? Это", month_hour, "часов в месяц и", year_hour, "в год!"
              "Это хорошая инвестиция в себя.")
        return



def habits_calc_sec(): # основная функция
    t = int(input("Введите время: "))
    month_hour = (t * 30)/60
    year_hour = (month_hour * 12)
    if t >= 10:
        print("Ты готов тратить", t, "минут на своё занятие? Это", month_hour, "часов в месяц и", year_hour, "в год!"
              "Это хорошая инвестиция в себя.")
        return

if __name__ == "__main__":
    hello()
    habits()