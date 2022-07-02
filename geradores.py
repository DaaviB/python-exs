import sys
import time

# gerador -> interador -> intéravel

def gerador():
    for n in range(20):
        yield n 


lista = [x for x in range(200)]
gers = gerador()
gers_too = (x for x in range(20))

print(type(gers))  
print(type(lista))
print(type(gers_too))

print('bytes: ', sys.getsizeof(lista))
print('bytes: ', sys.getsizeof(gers))
print('bytes: ', sys.getsizeof(gers_too))

while True:
    try:
        print(next(gers))
    except StopIteration:
        break
