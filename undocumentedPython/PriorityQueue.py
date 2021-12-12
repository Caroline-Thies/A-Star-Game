# standard lib for this does not reorder itself when priority of saved item changes
class PriorityQueue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        self.items.sort()
        to_return = self.items[0]
        self.items.remove(to_return)
        return to_return

    def __contains__(self, item):
        return item in self.items

    def __str__(self):
        string = "[ "
        for item in self.items:
            string += " " + str(item) + " "
        string += "]"
        return string

    def is_empty(self):
        return len(self.items) < 1
