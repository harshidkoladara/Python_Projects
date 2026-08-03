# Container Class
class Container():

    def __init__(self):
        self.name = None
        self.price = None

# Paper class which inherits Container class
class Paper(Container):

    def __init__(self):
        self.name = "paper"
        self.price = 0.1


# Bottle class which inherits Container class
class Bottle(Container):

    def __init__(self):
        self.name = "bottle"
        self.price = 0.3


# Can class which inherits Container class
class Can(Container):

    def __init__(self):
        self.name = "can"
        self.price = 0.5

# Box  which inherits Container class
class Box(Container):

    def __init__(self):
        self.name = "box"
        self.price = 0.7
