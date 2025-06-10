def prime(numbers):
    p_num=[]
    for n in numbers:
        if n > 1:
            for i in range(2, n):
                if (n % i == 0):
                    break
            else:
                p_num.append(n)
    print(p_num)
nums=input()
numbers=[]
for n in nums.split():
    numbers.append(int(n))
prime(numbers)