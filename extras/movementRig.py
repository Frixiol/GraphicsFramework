from core.object3D import Object3D

class MovementRig(Object3D):

    def __init__(self, unitsPerSecond=1, degreesPerSecond=60):

        super().__init__()

        # initialize attached object3D
        self.lookAttachment = Object3D()
        self.children = [self.lookAttachment]
        self.lookAttachment.parent = self

        self.unitsPerSecond = unitsPerSecond
        self.degreesPerSecond = degreesPerSecond

        # customizable key mappings
        self.KEY_MOVE_FORWADS   = "z"
        self.KEY_MOVE_BACKWARDS = "s"
        self.KEY_MOVE_LEFT      = "q"
        self.KEY_MOVE_RIGHT     = "d"

        self.KEY_TURN_LEFT = "left"
        self.KEY_TURN_RIGHT = "right"

        self.KEY_MOVE_UP = "space"
        self.KEY_MOVE_DOWN = "left shift"

        self.KEY_LOOK_UP = "up"
        self.KEY_LOOK_DOWN= "down"

    def add(self, child):
        self.lookAttachment.add(child)

    def update(self, inputObject, deltaTime):

        moveAmount = self.unitsPerSecond * deltaTime
        rotateAmount = self.degreesPerSecond * 3.14/180 * deltaTime

        if inputObject.isKeyPressed(self.KEY_MOVE_FORWADS):
            self.translate(0,0,-moveAmount)
        if inputObject.isKeyPressed(self.KEY_MOVE_BACKWARDS):
            self.translate(0,0, moveAmount)
        if inputObject.isKeyPressed(self.KEY_MOVE_LEFT):
            self.translate(-moveAmount,0,0)
        if inputObject.isKeyPressed(self.KEY_MOVE_RIGHT):
            self.translate( moveAmount,0,0)
        if inputObject.isKeyPressed(self.KEY_MOVE_UP):
            self.translate(0, moveAmount,0)
        if inputObject.isKeyPressed(self.KEY_MOVE_DOWN):
            self.translate(0,-moveAmount,0)

        if inputObject.isKeyPressed(self.KEY_TURN_LEFT):
            self.rotateY(rotateAmount)
        if inputObject.isKeyPressed(self.KEY_TURN_RIGHT):
            self.rotateY(-rotateAmount)
        if inputObject.isKeyPressed(self.KEY_LOOK_UP):
            self.lookAttachment.rotateX(rotateAmount)
        if inputObject.isKeyPressed(self.KEY_LOOK_DOWN):
            self.lookAttachment.rotateX(-rotateAmount)

