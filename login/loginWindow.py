from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file('login/loginWindow.kv')


class LoginWindow(BoxLayout):
    def __init__(self, target_screen, **kwargs):
        super().__init__(**kwargs)
        self.target_screen = target_screen

    def validate_user(self):
        user_field = self.ids.username_field
        password_field = self.ids.pwd_field
        info_field = self.ids.info

        username = user_field.text
        password = password_field.text

        if username == '' or password == '':
            info_field.text = '[color=#FF0000]Username and Password are required![/color]'
        else:
            if username == 'demo' and password == 'demo':
                info_field.text = '[color=#00FF00]Logged In successfully![/color]'
                self.parent.parent.current = self.target_screen
            else:
                info_field.text = '[color=#FF0000]Invalid Username and/or Password[/color]'


class LoginApp(App):
    def build(self):
        return LoginWindow(None)


if __name__ == "__main__":
    la = LoginApp()
    la.run()
