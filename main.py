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
        screenmenu1 = Screen(name='Wiki')
        screenmenu2 = Screen(name='Advices')
        screenmenu3 = Screen(name='Advice1')
        screenmenu4 = Screen(name='Advice2')
        screenmenu5 = Screen(name='Advice3')
        screenmenu6 = Screen(name='Advice4')
        screenmenu7 = Screen(name='Advice5')
        self.sm = ScreenManager(transition=SlideTransition())
        self.sm.add_widget(screenmenu)
        self.sm.add_widget(screenmenu1)
        self.sm.add_widget(screenmenu2)
        self.sm.add_widget(screenmenu3)
        self.sm.add_widget(screenmenu4)
        self.sm.add_widget(screenmenu5)
        self.sm.add_widget(screenmenu6)
        self.sm.add_widget(screenmenu7)
        hl = BoxLayout(orientation = "vertical")
        colors = [red, green, blue, purple]
        screenmenu.add_widget(hl)
        img = Image(source='hahaha.jpg')
        txt = Label(text = 'Привет я бабушка Олег! Начни работу, а то съем.')
        button = Button(text = 'Начать Работу!',
                        background_color=random.choice(colors))
        button.bind(on_press=self.on_press_button)
        hl.add_widget(img)
        hl.add_widget(txt)
        hl.add_widget(button)
        hl1 = BoxLayout(orientation="vertical")
        screenmenu1.add_widget(hl1)
        img = Image(source='med.jpg')
        txt = Label(text='ПРЕДУПРЕЖДЕНИЕ!!!!!!!!'
                         'Народная медицина – часть альтернативной медицины,методах и средствах лечения,'
                         ' которые передаются в народе из поколения в поколение.Но также народная медицина может'
                         ' включать элементы магии, эзотерики и «альтернативные», часто неэффективные, или даже опасные'
                         ' методы лечения.Поэтому читая эти статьи вы принимаете то что вы сами отвичаете за свою '
                         'жизнь', text_size=(300, None))
        button = Button(text = 'Я соглашаюсь с тем что вы сами отвичаете за свою жизнь.',
                        text_size=(300, None),
                        background_color = random.choice(colors))
        button.bind(on_press=self.on_press_button1)
        hl1.add_widget(img)
        hl1.add_widget(txt)
        hl1.add_widget(button)
        hl2 = BoxLayout(orientation="vertical")
        screenmenu2.add_widget(hl2)
        button = Button(text = 'Полоскание водой при инфекциях верхних дыхательных путей' ,text_size=(300, None),
                        background_color = random.choice(colors))
        button.bind(on_press=self.on_press_button2)
        button1 = Button(text='Имбирь при тошноте', text_size=(300, None),
                        background_color=random.choice(colors))
        button1.bind(on_press=self.on_press_button3)
        button2 = Button(text='Куриный бульон при простуде', text_size=(300, None),
                        background_color=random.choice(colors))
        button2.bind(on_press=self.on_press_button4)
        button3 = Button(text='Яблоки и морковь для белых зубов', text_size=(300, None),
                        background_color=random.choice(colors))
        button3.bind(on_press=self.on_press_button5)
        button4 = Button(text='Мед при кашле', text_size=(300, None),
                        background_color=random.choice(colors))
        button4.bind(on_press=self.on_press_button6)
        hl2.add_widget(button)
        hl2.add_widget(button1)
        hl2.add_widget(button2)
        hl2.add_widget(button3)
        hl2.add_widget(button4)
        hl3 = BoxLayout(orientation="vertical")
        screenmenu3.add_widget(hl3)
        txt = Label(text='Чувствуете, что простудились? Попробуйте начать полоскать горло обычной водой.'
                         ' Исследование около 400 здоровых добровольцев показало, что те, кто полоскал горло простой'
                         ' водой, в течение периода исследования значительно реже заболевали инфекциями верхних'
                         ' дыхательных путей (ИВДП) — этот тип инфекций часто связан с простудой и гриппом.'
                         ' Исследователи пришли к выводу, что полоскание простой водой было эффективным для'
                         ' предотвращения ИВДП среди здоровых людей.', text_size=(300, None))
        button = Button(text='Обратно')
        button.bind(on_press=self.on_press_button7)
        img = Image(source='Advice1.jpg')
        hl3.add_widget(txt)
        hl3.add_widget(img)
        hl3.add_widget(button)
        hl4 = BoxLayout(orientation="vertical")
        screenmenu4.add_widget(hl4)
        button = Button(text='Обратно')
        button.bind(on_press=self.on_press_button7)
        img= Image(source='Advice2.jpg')
        txt = Label(text='Если вы испытываете сложности при морских прогулках, попробуйте пару имбирных конфет.'
                         ' Сравнивая людей, принимающих плацебо, с теми, кто принимал имбирь, исследователи обнаружили,'
                         ' что всего лишь один грамм этого корня облегчает симптомы морской болезни, утренней тошноты и'
                         ' тошноты при химиотерапии. В целом имбирь также может быть полезен для уменьшения'
                         ' газообразования и при расстройстве желудка.', text_size=(300, None))
        hl4.add_widget(txt)
        hl4.add_widget(img)
        hl4.add_widget(button)
        hl5 = BoxLayout(orientation="vertical")
        screenmenu5.add_widget(hl5)
        button = Button(text='Обратно')
        button.bind(on_press=self.on_press_button7)
        img = Image(source='Advice3.jpg')
        txt = Label(text='Мама была права. Всё еще точно не известно, почему куриный бульон заставляет нас чувствовать'
                         ' себя лучше во время болезни, но исследователи почти уверены в его действенности.'
                         ' Во время одного эксперимента ученые попробовали определить эффект, который бульон оказывал'
                         ' на воспаление (общий компонент простуды). В результате они обнаружили замедление движения'
                         ' нейтрофилов — белых кровяных клеток, которые являются отличительной чертой острой инфекции.'
                         ' Другими словами, бульон, кажется, помогает снять воспаление, которое вызывает много'
                         ' симптомов простуды.', text_size=(300, None))
        hl5.add_widget(txt)
        hl5.add_widget(img)
        hl5.add_widget(button)
        txt = Label(text='Пока у вас целая барабанная перепонка, можно использовать этот легкий рецепт от клиники Майо'
                         ' для предотвращения ушных инфекций. Просто смешайте одну часть белого уксуса с одной частью'
                         ' спирта, залейте чайную ложку смеси в каждое ухо и слейте ее обратно. Смесь предназначена для'
                         ' остановки роста бактерий и грибков, которые развиваются в ушах'
                         ' пловцов.', text_size=(300, None))


        txt = Label(text='Ненавидите вкус сиропа от кашля? Всемирная организация здравоохранения рекомендует мед в'
                         ' качестве лекарства от кашля для детей. Исследования, проведенные в 2012 году среди 300'
                         ' детей, которые были больны в течение недели или меньше, обнаружили, что у тех, кому перед'
                         ' сном давали 10 г меда, было меньше симптомов кашля'
                         ' (по сравнению с теми, кто получал плацебо) и они, как ни странно, спали более крепким и'
                         ' спокойным сном.', text_size=(300, None))
        return self.sm
    def on_press_button(self, instance):
        self.sm.current = 'Wiki'
    def on_press_button1(self, instance):
        self.sm.current = 'Advices'
    def on_press_button2(self, instance):
        self.sm.current = 'Advice1'
    def on_press_button3(self, instance):
        self.sm.current = 'Advice2'
    def on_press_button4(self, instance):
        self.sm.current = 'Advice3'
    def on_press_button5(self, instance):
        self.sm.current = 'Advice4'
    def on_press_button6(self, instance):
        self.sm.current = 'Advice5'
    def on_press_button7(self, instance):
        self.sm.current = 'Advices'
Window.size = (450 , 935)
app=MyApp()
app.run()