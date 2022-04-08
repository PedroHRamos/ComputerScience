from typing import Generator

def fib6( n: int ) -> Generator[ int, None, None ]:
    yield 0             #caso especial
    if n > 0: yield 1   #caso especial
    last: int = 0
    next: int = 1
    for _ in range( 1, n ):
        last, next = next, last + next
        yield next      #passo principal da geração


for i in fib6(50):
    print(i)