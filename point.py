from dataclasses import dataclass

@dataclass
class ThreeDPoint:
    x: int | float
    y: int | float
    z: int | float

    """def __iter__(self):
        yield from (self.x, self.y, self.z)"""

    @classmethod
    def from_sequence(cls, sequence):
        return cls(*sequence)

    @staticmethod
    def show_intro_message(name):
        print(f"Hey {name}! This is your 3D Point!")
    
    """def __repr__(self):
        return f"{type(self).__name__}({self.x}, {self.y}, {self.z})"""
    