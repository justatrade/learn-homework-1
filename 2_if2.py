"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""
def string_comparison(s1, s2):
    if type(s1) is not str or type(s2) is not str:
        return 0
    elif s1 == s2:
        return 1
    elif s1 != s2 and len(s1) > len(s2):
        return 2
    elif s1 != s2 and s2 == 'learn':
        return 3
    else: return "I don't know, what the hell is this)"


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    random_values = ["abc", 123, "python", "wxzz", "learn"]
    for i in range(len(random_values)):
        for j in range(len(random_values)):
            print(f'"{random_values[i]}" and "{random_values[j]}" result is '
                  f'{string_comparison(random_values[i], random_values[j])}')



if __name__ == "__main__":
    main()
