lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binarySearch(list, object):
    lower = 0
    higher = len(list) - 1

    while(lower <= higher):
        mid = (higher + lower) // 2
        guess = list[mid]

        if(guess == object): return mid
        elif(guess < object): lower = mid + 1
        else: higher = mid - 1
    
    return None

print(binarySearch(lista, 88))