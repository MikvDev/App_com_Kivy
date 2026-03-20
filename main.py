from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

class gerenciadorTelas(ScreenManager):
    pass
class primeiraTela(Screen):
    pass
class segundaTela(Screen):
    pass
class MyApp(App):  # vai ser uma janela
    def build(self): # vai ser o conteúdo da janela 
        sm = gerenciadorTelas() # não da para colocar varias coisas aqui, button, tela...
        sm.add_widget(primeiraTela(name="primeiraTela"))
        sm.add_widget(segundaTela(name="segundaTela"))
        return sm
MyApp().run()