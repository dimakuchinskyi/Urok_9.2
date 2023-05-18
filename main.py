'''
#Ітератор
lst = [1,2,3,4,5,6,6]
print(iter(lst))
class MyIterator:
    def __init__(self, data):
        self.date = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value
for num in MyIterator(lst):
    print(num)

def my_generator(data):
    for item in data:
        yield item

for num in my_generator(lst):
    print(num)

def calc():
    def add(a, b):
        return a + b
    def sub(a, b):
        return a - b
    def mult(a, b):
        return a * b
    def div(a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError('Помилка! Ділення на нуль!')
    return add, sub, mult, div
add, sub, mult, div = calc()#Відбувається замикання
print(div(3, 1))
'''
#Лабороторна робота
#1
'''
class OddIterator:
    def __init__(self, n):
        if n <= 0:
            raise ValueError("N має бути додатнім числом")
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration("Досягнуто кінець ітерації")
        else:
            odd_number = self.current
            self.current += 2
            return odd_number
try:
    n = int(input("Введіть значення N: "))
    iterator = OddIterator(n)
    for num in iterator:
        print(num)
except ValueError as e:
    print("Помилка:", e)
except StopIteration as e:
    print("Помилка:", e)
'''
