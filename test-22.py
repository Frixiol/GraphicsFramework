from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from core.uniform import Uniform
from core.matrix import Matrix
from OpenGL.GL import *
from math import pi

# move triangle around the screen
class Test(Base):

    def initialize(self):
        print("Initializing...")

        # shaders
        vsCode = """
        in vec3 position;
        uniform mat4 projectionMatrix;
        uniform mat4 modelMatrix;
        void main()
        {
            gl_Position = projectionMatrix * modelMatrix * vec4(position, 1.0);
        }
        """

        fsCode = """
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }
        """

        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        # render settings
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)

        # vao
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        # vertex attribute
        positionData = [[ 0.0,  0.2, 0.0],
                        [ 0.1, -0.2, 0.0],
                        [-0.1, -0.2, 0.0]]

        self.vertexCount = len(positionData)
        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")

        # uniforms
        mMatrix = Matrix.makeTranslation(0, 0, -1)
        self.modelMatrix = Uniform("mat4", mMatrix)
        self.modelMatrix.locateVariable(self.programRef, "modelMatrix")

        pMatrix = Matrix.makePersepctive()
        self.projectionMatrix = Uniform("mat4", pMatrix)
        self.projectionMatrix.locateVariable(self.programRef, "projectionMatrix")

    def update(self):

        moveAmount = 0.005
        turnAmount = 0.01

        # global translations
        if self.input.isKeyPressed("z"):
            m = Matrix.makeTranslation(0, moveAmount, 0)
            self.modelMatrix.data = m @ self.modelMatrix.data
        if self.input.isKeyPressed("s"):
            m = Matrix.makeTranslation(0, -moveAmount, 0)
            self.modelMatrix.data = m @ self.modelMatrix.data
        if self.input.isKeyPressed("q"):
            m = Matrix.makeTranslation(-moveAmount, 0, 0)
            self.modelMatrix.data = m @ self.modelMatrix.data
        if self.input.isKeyPressed("d"):
            m = Matrix.makeTranslation(moveAmount, 0, 0)
            self.modelMatrix.data = m @ self.modelMatrix.data

        if self.input.isKeyPressed("w"):
            m = Matrix.makeTranslation(0, 0, moveAmount)
            self.modelMatrix.data = m @ self.modelMatrix.data
        if self.input.isKeyPressed("x"):
            m = Matrix.makeTranslation(0, 0, -moveAmount)
            self.modelMatrix.data = m @ self.modelMatrix.data

        # global rotations
        if self.input.isKeyPressed("a"):
            m = Matrix.makeRotationZ(turnAmount)
            self.modelMatrix.data = m @ self.modelMatrix.data
        if self.input.isKeyPressed("e"):
            m = Matrix.makeRotationZ(-turnAmount)
            self.modelMatrix.data = m @ self.modelMatrix.data

        # local translations
        if self.input.isKeyPressed("i"):
            m = Matrix.makeTranslation(0, moveAmount, 0)
            self.modelMatrix.data = self.modelMatrix.data @ m
        if self.input.isKeyPressed("k"):
            m = Matrix.makeTranslation(0, -moveAmount, 0)
            self.modelMatrix.data = self.modelMatrix.data @ m
        if self.input.isKeyPressed("j"):
            m = Matrix.makeTranslation(-moveAmount, 0, 0)
            self.modelMatrix.data = self.modelMatrix.data @ m
        if self.input.isKeyPressed("l"):
            m = Matrix.makeTranslation(moveAmount, 0, 0)
            self.modelMatrix.data = self.modelMatrix.data @ m

        # local rotations
        if self.input.isKeyPressed("u"):
            m = Matrix.makeRotationZ(turnAmount)
            self.modelMatrix.data = self.modelMatrix.data @ m
        if self.input.isKeyPressed("o"):
            m = Matrix.makeRotationZ(-turnAmount)
            self.modelMatrix.data = self.modelMatrix.data @ m

        # render
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.programRef)
        self.projectionMatrix.uploadData()
        self.modelMatrix.uploadData()
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)
        print(self.modelMatrix.data)

# instantiate and run
Test().run()