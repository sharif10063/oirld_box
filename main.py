import qrcode
# from kivymd.uix.button import MDRectangleFlatButton
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, FadeTransition, ScreenManager
from kivy.lang import Builder
from kivy.uix.image import Image

import plyer
import time


# from PIL import Image


Window.size = 320, 550


class Function(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def generate_qr_code(self, root):

        code = qrcode.QRCode(version=1.00, box_size=15, border=4)
        code.add_data(self.ids.link_text.text)
        code.make(fit=True)
        img = code.make_image(fill='Black', back_color='White')
        img.save(f"{self.ids.image_name.text}.png")

    def make_another(self, root):
        self.ids.link_text.text = ''
        self.ids.image_name.text = ''
        root.current = 'first'

    def view_image(self, root):
        self.ids.img_.source = f'{self.ids.image_name.text}.png'
        time.sleep(0.5)
        root.current = 'Result'


class MainApp(MDApp):
    def build(self):
        Builder.load_file('layout.kv')
        self.theme_cls.primary_palette = 'Green'
        return Function()

    def show_notification(self):
        plyer.notification.notify(
            title='QR Code generator', message="Qr code created")


if __name__ == '__main__':

    MainApp().run()
