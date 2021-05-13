from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from core.uniform import Uniform
from OpenGL.GL import *

from math import sin


# render multiple triangles
class Test(Base):

    def initialize(self):
        print("initializing program...")

        vsCode = """
        in vec3 position;
        uniform vec3 translation;
        void main()
        {
            vec3 pos = position + translation;
            gl_Position = vec4(pos.x, pos.y, pos.z, 1.0);
        }
        """

        fsCode = """
        uniform vec3 baseColor;
        void main()
        {
            gl_FragColor = vec4(baseColor.r, baseColor.g, baseColor.b, 1.0);
        }
        """

        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        # render settings
        glClearColor(0.6, 0.6, 0.8, 1.0)

        # vertex array object
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        # set up attribute
        positionData = [[ 0.0,  0.2, 0.0],
                        [ 0.2, -0.2, 0.0],
                        [-0.2, -0.2, 0.0]]
        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")
        self.vertexCount = len(positionData)

        # set up uniforms
        self.translation1 = Uniform("vec3", [-0.5, 0.0, 0.0])
        self.translation1.locateVariable(self.programRef, "translation")

        self.translation2 = Uniform("vec3", [ 0.5, 0.0, 0.0])
        self.translation2.locateVariable(self.programRef, "translation")

        self.baseColor1 = Uniform("vec3", [1.0, 0.0, 0.0])
        self.baseColor1.locateVariable(self.programRef, "baseColor")

        self.baseColor2 = Uniform("vec3", [0.0, 0.0, 1.0])
        self.baseColor2.locateVariable(self.programRef, "baseColor")

        self.time = 0

    def update(self):

        glUseProgram(self.programRef)

        # clear the screen
        glClear(GL_COLOR_BUFFER_BIT)
        self.time += 1/60

        # draw first triangle
        self.translation1.data[1] += 0.01
        self.translation1.uploadData()
        self.baseColor1.uploadData()
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)

        # draw second triangle
        self.baseColor2.data[2] = (sin(self.time) + 1) / 2
        self.translation2.uploadData()
        self.baseColor2.uploadData()
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)

# create instance of class and run
Test().run()