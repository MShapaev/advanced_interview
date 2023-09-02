class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if self.stack:
            return True
        return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        item = self.stack.pop()
        return item

    def peek(self):
        item = self.stack[-1]
        return item

    def size(self):
        return len(self.stack)


def main():
    list = Stack()  # Создаем экземпляр класса стек с пустым списком
    # test_string = '{{[(])]}}'
    test_string = input('Введите тестовую строку для проверки: ')
    flag = True  # Пусть строка сразу сбалансирована
    for i in test_string:
        if i in '[({':  # если элемент проверочной строки является открывающим - добавляем в стек методом push
            list.push(i)
        elif i in '])}':  # Если он закрывающий - и если стек не пустой - берем его и сравниваем с верхним элементом стека
            if not list.size():
                flag = False
                break
            item = list.pop()

            if item == '(' and i == ')':  # Если закрывающий элемент списка соответствует верхнему из стека - удаляем верхний
                continue  # и идем дальше до конца строки. Если все элементы зеркальны: flag = True
            if item == '[' and i == ']':
                continue
            if item == '{' and i == '}':
                continue
            flag = False  # Если скобка не отзеркалилась - flag = False , прекращаем программу
            break
    if flag and not list.size():  # Если flag == True и стэк пустой ( значит у всех скобок нашлась пара), выводим ответ
        print('Сбалансированно')
    else:
        print('Не сбалансированно')


if __name__ == '__main__':
    main()
