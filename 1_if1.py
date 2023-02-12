"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь:
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def what_to_do(age):
    age = int(age)
    if age < 7:
        return "Please ask your parents to get you to the kindergarten"
    elif age < 17:
        return "How dare you to play hooky the school lessons?!"
    elif age < 23:
        return "Go to the university and get this f%#king knowledge!"
    elif age < 65:
        return "Work hard!"
    else: return "You deserve to rest)"

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age = input("What's your age, mate? Type here: ")
    res = what_to_do(age)
    print(res)

if __name__ == "__main__":
    main()
