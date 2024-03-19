from collections import deque


class Postfixconverter:
    def __init__(self):
        self.stack = []
        self.queue = deque([])
