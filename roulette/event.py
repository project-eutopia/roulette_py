from enum import Enum
import regex, re

class Event(object):
    EVENT_REGEX = "Event\((-?\d+?),\s*(-?\d+?),\s*FourMomentum\(([^\(\)]+?)\),\s*ThreeVector\(([^\(\)]+?)\),\s*ThreeVector\(([^\(\)]+?)\)\s*,\s*children\s*=\s*\[((?:.+|(?R))*)\]\)"
    CHILDREN_REGEX = "^Event(\(((?:[^\(\)]+|(?1))*)\)),"

    class EventType(Enum):
        NONE = 0
        TERMINATED = 1
        PHOTON_SCATTER = 10
        PHOTON_PHOTOELECTRIC = 11
        ELECTRON_ABSORB = 20

    class ParticleType(Enum):
        PHOTON = 0
        ELECTRON = -1

    def __init__(self, event_string):
        insides = regex.findall(self.EVENT_REGEX, event_string)[0]

        self.event_type = self.EventType(int(insides[0]))
        self.particle_type = self.ParticleType(int(insides[1]))

        m = re.search("([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)", insides[2])
        self.initial_momentum = [m.group(1), m.group(2), m.group(3), m.group(4)]
        self.initial_momentum = [float(x) for x in self.initial_momentum]

        m = re.search("([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)", insides[3])
        self.initial_position = [m.group(1), m.group(2), m.group(3)]
        self.initial_position = [float(x) for x in self.initial_position]

        m = re.search("([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)", insides[4])
        self.final_position = [m.group(1), m.group(2), m.group(3)]
        self.final_position = [float(x) for x in self.final_position]

        self.children = []
        children_string = insides[5]
        while children_string:
            m = regex.match(self.CHILDREN_REGEX, children_string)
            if not m: break

            span = m.span()
            child_string = "Event{}".format(m.group(1))
            self.children.append(Event(child_string))

            children_string = children_string[span[1]:].strip()

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
