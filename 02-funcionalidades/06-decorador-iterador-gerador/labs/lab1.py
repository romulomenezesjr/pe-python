def log_decorator(fn):
    def fn_melhorada(*args, **kwargs):
        print(f"função '{fn.__name__}' iniciada com valores {args}")
        result = fn(*args, **kwargs)
        return result
    return fn_melhorada

@log_decorator
def soma(a,b):
    return a+b

@log_decorator
def fatorial(n):
    if n == 0:
        return 1
    if n > 0:
        return n*fatorial(n-1)

@log_decorator
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(soma(1,1))
print(fatorial(5))
print(fibonacci(5))


