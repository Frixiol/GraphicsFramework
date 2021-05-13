from OpenGL.GL import *

# static methods to load/compile OpenGL shaders
#   and link to create GPU programs

class OpenGLUtils(object):

    @staticmethod
    def initializeShader(shaderCode, shaderType):

        # specifiy OpenGL version and requirements
        shaderCode = "#version 330\n" + shaderCode

        # create empty shader object and return reference value
        shaderRef = glCreateShader(shaderType)
        # store source code in shader
        glShaderSource(shaderRef, shaderCode)
        # compile source code stored in shader
        glCompileShader(shaderRef)

        # query whether compilation was successful
        compileSuccess = glGetShaderiv(shaderRef,GL_COMPILE_STATUS)

        if not compileSuccess:
            # retrieve error message
            errorMessage = glGetShaderInfoLog(shaderRef)
            # free memory used to store shader program
            glDeleteShader(shaderRef)
            # convert byte string to character string
            errorMessage = "\n" + errorMessage.decode("utf-8")
            # raise exception, halt program, print error message
            raise Exception( errorMessage )

        # compilation was successful
        return shaderRef

    @staticmethod
    def initializeProgram(vertexShaderCode, fragmentShaderCode):

        # compile shaders and store references
        vertexShaderRef = OpenGLUtils.initializeShader(vertexShaderCode, GL_VERTEX_SHADER)
        fragmentShaderRef = OpenGLUtils.initializeShader(fragmentShaderCode, GL_FRAGMENT_SHADER)

        # create program object
        programRef = glCreateProgram()

        # attach previously compiled shaders
        glAttachShader(programRef, vertexShaderRef)
        glAttachShader(programRef, fragmentShaderRef)

        # link vertex shader to fragment shader
        glLinkProgram(programRef)

        # quiery if linking was sucessful
        linkSucces = glGetProgramiv(programRef, GL_LINK_STATUS)

        if not linkSucces:
            # retrieve error message
            errorMessage = glGetProgramInfoLog(programRef)
            # free memory used to store program
            glDeleteProgram(programRef)
            # convert byte string to character string
            errorMessage = "\n" + errorMessage.decode("utf-8")
            # raise exception, halt program, print error message
            raise Exception( errorMessage )

        # linking was successful, return program reference
        return programRef

    @staticmethod
    def printSystemInfo():
        print("=========================================================")
        print(" Vendor:  " + glGetString(GL_VENDOR).decode('utf-8'))
        print("Renderer: " + glGetString(GL_RENDERER).decode('utf-8'))
        print("OpenGL version supported: " + glGetString(GL_VERSION).decode('utf-8'))
        print("  GLSL version supported: " + glGetString(GL_SHADING_LANGUAGE_VERSION).decode('utf-8'))
        print("=========================================================")