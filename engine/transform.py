
class Transform():

    # TODO struct?
    # TODO: make magnitude a derived field
    # and aso get base direction vector. this will allow move to increment through it to solve is_valid?()

    def __init__(self, x, y, magnitude):
        self.x = x
        self.y = y
        self.magnitude = magnitude

