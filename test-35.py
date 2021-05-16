from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh

from geometry.boxGeometry import BoxGeometry
from geometry.polygonGeometry import PolygonGeometry
from materials.surfaceBasicMaterial import SurfaceBasicMaterial

from extras.movementRig import MovementRig

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


        geometry = BoxGeometry()
        material = SurfaceBasicMaterial({"useVertexColors": 1})
        self.mesh = Mesh(geometry, material)
        self.mesh.rotateX(0.6)
        self.mesh.rotateY(-0.6)
        self.mesh.rotateZ(-0.4)

        self.scene.add(self.mesh)

        # add a backdrop
        backGeometry = PolygonGeometry(sides=64, radius=2)
        backMaterial = SurfaceBasicMaterial({"baseColor":[1,1,0]})
        self.backdrop = Mesh(backGeometry, backMaterial)
        self.backdrop.rotateX(1.57)
        self.backdrop.setPosition(0,-1,0)
        self.scene.add(self.backdrop)


    def update(self):

        self.mesh.rotateX(-0.03)
        self.mesh.rotateY(0.03)
        self.mesh.rotateZ(-0.03)

        self.rig.update(self.input, 1/60)

        self.backdrop.rotateZ(0.03)
        self.renderer.render(self.scene, self.camera)


# instantiate and run class
Test().run()