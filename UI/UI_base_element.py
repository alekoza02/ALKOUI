import pyglet

class BaseElement:
    def __init__(self, x, y, w, h, batch):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.batch = batch
        self.color = [148, 177, 255]

        self.update_square()

    
    def update_position(self, new_x=None, new_y=None, new_w=None, new_h=None):
        if not new_x is None: self.x = new_x
        if not new_y is None: self.y = new_y
        if not new_w is None: self.w = new_w
        if not new_h is None: self.h = new_h
        self.update_square()


    def update_square(self):
        self.square = pyglet.shapes.Rectangle(
            x=self.x,
            y=self.y,
            width=self.w,
            height=self.h,
            color=self.color,
            batch=self.batch
        )