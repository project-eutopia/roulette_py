from roulette.event import Event

class Simulation(object):
    def __init__(self, filename):
        self.filename = filename
        self.events = []

        with open(self.filename, "r") as f:
            line = f.readline().strip()
            assert(line == "Simulation[")

            for line in f.readlines():
                line = line.strip()
                if line == "]": break
                self.events.append(Event(line))
