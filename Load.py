import pyglet
from pyglet.gl import *
from pyglet.image import ImageData


window = pyglet.window.Window()


class ImageResource(ImageData):

    def __init__(self, x, y, path='', format='RGBA', batch=None):
        super(LoadImage, self).__init__()
        self.x = x
        self.y = y
        self.image_file = pyglet.image.load(path)
        self.format = format

    def draw(self):
        window.clear()
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        self.blit(self.x, self.y)
        glDisable(GL_BLEND)

title_image = pyglet.image.load('resources/WaveSoftEdges.png')
title_image = title_image.get_image_data()
format = 'RGBA'
pitch = title_image.width * len(format)
pixels = title_image.get_data(format, pitch)
title_image = ImageData(width=title_image.width, height=title_image.height, data=pixels, format=format, pitch=pitch).get_texture()
print title_image



@window.event
def on_draw():
    window.clear()
    glEnable(title_image)
    glBindTexture(title_image.GL_TEXTURE_2D, title_image.id)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    title_image.blit(0, 240)
    glDisable(GL_BLEND)
    glDisable(title_image.GL_TEXTURE_2D)

pyglet.app.run()