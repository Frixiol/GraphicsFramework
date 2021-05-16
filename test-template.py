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

# render a scene

class Test(Base):

    def initialize(self):
        print("Initializing program...")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera()
        # pull camera towards viewer
        self.camera.setPosition(0, 0, 4)

        geometry = BoxGeometry()
        material = SurfaceBasicMaterial({"useVertexColors": 1})
        self.mesh = Mesh(geometry, material)

        self.scene.add(self.mesh)

    def update(self):

        self.renderer.render(self.scene, self.camera)


# instantiate and run class
Test().run()