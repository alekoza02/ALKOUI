import pyglet

from UI.UI_base_element import BaseElement

class Constructor:
    def __init__(self, W, H, batch):
        self.riquadri = [BaseElement(i*W/10, i*H/10, W/10, H/10, batch) for i in range(10)]