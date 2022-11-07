"""
    where all custom exception are
"""


class EventNotHandled(Exception):
    def __init__(self, event):
        text = f"handler={event['handler']}"
        self.message = text
        super().__init__(self.message)
