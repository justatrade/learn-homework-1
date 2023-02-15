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
    if not isinstance(s1, str) or not isinstance(s2, str):
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
    for i in random_values:
        for j in random_values:
            print(f'"{i}" and "{j}" result is '
                  f'{string_comparison(i, j)}')



if __name__ == "__main__":
    main()
