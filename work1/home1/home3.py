'''3. Реализовать функцию, которая принимает три позиционных аргумента и возвращает
сумму наибольших двух из них.'''

a = int(input("First: "))
b = int(input("Second: "))
c = int(input("Third: "))

if a < b:
    minimal = a
else:
    minimal = b
if c < minimal:
    minimal = c
res = a + b + c - minimal

print("Summa: ", res)