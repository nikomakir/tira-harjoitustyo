class App:
    def __init__(self, io):
        self.io = io

    def run(self):
        while True:
            user_input = self.io.read("Komento:")

            if user_input == "":
                break
            self.io.write(user_input)
