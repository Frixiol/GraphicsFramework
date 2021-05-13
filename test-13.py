from core.base import Base


# test input functions
class Test(Base):

    def initialize(self):
        print("Initializing program...")

    def update(self):

        # debug printing
        #if len(self.input.keyDownList) > 0:
        #    print("Keys Down:", self.input.keyDownList)

        #if len(self.input.keyPressedList) > 0:
        #    print("Keys Pressed:", self.input.keyPressedList)

        #if len(self.input.keyUpList) > 0:
        #    print("Keys Up:", self.input.keyUpList)

        # typical usage
        if self.input.isKeyDown("space"):
            print("hello")

        if self.input.isKeyPressed("right"):
            print("moving right")

# instantiate and run
Test().run()

