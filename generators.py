import time


def fibo_gen(max):
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
            if max == 0:
                return
        elif counter == 1:
            counter += 1
            yield n2
            if max == 1:
                return
        else:
            if counter != max:
                aux = n1 + n2
                n1, n2 = n2, aux
                counter += 1
                yield n2
            else:
                return


if __name__ == '__main__':
    fibonacci = fibo_gen(10)
    for element in fibonacci:
        print(element)
        time.sleep(.05)
