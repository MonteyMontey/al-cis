import pytest
import random
import numpy as np

from cis import cell
from cis import env
from cis import helper
import cis.config as conf
import tests.mocking as mck


class TestClass(object):

    # energy consumptions
    def test_move_cells(self):

        cells = mck.mock_cell_batch()
        test_position = [(cell.pos.x, cell.pos.y, cell.pos.z) for cell in cells]

        id_to_cell_dict = {}
        helper.map_cells_to_dict(cells, id_to_cell_dict)

        env.move_cells(cells, id_to_cell_dict)
        assert [(cell.pos.x, cell.pos.y, cell.pos.z) for cell in cells] != test_position

    def test_move_cell_and_connected_cells(self):

        cells = mck.mock_cell_batch()
        single_cell = cells[random.randint(0, len(cells))]
        test_position = (single_cell.pos.x, single_cell.pos.y, single_cell.pos.z)

        id_to_cell_dict = {}
        helper.map_cells_to_dict(cells, id_to_cell_dict)
        moved_dict = {}

        env.move_cell_and_connected_cells(single_cell, id_to_cell_dict, moved_dict)
        assert (single_cell.pos.x, single_cell.pos.y, single_cell.pos.z) != test_position

    def test_curl(self):

        pos = mck.Vector(10, 15, 20)

        curled = env.curl(pos)
        assert np.array_equal(curled, np.array([0, 3.92, -3.94]))

    # food
    def test_feed_cells(self):

        cells = mck.mock_cell_batch(500)
        test_energy = sum([cell.energy_level for cell in cells])

        for time_step in range(100):
            env.feed_cells(cells, time_step)
        energy = sum([cell.energy_level for cell in cells])

        assert energy > test_energy

    # def test_feed_cell(self):
    #     pass

    def test_food_function(self):

        pos = mck.Vector(10, 15, 20)

        food = env.food_function(pos, 100)
        assert food
        assert type(food) == np.float64

    def test_wave_function(self):

        # test pos
        for i in range(0, 2000, 100):
            rand_pos = random.randint(i, i+100)
            assert env.wave_function(rand_pos, 50)

        # test time
        for i in range(0, 2000, 100):
            rand_time = random.randint(i, i+100)
            assert env.wave_function(rand_time, 50)

    def test_noramlize_food_value(self):

        for _ in range(5):
            rand_num = random.randint(-3, 3)
            norm_num = env.normalize_food_value(rand_num, definition_area_size=6)

            assert norm_num >= 0 and norm_num <= 1
