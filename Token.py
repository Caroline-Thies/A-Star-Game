class Token:
    def __init__(self, left: bool, right: bool, up: bool, down: bool):
        self.canReach = {"left": left, "right": right, "up": up, "down": down}
