class Stack:
# Класс Стек

    def __init__(self, stack):
        self.stack = stack

    def is_empty(self):
    # Метод проверяет пустой ли стек
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, item):
    # Метод добавляет элемент в стек
        self.stack.append(item)

    def pop(self):
    # Метод удаляет элемент из стека
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def peek(self):
    # Метод возвращает последний элемент стека
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def size(self):
    # Метод возвращает размер стека
        return len(self.stack)


def is_balanced(string):
# Функция принимает на входе строку, состоящую из символов скобок: ()[]{}
# а на выходе выдаёт заключение о расположении скобок: "Сбалансированно" или "Несбалансированно"
    closing_brackets = Stack([]) # Стек, заполняемый только закрывающими скобками
    brackets = Stack(list(string)) # Стек, заполняемый разными скобками из входной строки

    # Проверка на корректность скобок

    string_len = len(string)
    if string_len % 2 != 0:
        return 'Несбалансированно' # Нечётное количество символов в исходной строке

    for i in range(string_len):
        if (string[i] != '}' and string[i] != ')' and string[i] != ']'
                and string[i] != '{' and string[i] != '(' and string[i] != '['):
            return 'Несбалансированно' # В исходной строке содержатся не только скобки

    # Проверка на сбалансированность скобок

    counter = 0
    for i in range(string_len):

        bracket = brackets.pop()
        if bracket == '}' or bracket == ')' or bracket == ']':
            closing_brackets.push(bracket)
        else:
            closing_bracket = closing_brackets.pop()
            if closing_bracket == ')':
                if bracket == '(':
                    continue
            elif closing_bracket == ']':
                if bracket == '[':
                    continue
            elif closing_bracket == '}':
                if bracket == '{':
                    continue
            return 'Несбалансированно'
    return 'Сбалансированно'

# Тестирование
if __name__ == '__main__':
        # stack = Stack(list('557'))
        # print(stack.stack)
        # print(stack.pop())
        # for i in range(10):
        #     stack.push(i)
        # # Проверка задачи №1
        # print(stack.peek())
        # print(stack.size())
        # print(stack.pop())
        # print(stack.peek())
        # print(stack.size())

    strings = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]', '[[{h))}]',
                '[[{h)}}(', '}[{h)}}]']
    for string in strings:
        print(string, '-', is_balanced(string))

