def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n - 1) + fib2(n - 2)

print(fib2(5))
print(fib2(10))
#print(fib2(50)) This call take a time and I interrupt, I saw my processor begin in 1% in visual studio code to 9%