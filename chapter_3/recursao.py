def fat(num):
    if(num < 0): return 'Insira um número válido'
    elif(num == 0): return 1
    elif(num == 1): return 1
    else: return num * fat(num - 1)


print(fat(998)) #Limite de cálculo 998