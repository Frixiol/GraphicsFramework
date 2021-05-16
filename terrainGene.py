from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh

from geometry.gridDotGeometry import GridDotGeometry
from materials.pointBasicMaterial import PointBasicMaterial
from materials.lineBasicMaterial import LineBasicMaterial
from materials.surfaceBasicMaterial import SurfaceBasicMaterial
from geometry.geometry import Geometry
from materials.material import Material

from extras.axesHelper import AxesHelper
from extras.movementRig import MovementRig

# render a scene

class Test(Base):

    def initialize(self):
        print("Initializing program...")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera()
        self.rig = MovementRig(unitsPerSecond=25, degreesPerSecond=90)
        self.rig.add(self.camera)
        self.scene.add(self.rig)
        self.rig.setPosition(0, 0, 4)


        geometry = GridDotGeometry(width=1000, height=1000, heightResolution=300, widthResolution=300)
        material = SurfaceBasicMaterial({"useVertexColors":1})
        self.mesh = Mesh(geometry, material)

        self.scene.add(self.mesh)
        self.scene.add(AxesHelper(axisLength=3, lineWidth=2))



    def update(self):

        if self.input.isKeyDown("p"):
            self.mesh.material.settings["wireframe"] = not self.mesh.material.settings["wireframe"]
        self.rig.update(self.input, 1/60)
        self.renderer.render(self.scene, self.camera)


# instantiate and run class
Test().run()