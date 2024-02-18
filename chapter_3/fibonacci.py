def fibonacci(i):
    if(i < 0): return 'Digite um número maior ou igual a 0'
    if(i == 0): return 0
    if(i == 1 or i == 2): return 1
    else: return (fibonacci(i - 1) + fibonacci(i - 2))

print(fibonacci(7))