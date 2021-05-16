from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh

from geometry.boxGeometry import BoxGeometry
from materials.pointBasicMaterial import PointBasicMaterial
from materials.lineBasicMaterial import LineBasicMaterial
from materials.surfaceBasicMaterial import SurfaceBasicMaterial
from geometry.geometry import Geometry
from materials.material import Material

from math import sin, cos

# render a scene

class Test(Base):

    def initialize(self):
        print("Initializing program...")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera()
        # pull camera towards viewer
        self.camera.setPosition(0, 0, 7)

        geometry = Geometry()
        posData = []
        for x in range(-32, 32, 3):
            posData.append([x/10, sin(x/10), 0])
        geometry.addAttribute("vec3", "vertexPosition", posData)
        geometry.countVertices()

        pointMaterial = PointBasicMaterial({"baseColor": [1,1,0]})
        self.pointMesh = Mesh(geometry, pointMaterial)

        lineMaterial = LineBasicMaterial({"baseColor": [1,0,1]})
        self.lineMesh = Mesh(geometry,lineMaterial)

        self.scene.add(self.pointMesh)
        self.scene.add(self.lineMesh)

    def update(self):

        self.renderer.render(self.scene, self.camera)


# instantiate and run class
Test().run()