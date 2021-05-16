from core.mesh import Mesh
from geometry.geometry import Geometry
from materials.lineBasicMaterial import LineBasicMaterial

class AxesHelper(Mesh):

    def __init__(self, axisLength=1, lineWidth=4):

        geo = Geometry()

        posData = [[0,0,0], [axisLength,0,0],
                   [0,0,0], [0,axisLength,0],
                   [0,0,0], [0,0,axisLength]]

        R = [1,0,0]
        G = [0,1,0]
        B = [0,0,1]
        colorData = [R,R, G,G, B,B]

        geo.addAttribute("vec3", "vertexPosition", posData)
        geo.addAttribute("vec3", "vertexColor", colorData)
        geo.countVertices()

        mat = LineBasicMaterial({
            "useVertexColors":1,
            "lineWidth": lineWidth,
            "lineType": "segments"
        })

        super().__init__(geo, mat)