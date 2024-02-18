def conta(arr):
    if(arr == []): return 0
    else:
        arr.pop(0)
        total = 1 + conta(arr)
    return total

# Livro
# def conta(arr):
#     if(arr == []): return 0
#     return 1 + conta(arr[1:])

print(conta([1, 2, 3, 10, 30, 91]))