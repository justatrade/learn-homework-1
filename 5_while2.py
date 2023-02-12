"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую

"""

questions_and_answers = {
    "How are you?": "Fine",
    "What are you doing?": "I'm developing now",
    "What's the plan for the evening?": "To have fun!)"
}

def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    while True:
        ask = input("Ask me something: ")
        if ask in questions_and_answers:
            print(questions_and_answers[ask])

if __name__ == "__main__":
    ask_user(questions_and_answers)
