def sumatorio(n):
    if n > 0: #cuando n llegue a 0 no hará nada y parará la función.
        return n + sumatorio(n-1)
    else:
        return 0
    
print(sumatorio(4))

def factorial(n):
    if n != 0:
        return n * sumatorio(n-1)
    else:
        return 0