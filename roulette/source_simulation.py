from matplotlib import pyplot as plt
import json

from roulette.simulation import Simulation
from roulette.voxel_grid import VoxelGrid

class SourceSimulation(object):
    def __init__(self, filename):
        self.filename = filename
        with open(filename) as f: self.data = json.load(f)

        self.voxel_grid = VoxelGrid(**self.data["voxel_grid"])
        self.simulation = Simulation(**self.data["simulation"])

    def draw(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        self.voxel_grid.draw_ax(ax)
        self.simulation.draw_ax(ax)

        plt.show()
