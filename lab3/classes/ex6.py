class Prime:
    def __init__(self, n_list):
        self.n_list = n_list

    def prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def filter_n(self):
        return list(filter(lambda x: self.prime(x), self.n_list))

i = input("Введите числа: ")
l = list(map(int, i.split()))
f = Prime(l)
p = f.filter_n()
print("Простые числа:", p)
