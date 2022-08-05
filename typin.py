from typing import Tuple, Dict, List

a: int = 5
print(a)
b: str = "Hello"
print(b)
c: bool = True
print(c)


def suma(a: int, b: int) -> int:
    return a + b


print(suma(1, 2))


positives: List[int] = [1, 2, 3, 4, 5]

users: Dict[str, int] = {
    'argentina': 1,
    'mexico': 34,
    'colombia': 45,
}

countries: List[Dict[str, str]] = [
    {
        'name': 'Argentina',
        'people': '450000',
    },
    {
        'name': 'México',
        'people': '9000000',
    },
    {
        'name': 'Colombia',
        'people': '9999999999999',
    }
]


numbers: Tuple[int, float, int] = (1, 0.5, 1)


CoordinatesType = List[Dict[str, Tuple[int, int]]]

coordinates: CoordinatesType = [
    {
        'coord1': (1, 2),
        'coord2': (3, 5)
    },
    {
        'coord1': (0, 1),
        'coord2': (2, 5)
    },
]
