import pyglet, Themes, sys

from Constants import window
from pyglet_gui.manager import Manager
from pyglet_gui.containers import GridContainer, Spacer
from Assets import MenuButton

class MainMenu(object):

    def __init__(self):
        self.batch = pyglet.graphics.Batch()
        self.state = 0
        self.defaultstate = 0


    def generate(self):

        def callback(is_released):
            self.state = 1


        title = MenuButton()
        Manager(title, window=window,
                        theme=Themes.title_theme,
                        is_movable=False,
                        batch=self.batch).set_position(20, 240)

        btnFree = MenuButton(label=' Free ', on_release=callback)
        btnDemo = MenuButton(label='Demo')
        btnExit = MenuButton(label='  Exit  ')
        btnInfo = MenuButton(label='  Info  ')

        Manager(GridContainer([[btnFree, Spacer(50, 100), btnDemo],
                                    [btnExit, Spacer(), btnInfo]]),
                                     window=window,
                                     is_movable=False,
                                     theme=Themes.button_theme,
                                     batch=self.batch).set_position(204, 100)




