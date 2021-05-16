from core.attribute import Attribute

class Geometry(object):

    def __init__(self):

        # dictionary to store attribute objects
        self.attributes = {}

        # number of vertices
        self.vertexCount = None

    def addAttribute(self, dataType, variableName, data):
        self.attributes[variableName] = Attribute(dataType, data)

    def countVertices(self):
        # the number of vertices is the lenght of any
        # Attribute object's array of data
        attrib = list(self.attributes.values())[0]
        print(len(attrib.data))
        self.vertexCount = len(attrib.data)
