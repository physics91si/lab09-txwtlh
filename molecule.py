import particle
import numpy as np

class Molecule:

    def __init__(self, pos1, pos2, m1, m2, k, L0):
        self.p1 = particle.Particle(pos1, m1)
        self.p2 = particle.Particle(pos2, m2)
        self.k = k
        self.L0 = L0

    def get_displ(self):
        return self.p1.pos - self.p2.pos

    def get_force(self):
        return self.k * self.get_displ()
