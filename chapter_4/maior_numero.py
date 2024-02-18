def maiorNumero(arr):
    if(len(arr) == 2): return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = maiorNumero(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

print(maiorNumero([1, 21, 3, 2, 3, 210]))
print(maiorNumero([1, 3, 2, 3, 210]))
print(maiorNumero([1, 2, 3, 210]))