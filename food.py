import cis_config as conf
import numpy as np
import random


def feed_all_cells(cells, time):
    """
        Calc the amount of food a cell gets and add it to cell,
        given the position of the cell and the time.
    """
    new_cells = []

    for cell in cells:
        cell = feed(cell, time)
        cell = consume_energy(cell)
        if alive(cell):
            new_cells.append(cell)

    return new_cells


def feed(cell, time):
    """
        Give the cell food,
        depending on position and time.
    """
    def f1(x): return np.sin(x)

    def f2(y): return np.sin(y)

    def f3(z): return np.sin(z)

    def f(x, y, z): return f1(x) + f2(y) + f3(z)

    food_value = f(cell.pos.x, cell.pos.y, cell.pos.z)  # {-3, 3}

    # normalize food_value to {0, 1}
    food_value = normalize(food_value)

    # probability that cell get food
    if food_value < conf.FOOD_THRESHOLD:
        cell.energy_level += conf.FOOD_ENERGY

    return cell


def consume_energy(cell):
    """
       Calc if cell still lives after energy consumption.
    """
    # general energy consumption
    cell.energy_level -= conf.GENERAL_ENERGY_CONSUMPTION

    # other energ consumption (in future)
    cell.energy_level -= 0

    return cell


def alive(cell):
    """
        Checks if cell is still living,
        depending on energy level.
    """
    if cell.energy_level > conf.ENERGY_THRESHOLD:
        return True

    return False


def normalize(num, definition_area_size=6):
    ret = round(num) / definition_area_size + 0.5
    return ret
