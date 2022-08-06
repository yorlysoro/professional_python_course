# Hola 3 -> HolaHolaHola
# Facundo 2 -> FacundoFacundo
# Platzi 4 -> PlatziPlatziPlatziPlatzi


def make_repeater_off(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string * n
    return repeater


def make_division_by(n):
    def divide(x):
        assert n != 0, f"No se puede realizar division por {n}"
        return x / n
    return divide


def run():
    repeat_5 = make_repeater_off(5)
    print(repeat_5("Hola"))

    divide_by_5 = make_division_by(5)
    print(divide_by_5(10))

    divide_by_2 = make_division_by(2)
    print(divide_by_2(4))
    
    divide_by_0 = make_division_by(0)
    print(divide_by_0(1))


if __name__ == '__main__':
    run()
