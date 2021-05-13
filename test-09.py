from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from OpenGL.GL import *

# render six points in a hexagon arrangement
class Test(Base):

    def initialize(self):
        print("Initializing program...")

        vsCode = """
        in vec3 position;
        void main()
        {
            gl_Position = vec4(position.x, position.y, position.z, 1.0);
        }
        """

        fsCode = """
        void main()
        {
            gl_FragColor = vec4(0.0, 1.0, 1.0, 1.0);
        }
        """

        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        # render settings
        glPointSize( 16 )
        glLineWidth( 8 )

        # set up VAOs (vertex array objects)
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        # set up vertex attribute
        positionData = [[ 0.8, 0.0, 0.0],
                        [ 0.4, 0.6, 0.0],
                        [-0.4, 0.6, 0.0],
                        [-0.8, 0.0, 0.0],
                        [-0.4,-0.6, 0.0],
                        [ 0.4,-0.6, 0.0]]
        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")

        self.vertexCount = len(positionData)

    def update(self):

        glUseProgram(self.programRef)
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertexCount)

# create instance and run
Test().run()