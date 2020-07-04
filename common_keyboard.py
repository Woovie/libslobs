import keyboard

class KeyboardHandler:
    def __init__(self):
        self.bindmode = False

    async def key_loop(self):
        while not self.bindmode:
            if pressed := keyboard.read_key():
                #Here we can store different key presses, maybe do an array of {"a": some_function}
                return pressed
        else:
            if pressed := keyboard.read_key():
                #Create a new binding, ensure the bind doesn't match any other
                return pressed

    def tick(self):
        while True:
            return