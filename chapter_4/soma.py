def soma(arr):
    if(arr == []): return 0
    else:
      total = arr[0]
      arr.pop(0)
      total += soma(arr)
    return total

# Livro
# def soma(arr):
#     if(arr == []): return 0
#     return arr[0] + soma(arr[1:])

print(soma([1, 2, 3, 4, 5, 6, 7, 8, 9]))