class Token:
    def __init__(self, left: bool, right: bool, up: bool, down: bool):
        self.canReach = {"left": left, "right": right, "up": up, "down": down}

    def __str__(self):
        row1 = ""
        if self.canReach["up"]:
            row1 = "   |   "
        row2 = ""
        if self.canReach["left"]:
            row2 += "-- "
        else:
            row2 += "   "
        row2 += "*"
        if self.canReach["right"]:
            row2 += " --"
        else:
            row2 += "   "

        row3 = ""
        if self.canReach["down"]:
            row3 = "   |   "
        return row1 + "\n" + row2 + "\n" + row3

    def str_row1(self):
        if self.canReach["up"]:
            return "   |   "
        else:
            return "       "

    def str_row2(self, is_start: bool = False, is_goal: bool = False, is_player: bool = False):
        row2 = ""
        if self.canReach["left"]:
            row2 += "-- "
        else:
            row2 += "   "
        if is_player:
            row2 += "*"
        elif is_goal:
            row2 += "g"
        elif is_start:
            row2 += "s"
        else:
            row2 += "*"
        if self.canReach["right"]:
            row2 += " --"
        else:
            row2 += "   "
        return row2

    def str_row3(self):
        if self.canReach["down"]:
            return "   |   "
        else:
            return "       "
