from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh

from geometry.boxGeometry import BoxGeometry
from materials.surfaceBasicMaterial import SurfaceBasicMaterial

# render a scene

class Test(Base):

    def initialize(self):
        print("Initializing program...")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera()

        geometry = BoxGeometry()
        material = SurfaceBasicMaterial({"useVertexColors": 1})
        self.mesh = Mesh(geometry, material)
        self.mesh.rotateX(0.6)
        self.mesh.rotateY(-0.6)
        self.mesh.rotateZ(-0.4)

        self.scene.add(self.mesh)

        # pull camera towards viewer
        self.camera.setPosition(0, 0, 4)

        # add a backdrop
        backGeometry = BoxGeometry(width=2, height=2, depth=0.01)
        backMaterial = SurfaceBasicMaterial({"baseColor":[1,1,0]})
        self.backdrop = Mesh(backGeometry, backMaterial)
        self.backdrop.rotateX(1.57)
        self.backdrop.setPosition(0,-1,0)
        self.scene.add(self.backdrop)


    def update(self):

        self.mesh.rotateX(-0.03)
        self.mesh.rotateY(0.03)
        self.mesh.rotateZ(-0.03)


        self.backdrop.rotateZ(0.03)
        self.renderer.render(self.scene, self.camera)


# instantiate and run class
Test().run()