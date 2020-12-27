
class Stack:
    def __init__(self):
        self.object = []

    def isEmpty(self):
        # проверка стека на пустоту. Метод возвращает True или False
        # Если пустой, то возвращает True
        return not self.object

    def push(self, new_element):
        # добавляет новый элемент на вершину стека. Метод ничего не возвращает.
        self.object.append(new_element)

    def pop(self):
        # удаляет верхний элемент стека. Стек изменяется.
        # Метод возвращает верхний элемент стека
        if not self.isEmpty():
            return self.object.pop()
        return None

    def peek(self):
        # возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
        if not self.isEmpty():
            return self.object[-1]
        return None

    def size(self):
        #  возвращает количество элементов в стеке.
        return len(self.object)


stack_example = Stack()
list_1 = '{}(()))'

def ok_or_not_ok(list):
    dict = {'(': ')',
            '[': ']',
            '{': '}'}

    for item in list:
        if dict.get(stack_example.peek(), None) == item:
            stack_example.pop()
        else:
            stack_example.push(item)

    if stack_example.isEmpty():
        return 'сбалансированный список'
    else:
        return 'несбалансированный список'

a = ok_or_not_ok(list_1)
print(a)
