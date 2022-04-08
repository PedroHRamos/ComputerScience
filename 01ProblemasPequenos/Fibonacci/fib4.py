from functools import  lru_cache

#esse max size indica qual é o limite de chamadas recentes devem ser armazenadas em cache, None indica que não há limite
@lru_cache(maxsize=None)
def fib4(n: int) -> int: #mesma definição de fib2()
    if n < 2: #caso de base
        return n
    return fib4( n - 2 ) + fib4( n - 1 )

print (fib4(5))
print (fib4(50))