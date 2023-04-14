import random


def rota(rooms: list) -> list:
    return random.choices(rooms, k=7) if len(rooms) < 7 else random.sample(rooms, 7)


if __name__ == '__main__':
    occupied_rooms = ["One", "Two", "Three", "Four", "Five", "Six", "Seven","Eight"]
    print(rota(occupied_rooms))
