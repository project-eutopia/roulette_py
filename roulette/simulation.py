import json
from roulette.event import Event
from roulette.voxel_grid import VoxelGrid

class Simulation(object):
    def __init__(self, events):
        self.events = [Event(**event_data) for event_data in events]
