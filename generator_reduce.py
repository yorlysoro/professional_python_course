from time import sleep


def fibo_gen(max):
    a, b = 0, 1
    for _ in range(max):
        yield a
        a, b = b, a+b


if __name__ == '__main__':
    fibonacci = fibo_gen(10)
    for element in fibonacci:
        print(element)
        sleep(.05)
