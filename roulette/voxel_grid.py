from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class VoxelGrid(object):
    def __init__(self, nx, ny, nz, v0, vn):
        self.nx = nx
        self.ny = ny
        self.nz = nz
        self.v0 = v0
        self.vn = vn

        self.deltax = self.vn[0] - self.v0[0]
        self.deltay = self.vn[1] - self.v0[1]
        self.deltaz = self.vn[2] - self.v0[2]

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def draw_ax(self, ax):
        faces = []

        # Front
        faces.append([
            [self.v0[0], self.v0[1], self.v0[2]],
            [self.vn[0], self.v0[1], self.v0[2]],
            [self.vn[0], self.vn[1], self.v0[2]],
            [self.v0[0], self.vn[1], self.v0[2]]
        ])
        # Back
        faces.append([
            [self.vn[0], self.vn[1], self.vn[2]],
            [self.v0[0], self.vn[1], self.vn[2]],
            [self.v0[0], self.v0[1], self.vn[2]],
            [self.vn[0], self.v0[1], self.vn[2]]
        ])

        # Left
        faces.append([
            [self.v0[0], self.v0[1], self.v0[2]],
            [self.v0[0], self.v0[1], self.vn[2]],
            [self.v0[0], self.vn[1], self.vn[2]],
            [self.v0[0], self.vn[1], self.v0[2]]
        ])
        # Right
        faces.append([
            [self.vn[0], self.vn[1], self.vn[2]],
            [self.vn[0], self.vn[1], self.v0[2]],
            [self.vn[0], self.v0[1], self.v0[2]],
            [self.vn[0], self.v0[1], self.vn[2]]
        ])

        # Top
        faces.append([
            [self.v0[0], self.v0[1], self.v0[2]],
            [self.vn[0], self.v0[1], self.v0[2]],
            [self.vn[0], self.v0[1], self.vn[2]],
            [self.v0[0], self.v0[1], self.vn[2]]
        ])
        # Bottom
        faces.append([
            [self.vn[0], self.vn[1], self.v0[2]],
            [self.v0[0], self.vn[1], self.v0[2]],
            [self.v0[0], self.vn[1], self.vn[2]],
            [self.vn[0], self.vn[1], self.vn[2]]
        ])

        for face in faces:
            poly3d = Poly3DCollection([face], alpha=0.5, linewidths=2, edgecolors="black", facecolors=(0, 0.5, 1, 0.15))
            ax.add_collection3d(poly3d)

        ax.set_xlim(self.v0[0] - 0.05*self.deltax, self.vn[0] + 0.05*self.deltax)
        ax.set_ylim(self.v0[1] - 0.05*self.deltay, self.vn[1] + 0.05*self.deltay)
        ax.set_zlim(self.v0[2] - 0.05*self.deltaz, self.vn[2] + 0.05*self.deltaz)
