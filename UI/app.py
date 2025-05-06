import pyglet

from UI.demo_constructor import Constructor

class App:
    def __init__(self, W, H):
        self.window = WindowAle(width=W, height=H, caption='Course1', resizable=True, file_drops=True)


    def run(self):
        pyglet.app.run()



class WindowAle(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.batch = pyglet.graphics.Batch()
        self.constructor = Constructor(kwargs['width'], kwargs['height'], self.batch)


    def on_draw(self) -> None:
        self.clear()
        self.batch.draw()