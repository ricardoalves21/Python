#Fatorial recursivo
def fatorial_recursivo(n):
    fat = 1
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return  fat
    else:
        return n * fatorial_recursivo(n-1)

print(fatorial_recursivo(5)) # resultado: 120