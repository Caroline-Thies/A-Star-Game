class Token:
    canReach = {
        "left" : False,
        "right" : False,
        "up" : False,
        "down" : False
    }
    def __init__(self, canReach):
        self.canReach = canReach
