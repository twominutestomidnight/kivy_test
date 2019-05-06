"""
run it to work program
pip install --upgrade pip wheel setuptools
pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text='Username:'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='Password:'))
        self.password = TextInput(multiline=False, password=True)
        self.add_widget(self.password)

        self.add_widget(Label(text='Two Factor Auth:'))
        self.tfa = TextInput(multiline=False, password=True)
        self.add_widget(self.tfa)


class TutorialApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    TutorialApp().run()
