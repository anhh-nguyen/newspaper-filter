from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.widget import Widget

from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '780')

class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("UI.kv")


class MyW(Widget):
    def b_smash(self): 
        print(self.ids.passw.text)



if __name__ == '__main__':
    app = MyMainApp()
    app.run()