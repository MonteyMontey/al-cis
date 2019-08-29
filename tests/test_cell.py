import pytest
import random

from cis import cell
from cis import env
import tests.mocking as mck


class TestClass(object):

    # energy consumptions
    def test_cells_consume_energy(self):

        cells = mck.mock_cell_batch(2000)
        test_energy = [cells[i].energy_level for i in range(len(cells))]

        cell.cells_consume_energy(cells)
        energy = [cells[i].energy_level for i in range(len(cells))]

        assert energy != test_energy

    def test_consume_energy(self):

        single_cell = mck.mock_cell()

        cell.consume_energy(single_cell)
        assert single_cell.energy_level == 18

    # survival
    def test_cells_survive(self):

        cells = mck.mock_cell_batch(2000)
        test_len = len(cells)

        cell.cells_survive(cells)
        assert len(cells) == test_len

    def test_is_alive(self):

        single_cell = mck.mock_cell()

        assert cell.is_alive(single_cell) == True

    # average energy
    # def test_average_out_cell_energy(self):
    #     pass

    # def test_average_out_energy_in_connected_cells(self):
    #     pass

    # division
    def test_cells_divide(self):

        num = 0

        for _ in range(10):
            cells = mck.mock_cell_batch(2000)
            test_len = len(cells)

            for single_cell in cells:
                single_cell.energy_level += random.randint(100, 500)

            with pytest.raises(AttributeError):
                cell.cells_divide(cells)

            if len(cells) != test_len:
                num += 1

        assert num != 0

    def test_divide(self):

        num = 0

        for _ in range(20):

            single_cell = mck.mock_cell()
            single_cell.energy_level = 1000
            ret = None

            try:
                with pytest.raises(AttributeError):
                    ret = cell.divide(single_cell)
            except:
                pass

            if ret != None:
                num += 1

        assert num != 0

    # def test_builds_connection_after_division(self):
    #     pass

    # def test_dna_copy_or_sub_slice(self):
    #     pass

    # def test_randomly_shifted_pos(self):
    #     pass

    # def test_random_dna(self):
    #     pass
