import json
from roulette.simulation import Simulation
from roulette.voxel_grid import VoxelGrid

class SourceSimulation(object):
    def __init__(self, filename):
        self.filename = filename
        with open(filename) as f: self.data = json.load(f)

        self.voxel_grid = VoxelGrid(**self.data["voxel_grid"])
        self.simulation = Simulation(**self.data["simulation"])
