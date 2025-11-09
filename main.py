from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from plyer import filechooser
import os
# import aes_engine

Window.size = (400, 600)

class MainScreen(Screen):
    pass

class EncryptScreen(Screen):
    pass

class DecryptScreen(Screen):
    pass

class AESApp(App):
    selected_file = None
    mode = None

    def build(self):
        return Builder.load_file("main.kv")

    def select_file(self, mode):
        self.mode = mode
        files = filechooser.open_file(title="Pick a file")
        if files:
            self.selected_file = files[0]
            screen = self.root.get_screen(mode)
            screen.ids.status.text = f"Selected: {os.path.basename(self.selected_file)}"

    def encrypt_selected(self, password):
        if not self.selected_file or not password:
            self.root.get_screen("encrypt").ids.status.text = "Select file and enter password"
            return
        try:
            # output = aes_engine.encrypt_file(self.selected_file, password)
            self.root.get_screen("encrypt").ids.status.text = f"Encrypted → {output}"
        except Exception as e:
            self.root.get_screen("encrypt").ids.status.text = f"Error: {str(e)}"

    def decrypt_selected(self, password):
        if not self.selected_file or not password:
            self.root.get_screen("decrypt").ids.status.text = "Select file and enter password"
            return
        try:
            # output = aes_engine.decrypt_file(self.selected_file, password)
            self.root.get_screen("decrypt").ids.status.text = f"Decrypted → {output}"
        except Exception as e:
            self.root.get_screen("decrypt").ids.status.text = f"Error: {str(e)}"

if __name__ == "__main__":
    AESApp().run()
