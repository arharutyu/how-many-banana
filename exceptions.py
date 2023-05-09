class InputNotNumber(Exception):
    pass

class LengthCantBeZero(Exception):
    def __init__(self, length, message='Length must be a number greater than 0'):
        self.length = length
        self.message = message
        
        