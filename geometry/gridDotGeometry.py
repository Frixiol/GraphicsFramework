from geometry.geometry import Geometry
from perlin_noise import PerlinNoise
import glm

class GridDotGeometry(Geometry):

    def __init__(self, width=10, height=10, widthResolution=8, heightResolution=8):

        super().__init__()


        self.uStart, self.uEnd, self.uResolution = -width/2, width/2, widthResolution
        self.vStart, self.vEnd, self.vResolution = -height / 2, height / 2, heightResolution

        # generate a set of points on the function
        self.deltaU = (self.uEnd - self.uStart) / self.uResolution
        self.deltaV = (self.vEnd - self.vStart) / self.vResolution

        self.update()

    def update(self):

        positions = []
        colorData = []
        nb = 0
        for uIndex in range(self.uResolution + 1):
            vArray = []
            for vIndex in range(self.vResolution + 1):
                u = self.uStart + uIndex * self.deltaU
                v = self.vStart + vIndex * self.deltaV
                y = glm.perlin(glm.vec2(u*0.01, v*0.01)) * 50

                nb += 1
                vArray.append([v,y,u])

            positions.append(vArray)

        # store vertex data
        positionData = []
        colorData = []

        # deafault vertex colors
        C1, C2, C3 = [0.5, 0.5, 0.5], [0.6, 0.6, 0.6], [0.4, 0.4, 0.4]

        # group vertex data into triangles
        for xIndex in range(self.uResolution):
            for yIndex in range(self.vResolution):
                # position data
                pA = positions[xIndex + 0][yIndex + 0]
                pB = positions[xIndex + 1][yIndex + 0]
                pC = positions[xIndex + 1][yIndex + 1]
                pD = positions[xIndex + 0][yIndex + 1]

                positionData += [pA, pB, pC, pA, pC, pD]
                colorData += [C1, C2, C3, C1, C3, C2]

        self.addAttribute("vec3", "vertexPosition", positionData)
        self.addAttribute("vec3", "vertexColor", colorData)
        self.countVertices()
