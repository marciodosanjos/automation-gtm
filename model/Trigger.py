

class Trigger:
    type: str
    value: str
    id: str

    def __init__(self, type: str, value: str):
        self.type = type
        self.value = value
