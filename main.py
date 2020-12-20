from kivy.config import Config
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from login.loginWindow import LoginWindow
from geolocator.geolocatorWindow import GeoLocatorWindow

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


class MainWindow(BoxLayout):
    login_widget = LoginWindow('screen_geolocator')
    geolocator_widget = GeoLocatorWindow()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.screen_login.add_widget(self.login_widget)
        self.ids.screen_geolocator.add_widget(self.geolocator_widget)


class MainApp(App):
    def build(self):
        return MainWindow()


if __name__ == '__main__':
    MainApp().run()
