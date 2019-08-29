import pytest
import random
import numpy as np

from cis import helper
import tests.mocking as mck


class TestClass(object):

    def test_map_cells_to_dict(self):

        cells = mck.mock_cell_batch()

        cell_dict = {}
        helper.map_cells_to_dict(cells, cell_dict)

        assert cell_dict, "ReturnError"
        assert len(cell_dict) == len(cells), "RangeError"
        for cell in cells:
            assert cell_dict[cell.id] == cell, "KeyError"

    def test_get_value(self):
        cells = mck.mock_cell_batch()

        cell_dict = {}
        helper.map_cells_to_dict(cells, cell_dict)

        for cell in cells:
            val, _ = helper.get_value(cell_dict, cell.id)
            assert val == cell, "KeyError"

    def test_random_vector_of_length(self):

        for _ in range(5):
            rand_length = random.randint(0, 100)
            vec = helper.random_vector_of_length(rand_length)

            length = sum(vec**2)**0.5
            assert abs(length - rand_length) < 1

    # def test_group_connected_cells(self):
    #     pass
