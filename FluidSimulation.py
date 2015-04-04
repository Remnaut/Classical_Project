import pyglet, sys
from lib.Constants import window
from lib.Info import InfoMenu
from lib.Main import MainMenu

main_menu = MainMenu()
main_menu.generate()
info_menu = InfoMenu()

menu_list = [main_menu, info_menu]

active_batch = main_menu.batch
state = main_menu
current_state = 0


@window.event
def on_draw():
    window.clear()
    active_batch.draw()

def change_state(state_number):
    new_state = menu_list[state_number]
    global state
    state.state = state.defaultstate
    global active_batch
    new_state.generate()
    active_batch = new_state.batch
    global current_state
    current_state = new_state


def update(dt):
    global state
    if state.state != state.defaultstate:
        change_state(state.state)
        global current_state
        state = current_state

def main():

    pyglet.clock.schedule_interval(update, 1/60.0)

    pyglet.app.run()


if __name__ == '__main__':
    sys.exit(main())






