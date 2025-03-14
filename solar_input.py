# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet
import matplotlib.pyplot as plt

def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":  # FIXME: do the same for planet(+)
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            else:
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    star.type = line.split()[0].lower()
    star.R = float(line.split()[1])
    star.color = line.split()[2]
    star.m, star.x, star.y, star.Vx, star.Vy = list(map(float, line.split()[3:8]))
    # FIXME: not done yet(+)


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    planet.type = line.split()[0].lower()
    planet.R = float(line.split()[1])
    planet.color = line.split()[2]
    planet.m, planet.x, planet.y, planet.Vx, planet.Vy = list(map(float, line.split()[3:8]))
    # FIXME: not done yet...(+)


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            out_file.write(
                "{} {} {} {} {} {} {} {}".format(obj.type, obj.R, obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy))
            # FIXME: should store real values(+)


# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...
def statistics(space_objects, time):
    obj = space_objects[1]
    f = open('statistics.txt', 'a')
    v = (obj.Vx ** 2 + obj.Vy ** 2) ** 0.5
    f.writelines('{} {} \n'.format(v, time))


def graph(file_name):
    file = open(file_name, 'r')
    file_str = file.readlines()
    t_arr = []
    v_arr = []
    for s1 in file_str:
        t = list(map(float, s1.rstrip().split()))[1]
        t_arr.append(t)
        v = list(map(float, s1.rstrip().split()))[0]
        v_arr.append(v)

    plt.plot(t_arr, v_arr, color='Black')
    plt.xlabel('t')
    plt.ylabel('v')
    plt.ion()
    plt.show()

if __name__ == "__main__":
    print("This module is not for direct call!")
