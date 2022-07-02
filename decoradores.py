
from collections import deque


def default(*args, **kwargs):
    """Define um valor padrão.
    :args:
        - any
    :return: retorna um object(função).
    """
    def inner(func):
        def exec(*_, **__):
            return func(*args, **kwargs)
        return exec
    return inner

@default(2)
def cache(cache_len: int=None):
    """Armazena o cache.
    :args: 
        - cache_len: tamanho do cache
    :return: Retorna um object(função)
    
    """
    
    def inner(func):
        caching = deque(maxlen=cache_len)
        def exec(*args, **kwargs):
            caching.appendleft(args)
            print(caching)
            return func(*args, **kwargs)
        return exec
    return inner

@cache(9)
def soma(x, y):
    return x + y

print(soma(4,7))
print(soma(99,16))
print(soma(76,6))
print(soma(4,8))
print(soma(6,16))

