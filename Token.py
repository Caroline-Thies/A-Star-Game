class Token:
    canReach: dict = {
        "left": False,
        "right": False,
        "up": False,
        "down": False
    }

    def __init__(self, can_reach: dict):
        self.canReach = can_reach
