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
class PrimeGenerator:
    def __init__(self):
        self.last_prime = 1

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate(self):
        while True:
            self.last_prime += 1
            try:
                if self.is_prime(self.last_prime):
                    yield self.last_prime
            except Exception as e:
                print(f"Виникла помилка: {str(e)}")
