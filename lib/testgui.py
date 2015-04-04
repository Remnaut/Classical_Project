from FluidSimulation import *

from pyglet_gui.gui import Label
from pyglet_gui.manager import Manager
from pyglet_gui.buttons import Button
from pyglet_gui.constants import ANCHOR_TOP_LEFT

import Themes

# Set up a Manager
Manager(Label("Drag me"), window=window,
        batch=batch,
        theme=Themes.button_theme)

Manager(Button("Drag me"), window=window,
        batch=batch,
        anchor=ANCHOR_TOP_LEFT,
        theme=Themes.button_theme)

pyglet.app.run()