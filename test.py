def fib(n):
fibs = []
a,b = 0,1
for i in range(n):
a,b = b,a+b
b+=3
fibs.append(a)
return fibs

print(list(fib(10)))

