"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    """"""

    """Initiate starting point for counter & start value to reset back to"""
    def __init__(self, start):
        self.start = start
        self.counter = start
    
    """Initialize specified starting point with increment on each call"""
    def generate(self):
        self.counter += 1     
        return self.counter - 1

    """Display Serial Details"""
    def __repr__(self):
        return f'<Serial_Generator: start:{self.start},next:{self.counter + 1}>'
    
    """Reset start back to initial value"""
    def reset(self):
        self.counter = self.start

# {self.start}, 
serial = SerialGenerator(200)

