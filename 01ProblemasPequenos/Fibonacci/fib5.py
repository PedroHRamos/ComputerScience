def fib5( n: int ) -> int:
    if n == 0: return n #caso especial
    last: int = 0 # inicialmente definido para fib(0)
    next: int = 1 # inicialmente definido para fib(1)
    for _ in range( 1 , n ):
        last, next = next, last + next #Demasiadamente complexo, abre muito a mão da legibilidade por concisão, mas funciona bem, vide rodapé 1
    return next

print(fib5(5))
print(fib5(50))


#1 -    last é definido com o valor anterior de next, next tem o valor anterior de last + valor anterior de next
#       isso poupa a criação de uma variável temporária(achei desnecessário esse nível de otimização visto o sacrifício de legibilidade).

#OBS: Apesar das complicações esse for executará no máximo n-1 vezes, enquanto fib2 faz 21891 chamadas para o número 20
#A recursão pode até ser a forma mais intuitiva visto que é uma tradução literal do problema de Fibonacci em código, mas nem de longe é a solução mais performática neste contexto