from enum import Enum
import regex, re

class Event(object):
    class EventType(Enum):
        NONE = 0
        TERMINATED = 1
        PHOTON_SCATTER = 10
        PHOTON_PHOTOELECTRIC = 11
        ELECTRON_ABSORB = 20

    class ParticleType(Enum):
        PHOTON = 0
        ELECTRON = -1

    def __init__(self, event_type, particle_type, initial_momentum, initial_position, final_position, children):
        self.event_type = self.EventType(event_type)
        self.particle_type = self.ParticleType(particle_type)
        self.initial_momentum = initial_momentum
        self.initial_position = initial_position
        self.final_position = final_position

        self.children = [Event(**child) for child in children]

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def draw_ax(self, ax):
        if self.particle_type == self.ParticleType.PHOTON:
            color = "green"
        else:
            color = "blue"

        ax.plot([self.initial_position[0], self.final_position[0]], [self.initial_position[1], self.final_position[1]], [self.initial_position[2], self.final_position[2]], color = color, linewidth=0.5)

        for child in self.children:
            child.draw_ax(ax)
