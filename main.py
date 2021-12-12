from kivy.app import App
from kivy.uix.text import Text
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
class MyApp(App):
    def build(self):
        txt = Text(text = 'Всем привет я бабушка Олеееег!!!!!!!!!!!! Начни работу а то съем.')
        button = Button(but='Начать Работу!')
        return txt
app=MyApp()
app.run()