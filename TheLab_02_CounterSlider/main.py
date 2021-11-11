import os
import sys
from pathlib import Path

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
# from kivy.uix.togglebutton import ToggleButton
from kivy.properties import StringProperty, BooleanProperty


root_path: Path = os.path.split((os.path.dirname(__file__)))[0]
sys.path.append(root_path)
# for import of Fonts dir
font_path: Path = os.path.join(root_path, f'Main/Fonts{os.sep}')


class WidgetsExamples(GridLayout):
    count = 0
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("0")
    # slider_value_txt = StringProperty("0")
    font_lcd: Path = os.path.join(font_path, "Lcd.ttf")
    print(font_lcd)

    def on_button_click(self):
        # print("Button clicked")
        if self.count_enabled:
            self.count += 1
            self.my_text = str(self.count)

    def on_toggle_button_state(self, widget):
        # print("toggle state" + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True

    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))


class TheLabApp(App):
    pass


TheLabApp().run()
