from pyglet_gui.theme import Theme

button_theme = Theme({"font": "Ubuntu",
               "font_size": 14,
               "text_color": [255, 255, 255, 255],
               "gui_color": [100, 100, 100, 255],
               "my_path": {
                   "down": {
                       "image": {
                           "source": "button-down.png",
                           "frame": [8, 6, 2, 2],
                           "padding": [18, 18, 8, 6]
                       },
                       "text_color": [0, 0, 0, 255],
                       "gui_color": [255, 255, 255, 255],

                   },
                   "up": {
                       "image": {
                           "source": "button.png",
                           "frame": [8, 5, 6, 3],
                           "padding": [18, 18, 8, 6]
                       }
                   }
               }
              }, resources_path='/Programs/pyglet-gui-master/theme')

title_theme = Theme({"font": "Trebuchet MS",
               "font_size": 22,
               "text_color": [255, 255, 255, 255],
               "gui_color": [255, 255, 255, 255],
               "my_path": {
                   "down": {
                       "image": {
                           "source": "WaveSoftEdges.png",
                           "frame": [8, 6, 2, 2],
                           "padding": [18, 18, 8, 6]
                       },
                   },
                   "up": {
                       "image": {
                           "source": "WaveSoftEdges.png",
                           "frame": [10, 10, 16, 3],
                           "padding": [30, 30, 40, 6]
                       }
                   }
               }
              }, resources_path='resources')

