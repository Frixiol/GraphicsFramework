from core.mesh import Mesh
from geometry.geometry import Geometry
from materials.lineBasicMaterial import LineBasicMaterial
from random import randint

class GridHelper(Mesh):

    def __init__(self, size=10, divisions=10, lineWidth=1,
                 gridColor=[1,1,1], centerColor=[1,1,0]):

        geo = Geometry()

        posData = []
        colorData = []

        # create range of values
        values = []
        deltaSize = size/divisions
        for n in range(divisions+1):
            values.append(-size/2 + n * deltaSize)

        # add vertical lines
        for x in values:
            posData.append([x, -size/2, 0])
            posData.append([x,  size/2, 0])
            if x == 0:
                colorData.append(centerColor)
                colorData.append(centerColor)
            else:
                colorData.append(gridColor)
                colorData.append(gridColor)

        # add horizontal lines
        for y in values:
            posData.append([-size/2, y, 0])
            posData.append([ size/2, y, 0])
            if y == 0:
                colorData.append(centerColor)
                colorData.append(centerColor)
            else:
                colorData.append(gridColor)
                colorData.append(gridColor)

        geo.addAttribute("vec3", "vertexPosition", posData)
        geo.addAttribute("vec3", "vertexColor", colorData)
        geo.countVertices()

        mat = LineBasicMaterial({
            "useVertexColors":1,
            "lineWidth": lineWidth,
            "lineType": "segments"
        })

        super().__init__(geo, mat)