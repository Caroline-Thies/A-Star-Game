class Token:
    def __init__(self, left: bool, right: bool, up: bool, down: bool):
        self.canReach = {"left": left, "right": right, "up": up, "down": down}

    def __str__(self):
        row1 = ""
        if self.canReach.up:
            row1 = "  |  "
        row2 = ""
        if self.canReach.left:
            row2 += "--"
        else:
            row2 += "  "
        row2 += "*"
        row3 = ""
        if self.canReach.down:
            row3 = "  |  "
        return row1 + "\n" + row2 + "\n" + row3