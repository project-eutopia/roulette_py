class VoxelGrid(object):
    def __init__(self, nx, ny, nz, v0, vn):
        self.nx = nx
        self.ny = ny
        self.nz = nz
        self.v0 = v0
        self.vn = vn

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
