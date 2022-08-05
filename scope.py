y = 5


def my_func():
    y = 3

    def my_other_func():
        y = 2
        print(y)
    my_other_func()
    print(y)


my_func()

print(y)
