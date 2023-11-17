# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

# Input: 5
# Output: 6

A = 21
n1 = 0
n2 = 1
n = 2
fibonachiN = 1

while fibonachiN < A:
    
        fibonachiN = n1 + n2
        n1 = n2
        n2 = fibonachiN
        # n1, n2 = n2, n1 + n2
        
        n = n + 1
print (n)
if (fibonachiN) != A:
    print(-1)
# print(f'{n}' if fibonachiN == n else '-1')
