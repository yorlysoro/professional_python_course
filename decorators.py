from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        total_time = final_time - initial_time
        print("Pasaron " + str(total_time.total_seconds()) + " segundos")
    return wrapper


@execution_time
def random_func():
    for _ in range(1, 100000):
        pass


@execution_time
def suma(a: int, b: int) -> int:
    return a + b


@execution_time
def saludo(nombre="Cesar"):
    print("Hola " + nombre)


random_func()
suma(5, 5)

saludo()


def with_custom_message(message):
    def with_message(function):
        print(f"{message}:")

        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
        return wrapper
    return with_message


@with_custom_message("Hello")
def multiply(a, b):
    c = a * b
    print(f"The result of {a} * {b} is {c}")


multiply(10, 2)
