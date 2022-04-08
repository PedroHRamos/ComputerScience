from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1} #This is a dictionary, that will be important to pre calculate the value of this indexes.

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2) #memoization - memoization theese results. It makes that is not necessary calculate theese values again
    return memo[n]

print(fib3(5))
print(fib3(10))
print(fib3(50)) #Now we can call this