import uuid
import random

from cis import cell


def mock_cell_batch(init_amount=2000):

    return [mock_cell() for _ in range(init_amount)]


class mock_cell():

    _init_energy_level = 20
    _dna_length = (3, 6)
    _dim = ((0, 2000), (0, 2000), (0, 2000))

    def __init__(self):

        self.id = str(uuid.uuid1())
        self.energy_level = self._init_energy_level
        self.pos = self.init_pos()
        self.vel = Vector(
            x=0,
            y=0,
            z=0
        )
        self.dna = cell.random_dna(
            min_length=self._dna_length[0],
            max_length=self._dna_length[1]
        )
        self.connections = []

    def init_pos(self):

        dim = self._dim

        initial_position = Vector(
            x=random.uniform(dim[0][0], dim[0][1]),
            y=random.uniform(dim[1][0], dim[1][1]),
            z=random.uniform(dim[2][0], dim[2][1])
        )

        return initial_position


class Vector():

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
