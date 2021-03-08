class Lamp:
    def __init__(self, color):
        self.color = color
        self.on = False

    def toggle_switch(self):
        self.on ^= True

    def state(self):
        return "The lamp is {}.".format("on" if self.on else "off")
