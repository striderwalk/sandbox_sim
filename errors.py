"""
    where all custom exception are
"""


class EventNotHandled(Exception):
    def __init__(self, event):
        self.message = f"handler={event['handler']}"
        super().__init__(self.message)


class ObjectNotFound(Exception):
    def __init__(self, obj):
        self.message = f"{obj}"
        super().__init__(self.message)
