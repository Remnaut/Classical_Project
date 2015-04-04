import pyglet, Themes
from Constants import *
from pyglet_gui.manager import Manager
from Assets import MenuButton

class InfoMenu(object):

    def __init__(self):
        self.batch = pyglet.graphics.Batch()
        self.info_text = 'resources/Info.txt'
        self.state=1
        self.defaultstate = 1

    def generate(self):
        f = open(self.info_text)
        lines = f.readlines()
        f.close()
        counter = 0
        for i in lines:
            textline = pyglet.text.Label(i[:-1],
                             font_name='Times New Roman',
                             font_size=16,
                             x=20, y=(460-counter*25),
                             batch=self.batch)

            textline.draw()
            counter +=1

        def callback(is_released):
            self.state = 0

        btnMenu = MenuButton(label='Menu', on_release=callback)

        Manager(btnMenu,window=window,
                        theme=Themes.button_theme,
                        is_movable=False,
                        batch=self.batch).set_position(280, 20)




