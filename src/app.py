from services.postfix import Postfixconverter
from services.evaluator import Evaluator


class App:
    def __init__(self, io):
        self.io = io
        self.converter = Postfixconverter()
        self.evaluator = Evaluator()

    def run(self):
        while True:
            user_input = self.io.read("Komento:")

            if user_input == "":
                break
            self.io.write(user_input)
