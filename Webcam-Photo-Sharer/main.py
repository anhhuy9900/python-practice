from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
import time
import webbrowser
from file_sharer import FileSharer

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.filepath = None

    def start(self):
        """Starts camera and changes Button text"""
        self.ids.camera.opacity = 1
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        """Stop camera and changes Button text"""
        self.ids.camera.opacity = 0
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        """Creates a filename with the current time and captures
        and saves a photo image under that filename"""
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filepath = f"files/capture-{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):
    link_message = "Create a Link First"

    def __init__(self, **kw):
        super().__init__(**kw)
        self.share_link_url = None

    def create_share_link(self):
        """Accesses the photo filepath, uploads it to the web,
        and inserts the link in the Label widget"""
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        file_sharer = FileSharer(file_path)
        self.share_link_url = file_sharer.share()
        self.ids.link.text = self.share_link_url

    def copy_share_link(self):
        """Copy link to the clipboard available for pasting"""
        try:
            Clipboard.copy(self.share_link_url)
        except:
            self.ids.link.text = self.link_message

    def open_share_link(self):
        """Open link with default browser"""
        try:
            webbrowser.open(self.share_link_url)
        except:
            self.ids.link.text = self.link_message


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
