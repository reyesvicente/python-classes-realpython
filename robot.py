class IndustrialRobot:
    def __init__(self, body, arm):
        self.body = body
        self.arm = arm

    def rotate_body_left(self, degrees=10):
        self.body.rotate_left(degrees)

    def rotate_body_right(self, degrees=10):
        self.body.rotate_right(degrees)

    def move_arm_up(self, distance=10):
        self.arm.move_up(distance)

    def move_arm_down(self, distance=10):
        self.arm.move_down(distance)

    def weld(self):
        self.arm.weld()


class Body:
    def __init__(self):
        self.rotation = 0

    def rotate_left(self, degrees=10):
        self.rotation -= degrees
        print(f"Rotating body {degrees} degrees to the left...")

    def rotate_right(self, degrees=10):
        self.rotation += degrees
        print(f'Rotating body {degrees} degrees to the right...')


class Arm:
    def __init__(self):
        self.position = 0

    def move_up(self, distance=10):
        self.position += 1
        print(f'Moving arm up {distance} cm up...')

    def move_down(self, distance=10):
        self.position -= 1
        print(f'Moving arm down {distance} cm down...')

    def weld(self):
        print('Welding arm...')