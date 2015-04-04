from pyglet_gui.buttons import OneTimeButton, Button


class MenuButton(OneTimeButton):

    def __init__(self, path='my_path', *args, **kwargs):
        super(MenuButton, self).__init__(*args, **kwargs)

        self.path = path

    def get_path(self):
        path = [self.path]
        if self.is_pressed:
            path.append('down')
        else:
            path.append('up')
        return path

class ReturnToMenu(MenuButton):

    def __init__(self, *args, **kwargs):
        super(ReturnToMenu, self).__init__(*args, **kwargs)

