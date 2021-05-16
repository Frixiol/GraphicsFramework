from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh

from geometry.planeGeometry import PlaneGeometry
from materials.surfaceBasicMaterial import SurfaceBasicMaterial

from extras.movementRig import MovementRig
from extras.axesHelper import AxesHelper
from extras.gridHelper import GridHelper

# render a scene

class Test(Base):

    def initialize(self):
        print("Initializing program...")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera()

        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.scene.add(self.rig)
        self.rig.setPosition(0, 0, 4)

        geometry = PlaneGeometry(width=100, height=100,widthResolution=100, heightResolution=100)
        material = SurfaceBasicMaterial({"useVertexColors":1})
        self.terrain = Mesh(geometry, material)
        self.terrain.rotateX(3.14/2)
        self.scene.add(self.terrain)





        self.scene.add(AxesHelper(axisLength=3))




    def update(self):

        self.rig.update(self.input, 1/60)
        self.renderer.render(self.scene, self.camera)


# instantiate and run class
Test().run()