import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen,SlideTransition
from kivy.core.window import Window
red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue =  [0, 0, 1, 1]
purple = [1, 0, 1, 1]
class MyApp(App):
    def build(self):
        screenmenu = Screen(name='Menu')
        screenmenu1 = Screen(name='scr2')
        self.sm = ScreenManager(transition=SlideTransition())
        self.sm.add_widget(screenmenu)
        self.sm.add_widget(screenmenu1)
        hl = BoxLayout(orientation = "vertical")
        colors = [red, green, blue, purple]
        screenmenu.add_widget(hl)
        img = Image(source='hahaha.jpg')
        txt = Label(text = 'Привет я бабушка Олег! Начни работу, а то съем.')
        button = Button(text = 'Начать Работу!',
                    background_color = random.choice(colors))
        button.bind(on_press=self.on_press_button)
        hl.add_widget(img)
        hl.add_widget(txt)
        hl.add_widget(button)
        return self.sm
    def on_press_button(self, instance):
        self.sm.current = 'scr2'
Window.size = (450 , 935)
app=MyApp()
app.run()