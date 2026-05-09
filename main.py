from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatButton, MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.list import MDList, OneLineListItem
from kivy.uix.scrollview import ScrollView

# Наш фирменный нежно-зеленый
SOFT_GREEN = (0.7, 0.9, 0.7, 1)

class LoginScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = MDBoxLayout(orientation='vertical', spacing="20dp", padding="40dp", pos_hint={"center_y": .5})
        
        self.username = MDTextField(
            hint_text="Имя пользователя", 
            mode="round",
            line_color_focus=SOFT_GREEN
        )
        self.password = MDTextField(
            hint_text="Пароль", 
            password=True, 
            mode="round",
            line_color_focus=SOFT_GREEN
        )
        
        login_btn = MDFillRoundFlatButton(
            text="ВОЙТИ", 
            md_bg_color=SOFT_GREEN,
            text_color=(0, 0, 0, 1),
            size_hint_x=1,
            on_release=self.go_to_chat
        )
        
        reg_btn = MDFillRoundFlatButton(
            text="ЗАРЕГИСТРИРОВАТЬСЯ",
            md_bg_color=(1, 1, 1, 1),
            text_color=(0, 0, 0, 1),
            size_hint_x=1
        )
        
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(login_btn)
        layout.add_widget(reg_btn)
        self.add_widget(layout)

    def go_to_chat(self, instance):
        self.manager.current = 'chat'

class ChatScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = MDBoxLayout(orientation='vertical')
        
        # Верхняя панель: фон черный, текст белый
        toolbar = MDTopAppBar(
            title="SQUARI", 
            elevation=2, 
            md_bg_color=(0.05, 0.05, 0.05, 1), # Глубокий темный
            specific_text_color=(1, 1, 1, 1)    # Белый текст
        )
        
        scroll = ScrollView()
        self.chat_list = MDList()
        scroll.add_widget(self.chat_list)
        
        input_area = MDBoxLayout(adaptive_height=True, padding="10dp", spacing="10dp")
        self.msg_input = MDTextField(
            hint_text="Начни писать...", 
            mode="round",
            line_color_focus=SOFT_GREEN
        )
        
        send_btn = MDIconButton(
            icon="star", 
            theme_icon_color="Custom",
            icon_color=SOFT_GREEN,
            on_release=self.send_msg
        )
        
        input_area.add_widget(self.msg_input)
        input_area.add_widget(send_btn)
        
        layout.add_widget(toolbar)
        layout.add_widget(scroll)
        layout.add_widget(input_area)
        self.add_widget(layout)

    def send_msg(self, *args):
        if self.msg_input.text:
            self.chat_list.add_widget(OneLineListItem(
                text=f"Вы: {self.msg_input.text}",
                theme_text_color="Custom",
                text_color=(1, 1, 1, 1)
            ))
            self.msg_input.text = ""

class SquariApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray" 
        
        sm = MDScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(ChatScreen(name='chat'))
        return sm

if __name__ == "__main__":
    SquariApp().run()
