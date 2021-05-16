from geometry.cylindricalGeometry import CylindricalGeometry

class PrismGeometry(CylindricalGeometry):

    def __init__(self, radius=1, height=1, sides=6, heightSegments=4):

        super().__init__(radius, radius, height,
                         sides, heightSegments)