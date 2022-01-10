from datetime import datetime

def messure_time(function):
    def wrapper(*args,**kwargs):
        import time

        start = time.time()
        result = function(*args,**kwargs)
        total = time.time()- start
        print(total,' Seconds')

        return result
    return wrapper

@messure_time
def suma(a,b):
    import time
    time.sleep(1)
    return a + b

## Otro

def execution_time(func):
    def wrapper(*args,**kwargs):
        initial_time = datetime.now()
        func(*args,**kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron "  + str(time_elapsed.total_seconds()))
    return wrapper

@execution_time
def random_func():
    for _ in range(1,1000000):
        pass


## un decorador que recibe tambien parametro

def my_decorator_name(name):
    def my_custome_decorator(function):
        def wrapper(*args, **kwargs):

            print('Name:', name)
            return function(*args, **kwargs)

        return wrapper

    return my_custome_decorator

@my_decorator_name('CodigoFácilito')
def suma(a, b):
    return a + b

# Una desventaja de los decoradores es que se pierden
# los atributos de las funciones para evitar eso. 
# se le pasa los atributos del la función al decorador
from functools import wraps
def debug(f):
    @wraps(f) # decorador standart que copia los atributos de la 
              # funcion original a la nueva 
    def new_function(*args, **kwargs):
        print(f"Function {f.__name__}() called!")
        return f(*args, **kwargs)
    return new_function

def run():
    random_func()

if __name__ == '__main__':
    run()