

class Trigger:
    name: str
    type: str
    filter: list

    def __init__(self, name: str, type: str, filter: list):
        self.name = name
        self.type = type
        self.filter = filter
