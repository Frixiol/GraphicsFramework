

class Geometry(object):

    def __init__(self):

        # dictionary to store attribute objects
        self.attributes = {}

        # number of vertices
        self.vertexCount = None

    def countVertices(self):
        # the number of vertices is the lenght of any
        # Attribute object's array of data
        attrib = list(self.attributes.values())[0]
        self.vertexCount = len(attrib.data)
