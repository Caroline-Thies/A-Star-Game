class Token:
    canReach : dict = {
        "left" : False,
        "right" : False,
        "up" : False,
        "down" : False
    }
    def __init__(self, canReach : dict):
        self.canReach = canReach
